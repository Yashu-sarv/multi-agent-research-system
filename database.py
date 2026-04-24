import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

from datetime import datetime, timedelta

def get_cached_research(topic):
    # 30 din pehle ki date calculate karein
    one_month_ago = (datetime.now() - timedelta(days=30)).isoformat()

    # Database mein topic dhundo, lekin sirf tab agar wo 30 din ke andar ka ho
    response = supabase.table("research_cache")\
        .select("*")\
        .eq("topic", topic.lower())\
        .gt("created_at", one_month_ago)\
        .execute()
    
    return response.data[0] if response.data else None

def save_research(topic, search_results, scraped_content, final_report):
    # Naya data save ya update karo (with fresh timestamp)
    data = {
        "topic": topic.lower(),
        "search_results": search_results,
        "scraped_content": scraped_content,
        "final_report": final_report,
        "created_at": datetime.now().isoformat()
    }
    supabase.table("research_cache").upsert(data).execute()
