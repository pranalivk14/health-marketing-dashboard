🏥 Healthcare Marketing Analytics Dashboard
An AI-powered analytics dashboard that analyses 200,000+ marketing campaign records and lets you ask questions about the data in plain English — powered by Python, Streamlit, and Google Gemini.
🔗 View Live App

What it does

Loads and processes 200,000 rows of real marketing campaign data
Displays 4 interactive charts — channel performance, monthly spend trends, cost per acquisition by segment, and regional conversion heatmap
Sidebar filters let you slice data by channel and region in real time
AI Analyst panel — type any question in plain English and Google Gemini answers using the actual data as context


Screenshots

Add a screenshot here — take one with Cmd+Shift+4 on Mac and drag it into this folder


Tech Stack
ToolPurposePython 3.10+Core languageStreamlitWeb app frameworkpandasData loading and transformationPlotlyInteractive chartsGoogle Gemini APIAI analyst (natural language Q&A)python-dotenvEnvironment variable management

Project Structure
health-marketing-dashboard/
├── app.py               # Main Streamlit app
├── data_loader.py       # Loads and cleans CSV data
├── ai_analyst.py        # Handles Gemini API calls
├── charts.py            # All chart functions
├── requirements.txt     # Python dependencies
├── .env                 # API key (never committed)
├── .gitignore           # Ignores .env and venv
└── data/
    └── health_marketing.csv  # Dataset (200k rows)

Data
Uses the Marketing Campaign Performance Dataset from Kaggle — 200,000 records across multiple channels, regions, demographics and campaign types.
Key columns used:

Channel_Used → marketing channel (Email, Social Media, Google Ads etc.)
Acquisition_Cost → spend per campaign
Impressions → total reach
Clicks → used as conversion proxy
Location → regional breakdown
Target_Audience → age segment


Run Locally
1. Clone the repo
bashgit clone https://github.com/YOUR-USERNAME/health-marketing-dashboard.git
cd health-marketing-dashboard
2. Create and activate virtual environment
bashpython -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
3. Install dependencies
bashpip install -r requirements.txt
4. Add your API key
Create a .env file in the project root:
GOOGLE_API_KEY=your-google-ai-studio-key-here
Get a free API key at aistudio.google.com
5. Run the app
bashstreamlit run app.py
Opens at http://localhost:8501

Key Learnings
Building this project taught me:

How to build and deploy a full Python web application end-to-end
Connecting a data pipeline to an LLM API (Google Gemini)
pandas data transformation — groupby, aggregation, cleaning real-world messy data
Streamlit for rapid interactive dashboard development
Git and GitHub for version control and deployment


What's Next
This is Project 1 of a 3-project AI/ML portfolio:

Project 2 — Automated report generator (LLM-written summaries + PDF output)
Project 3 — RAG chatbot on domain-specific documents


Author
Pranali Kulkarni
Data Analyst transitioning into AI/ML Engineering
LinkedIn · GitHub
