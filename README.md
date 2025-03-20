# The Second Mind - AI-Powered Research System

## 🚀 Project Overview
The Second Mind is an AI-driven multi-agent system designed to mimic human learning. It iteratively refines research outputs using **real-time web data** and **stored memory**, making smarter decisions over multiple cycles.

This system was developed for the **IIT Hyderabad Hackathon** and leverages specialized AI agents to improve research insights dynamically.

---
##🧠 How It Works
Our system consists of **six specialized agents** managed by a **Supervisor Agent**:
1. Generation Agent– Retrieves initial ideas from web data (Google Search API, BeautifulSoup).
2. Reflection Agent – Validates data coherence and relevance.
3. Ranking Agent – Scores research ideas using NLP (TF-IDF, Cosine Similarity).
4. Evolution Agent – Refines ideas based on trends and new research.
5. Proximity Agent – Recalls past research to enhance continuity.
6. **Meta-Review Agent – Evaluates improvements and suggests refinements.

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
Query:"urban energy solutions"
```
🚀 Processing Query: urban energy solutions
🔎 Debug: Current stored queries: [('urban energy solutions', 'Hydrogen fuel cells for city transport', 5)]
🔗 Proximity Suggestion: Consider revisiting 'Hydrogen fuel cells for city transport' from previous research.

================== Cycle 1 ==================

🧠 Generation → Retrieved: 'Wind turbines integrated into buildings' from web data.
🔍 Reflection → Validated: Confirmed: Wind turbines integrated into buildings (efficiency: 75%)
📊 Ranking → Scored: 3/10
🔄 Evolution → Refined: 'Wind turbines integrated into buildings' → 'Solar panels on rooftops', Score: 6/10
💾 Memory → Stored: 'Solar panels on rooftops - Score: 6/10'.
🔎 Debug: Stored queries after cycle: [('urban energy solutions', 'Solar panels on rooftops', 6)]
📌 Meta-Review → Feedback: Meta-review: Moderate improvement. Consider refining ranking and evolution further.
====================================================

================== Cycle 2 ==================

🧠 Generation → Retrieved: 'Solar panels on rooftops' from web data.
🔍 Reflection → Validated: Confirmed: Solar panels on rooftops (efficiency: 75%)
📊 Ranking → Scored: 3/10
🔄 Evolution → Refined: 'Solar panels on rooftops' → 'Wind turbines integrated into buildings', Score: 5/10
💾 Memory → Stored: 'Wind turbines integrated into buildings - Score: 5/10'.
🔎 Debug: Stored queries after cycle: [('urban energy solutions', 'Wind turbines integrated into buildings', 5)]
📌 Meta-Review → Feedback: Meta-review: Moderate improvement. Consider refining ranking and evolution further.
====================================================

================== Cycle 3 ==================
🧠 Generation → Retrieved: 'Wind turbines integrated into buildings' from web data.
🔍 Reflection → Validated: Confirmed: Wind turbines integrated into buildings (efficiency: 75%)
📊 Ranking → Scored: 3/10
🔄 Evolution → Refined: 'Wind turbines integrated into buildings' → 'Smart grids for urban energy efficiency', Score: 5/10
💾 Memory → Stored: 'Smart grids for urban energy efficiency - Score: 5/10'.
🔎 Debug: Stored queries after cycle: [('urban energy solutions', 'Smart grids for urban energy efficiency', 5)]
📌 Meta-Review → Feedback: Meta-review: Moderate improvement. Consider refining ranking and evolution further.

====================================================

---
## 📌 Why This Project Stands Out
- Simulates human-like research thinking** – Retains knowledge and iteratively improves insights.
- Handles real-world data** – Uses live web data for research enhancement.
- Efficient agent collaboration** – Specialized agents work together to refine outputs.
- Scalable & adaptable** – Can be expanded with more agents and improved NLP models.

This project demonstrates a highly functional and scalable approach to AI-driven research. 🚀



