from input_handler import get_user_query, get_date_filter
from api_client import fetch_articles
from cleaner import clean_articles
from exporter import save_to_csv

def main():
    query = get_user_query()
    start,end = get_date_filter()

    raw_df = fetch_articles(query,start,end)

    if raw_df.empty:
        print("No articles found or API failed")
        return
    
    clean_df = clean_articles(raw_df)
    save_to_csv(clean_df,query)

if __name__ == "__main__":
    main()


