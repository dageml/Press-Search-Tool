import time


def get_user_query():
    print("Welcome to Press Search Tool by Dagem Legesse.")
    time.sleep(4)
    print("Option A: Topic (e.g., Medicaid) or Option B: Location (e.g., New York City)")
    time.sleep(3)
    query = input("Please enter your keyword or location: ").strip().lower()
    return query

def get_date_filter():
    answer = input("Do you want to filter by date? (Y/N): ").strip().lower()
    if answer == 'y':
        start = input("Start Date (YYYY-MM-DD): ")
        end = input("End date (YYYY-MM-DD): ")
        return start, end
    return None, None
