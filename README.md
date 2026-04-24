# 🔬 ResearchMind AI: Multi-Agent Research System

**ResearchMind AI** ek advanced research tool hai jo internet se information nikalne, use padhne, aur ek professional report taiyaar karne ke liye 4 alag-alag AI Agents ka use karta hai. Ye bilkul ek research team ki tarah kaam karta hai!

---

## 🌟 Key Features
*   **Multi-Agent Collaboration:** Ek agent search karta hai, dusra padhta hai, teesra likhta hai, aur chautha review karta hai.
*   **Deep Web Scraping:** Sirf search results nahi, balki ye actual website ke andar jaakar gehraayi se information nikalta hai.
*   **Professional Reports:** Markdown format mein structured aur detailed research reports.
*   **AI Quality Check:** Ek dedicated 'Critic' agent har report ko score deta hai aur improvements suggest karta hai.
*   **Premium UI:** Streamlit se bana ek modern aur clean user interface.

---

## 🤖 Meet the Research Team (Agents)
Ye project **Mistral AI** ke dimaag aur **LangChain** ke framework par chalta hai:

1.  **🔍 The Searcher:** Ye internet par sabse sahi aur latest links dhundta hai.
2.  **📄 The Reader:** Ye sabse acche article ko pura padhta hai aur usme se kaam ki baatein nikalta hai.
3.  **✍️ The Writer:** Ye saari information ko ek sundar aur structured report mein badalta hai.
4.  **🧐 The Critic:** Ye report ki quality check karta hai aur use 10 mein se score deta hai.

---

## 🛠 Tech Stack
*   **Language:** Python 3.11+
*   **Framework:** LangChain (Agentic Workflow)
*   **AI Brain:** Mistral AI (`open-mistral-7b`)
*   **Tools:** Tavily Search API, BeautifulSoup4
*   **Frontend:** Streamlit

---

## 🚀 Getting Started

### 1. Prerequisites
Aapke paas ye API keys honi chahiye:
*   **Mistral API Key** (From [Mistral Console](https://console.mistral.ai/))
*   **Tavily API Key** (From [Tavily AI](https://tavily.com/))

### 2. Installation
Repository ko clone karein aur dependencies install karein:

```bash
# Clone the repo
git clone https://github.com/Yashu-sarv/multi-agent-research-system.git
cd multi-agent-research-system

# Virtual environment banayein aur activate karein
python -m venv venv
source venv/bin/activate  # Windows ke liye: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
```

### 3. Environment Setup
Project root mein ek `.env` file banayein aur apni keys dalein:
```env
MISTRAL_API_KEY=your_mistral_key_here
TAVILY_API_KEY=your_tavily_key_here
```

### 4. Run the App
```bash
streamlit run app.py
```

---

## 📂 Project Structure
*   `app.py`: Streamlit Dashboard (Main UI)
*   `agents.py`: AI Agents ki definition aur logic.
*   `tools.py`: Search aur Scraping functions.
*   `pipeline.py`: Pure process ka backend flow.
*   `requirements.txt`: Project ki saari dependencies.

---

## 📄 License
This project is licensed under the MIT License.

---

**Made with ❤️ using Mistral AI & LangChain**
