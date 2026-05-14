import sqlite3
import requests


conn = sqlite3.connect('EldenRingLocationsdb.sql')


cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS locations (
        id TEXT PRIMARY KEY,
        name TEXT,
        region TEXT
    )
''')


def get_and_save_locations():
    base_url = 'https://eldenring.fanapis.com/api/locations'
    limit = 5  
    page = 1   

    print("Fetching data from API")

    while True:
        params = {'limit': limit, 'page': page}
        response = requests.get(base_url, params=params, timeout=10)
        if response.status_code != 200:
            print("Failed to fetch data from API.")
            break

        data = response.json()
        locations = data.get('data', [])

        if not locations:
    
            break

        
        for loc in locations:
            cursor.execute('''
                INSERT OR REPLACE INTO locations (id, name, region)
                VALUES (?, ?, ?)
            ''', (loc.get('id'), loc.get('name'), loc.get('region')))

        conn.commit()
        print(f"Page {page}: Saved {len(locations)} locations.")
        
        if len(locations) < limit:
            
            break

        page += 1


def display_locations(limit=5):
    cursor.execute('SELECT * FROM locations LIMIT ?', (limit,))
    rows = cursor.fetchall()
    print(f"\n--- Displaying first {limit} locations ---")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Region: {row[2]}")


if __name__ == '__main__':
    get_and_save_locations()
    display_locations()


    conn.close()
    print("\nDatabase connection closed.")