# The Second Mind - AI-Powered Research System

## 🚀 Project Overview
The Second Mind is an AI-driven multi-agent system designed to mimic human learning. It iteratively refines research outputs using **real-time web data** and **stored memory**, making smarter decisions over multiple cycles.

This system was developed for the **IIT Hyderabad Hackathon** and leverages specialized AI agents to improve research insights dynamically.

---
##🧠 How It Works
Our system consists of **six specialized agents** managed by a **Supervisor Agent**:
1. **Generation Agent** – Retrieves initial ideas from web data (Google Search API, BeautifulSoup).
2. **Reflection Agent** – Validates data coherence and relevance.
3. **Ranking Agent** – Scores research ideas using NLP (TF-IDF, Cosine Similarity).
4. **Evolution Agent** – Refines ideas based on trends and new research.
5. **Proximity Agent** – Recalls past research to enhance continuity.
6. **Meta-Review Agent** – Evaluates improvements and suggests refinements.

Each query undergoes **multiple cycles**, where weak ideas are replaced with stronger, more relevant alternatives.

---
## 🔑 Key Features
✅ **Memory-Driven Learning** – Stores past queries and intelligently recalls relevant insights.
✅ **Real-Time Web Extraction** – Uses Google Search API and fallback web scraping.
✅ **Iterative Refinement** – Improves research outputs over multiple cycles.
✅ **Clear Console Output** – Displays agent interactions and decision-making process.
✅ **Scalability** – Can be expanded with additional agents for deeper learning.

---
## ⚙️ Setup & Execution
### 1️⃣ Install Dependencies
Ensure Python 3.8+ is installed. Then, run:
```bash
pip install requests beautifulsoup4 scikit-learn nest-asyncio
```

### 2️⃣ Set Up Google Search API (Optional)
- Create a Google Search API key and Custom Search Engine ID.
- Add them to environment variables:
```bash
export GOOGLE_API_KEY='your_api_key'
export CUSTOM_SEARCH_ENGINE_ID='your_cse_id'
```

### 3️⃣ Run the System
Execute the script:
```bash
python main.py
```

---
🏆 Example Output
Query:"Renewable energy for urban areas"
```
🚀 Processing Query: Renewable energy for urban areas

🔗 Proximity Suggestion: No prior relevant data found.

================== Cycle 1 ==================
🧠 Generation → Retrieved: 'Smart grids for urban energy efficiency' from web data.
🔍 Reflection → Validated: Confirmed: Smart grids for urban energy efficiency (savings: 30%)
📊 Ranking → Scored: 4/10
🔄 Evolution → Refined: 'Smart grids' → 'Wind turbines integrated into buildings', Score: 6/10
💾 Memory → Stored: 'Wind turbines integrated into buildings - Score: 6/10'.
📌 Meta-Review → Consider refining ranking and exploring hybrid solutions.

================== Cycle 2 ==================
🧠 Generation → Retrieved: 'Wind turbines integrated into buildings' from memory.
📊 Ranking → Scored: 6/10
🔄 Evolution → Refined: 'Wind turbines' → 'Solar panels on rooftops', Score: 8/10
💾 Memory → Stored: 'Solar panels on rooftops - Score: 8/10'.
📌 Meta-Review → Strong improvement. Consider economic feasibility studies.

================== Cycle 3 ==================
🧠 Generation → Retrieved: 'Solar panels on rooftops' from memory.
📊 Ranking → Scored: 8/10
🔄 Evolution → No further improvement found.
💾 Memory → Stored: 'Solar panels on rooftops - Score: 8/10'.
📌 Meta-Review → Optimized solution reached.
```

---
## 📌 Why This Project Stands Out
- Simulates human-like research thinking** – Retains knowledge and iteratively improves insights.
- Handles real-world data** – Uses live web data for research enhancement.
- Efficient agent collaboration** – Specialized agents work together to refine outputs.
- Scalable & adaptable** – Can be expanded with more agents and improved NLP models.

This project demonstrates a highly functional and scalable approach to AI-driven research. 🚀



