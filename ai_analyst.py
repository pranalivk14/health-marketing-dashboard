import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_about_data(question: str, stats: dict) -> str:
    """Send a question + data summary to Gemini and return the answer."""

    context = f"""
You are an analyst for a healthcare marketing team.
Here is a summary of the current campaign dataset:

- Date range: {stats['date_range']}
- Total spend: ${stats['total_spend']:,}
- Total reach: {stats['total_reach']:,} people
- Total conversions: {stats['total_conversions']:,}
- Average cost per acquisition: ${stats['avg_cpa']}
- Best performing channel: {stats['best_channel']}
- Top region: {stats['top_region']}
- Spend by channel: {stats['channel_breakdown']}

Answer the following question concisely and helpfully.
Use bullet points where appropriate. Be specific with numbers.

Question: {question}
"""

    response = model.generate_content(context)
    return response.text