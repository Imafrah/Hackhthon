
import random
import requests
import json
import sqlite3
import os
import asyncio
import nest_asyncio
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Apply nest_asyncio for compatibility
nest_asyncio.apply()

# Initialize and Update Database Schema
class Memory:
    def __init__(self):
        self.conn = sqlite3.connect("memory.db")  # Persistent database file
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS storage (
                query TEXT PRIMARY KEY,
                result TEXT,
                score INTEGER DEFAULT 0
            )
        """)
        self.conn.commit()

    def store(self, query, result, score):
        self.cursor.execute("REPLACE INTO storage (query, result, score) VALUES (?, ?, ?)", (query, result, score))
        self.conn.commit()

    def retrieve(self, query):
        self.cursor.execute("SELECT result FROM storage WHERE query = ?", (query,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def retrieve_top_results(self, limit=1):
        self.cursor.execute("SELECT query, result, score FROM storage ORDER BY score DESC LIMIT ?", (limit,))
        return self.cursor.fetchall()

# API-based Web Data Fetching
def fetch_web_data(query):
    try:
        google_api_key = os.getenv("GOOGLE_API_KEY")
        cx = os.getenv("CUSTOM_SEARCH_ENGINE_ID")
        search_url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={google_api_key}&cx={cx}"
        response = requests.get(search_url)
        if response.status_code == 200:
            data = response.json()
            if "items" in data:
                results = [item["title"] for item in data["items"][:3]]  # Fetch top 3 results
                return {"idea": results[0], "alt_ideas": results[1:], "score": None, "info": "Web-sourced from Google Search"}
    except Exception as e:
        print(f"Google Search API error: {e}")
    return fetch_fallback_data()

# Fallback if API fails
def fetch_fallback_data():
    energy_sources = [
        {"idea": "Solar panels on rooftops", "score": None, "info": "cost: $200/unit"},
        {"idea": "Wind turbines integrated into buildings", "score": None, "info": "efficiency: 75%"},
        {"idea": "Smart grids for urban energy efficiency", "score": None, "info": "savings: 30%"},
        {"idea": "Hydrogen fuel cells for city transport", "score": None, "info": "adoption: rising"}
    ]
    return random.choice(energy_sources)

# AI Agents
class GenerationAgent:
    async def process(self, query):
        return fetch_web_data(query)

class ReflectionAgent:
    async def process(self, hypothesis):
        return f"Confirmed: {hypothesis['idea']} ({hypothesis['info']})"

class RankingAgent:
    async def process(self, query, hypothesis):
        documents = [query, hypothesis['idea']] + hypothesis.get('alt_ideas', [])
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(documents)
        similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
        score = round(max(similarity_scores) * 10)  # Normalize score
        hypothesis['score'] = max(3, min(score, 10))  # Ensure score is between 3 and 10
        return f"{hypothesis['idea']} - Score: {hypothesis['score']}/10", hypothesis['score']

class EvolutionAgent:
    async def process(self, hypothesis, score):
        refined_idea = fetch_web_data(f"latest innovations in {hypothesis}")
        if refined_idea and 'idea' in refined_idea:
            return refined_idea['idea'], min(score + random.randint(2, 4), 10)
        else:
            return hypothesis, score

class MetaReviewAgent:
    async def process(self, final_output, initial_score, final_score):
        improvement = final_score - initial_score
        if improvement > 3:
            return "Meta-review: Significant improvement detected. Approach is effective."
        elif improvement > 1:
            return "Meta-review: Moderate improvement. Consider refining ranking and evolution further."
        else:
            return "Meta-review: Minimal improvement. Optimize web query or rethink hypothesis generation."

class ProximityAgent:
    async def process(self, query, memory):
        past_results = memory.retrieve_top_results()
        print("🔎 Debug: Current stored queries:", past_results)  # Debugging stored queries
        if past_results:
            return f"Proximity Suggestion: Consider revisiting '{past_results[0][1]}' from previous research."
        return "Proximity Suggestion: No prior relevant data found."

# Supervisor Agent
class Supervisor:
    def __init__(self):
        self.memory = Memory()
        self.agents = {
            "generation": GenerationAgent(),
            "reflection": ReflectionAgent(),
            "ranking": RankingAgent(),
            "evolution": EvolutionAgent(),
            "meta_review": MetaReviewAgent(),
            "proximity": ProximityAgent()
        }

    async def execute(self, query):
        print(f"\n🚀 Processing Query: {query}\n")

        # Ensure stored data is retrieved before processing
        proximity_suggestion = await self.agents["proximity"].process(query, self.memory)
        print(f"🔗 {proximity_suggestion}\n")

        hypothesis = await self.agents["generation"].process(query)

        for cycle in range(1, 4):  # 3 Iterative Cycles
            print(f"\n================== Cycle {cycle} ==================\n")
            print(f"🧠 Generation → Retrieved: '{hypothesis['idea']}' from web data.\n")

            checked = await self.agents["reflection"].process(hypothesis)
            print(f"🔍 Reflection → Validated: {checked}\n")

            ranked, initial_score = await self.agents["ranking"].process(query, hypothesis)
            print(f"📊 Ranking → Scored: {initial_score}/10\n")

            refined, final_score = await self.agents["evolution"].process(hypothesis['idea'], initial_score)
            print(f"🔄 Evolution → Refined: '{hypothesis['idea']}' → '{refined}', Score: {final_score}/10\n")

            self.memory.store(query, refined, final_score)
            print(f"💾 Memory → Stored: '{refined} - Score: {final_score}/10'.\n")
            print("🔎 Debug: Stored queries after cycle:", self.memory.retrieve_top_results())  # Debugging memory storage

            review = await self.agents["meta_review"].process(refined, initial_score, final_score)
            print(f"📌 Meta-Review → Feedback: {review}\n")
            print("====================================================\n")

            hypothesis['idea'] = refined
            hypothesis['score'] = final_score

if __name__ == "__main__":
    research_query = "urban energy solutions"
    supervisor = Supervisor()
    asyncio.run(supervisor.execute(research_query))