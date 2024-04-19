"""Script para inserir dados no banco"""
import psycopg2
import pandas as pd


def main():
    """Insere no banco de dados os dados da netflix"""
    show_info = pd.read_csv('datasets/show_info.csv')
    show_info = show_info[['show_id', 'type', 'title', 'date_added', 'duration', 'listed_in', 'description']]
    show_info = show_info.query('date_added.notna()')
    show_info['date_added'] = show_info['date_added'].astype(str)

    director_shows = pd.read_csv('datasets/director_shows.csv')
    director_shows = director_shows[['show_id', 'director', 'cast', 'country', 'release_year', 'rating']]
    director_shows = director_shows.query('@director_shows.notna()')
    # Connect to your PostgreSQL database
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="alura",
        user="postgres",
        password="postgres"
    )



    # Convert DataFrame to a list of tuples

    # Create a cursor object
    cur = conn.cursor()

    # Define your insert statement
    insert_query = """INSERT INTO show_info 
    (show_id, show_type, title, date_added, duration, listed_in, description) 
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    data_values = [tuple(x) for x in show_info.to_numpy()]

    # Execute the insert statement with executemany
    cur.executemany(insert_query, data_values)

    insert_query = """INSERT INTO director_shows
    (show_id, director, country, cast_data, release_year, rating) 
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    director_shows = director_shows.dropna()
    director_shows['release_year'] = director_shows['release_year'].astype(int)
    data_values = [tuple(x) for x in director_shows.to_numpy()]

    for data in data_values:
        cur.execute(insert_query, data)

    # Commit the transaction
    conn.commit()

    # Close the cursor and connection
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
