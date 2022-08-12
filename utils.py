import sqlite3


def get_movie_by_title(name):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()  # Запускаем курсор, с помощью которого мы будем получать данные из БД
        sqlite_query = """
                            SELECT title, country, release_year, listed_in, description
                            FROM netflix
                            WHERE title=? AND "type" = 'Movie'
                            ORDER BY release_year DESC
                            """
        cursor.execute(sqlite_query, (name,))  # Выполняем запрос с помощью курсора
        data = cursor.fetchone()
        sql_dict = {"title": data[0],
                    "country": data[1],
                    "release_year": data[2],
                    "genre": data[3],
                    "description": data[4]}
        return sql_dict


def get_movie_by_years(first_year, second_year):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()  # Запускаем курсор, с помощью которого мы будем получать данные из БД
        sqlite_query = """
                            SELECT title, release_year
                            FROM netflix
                            WHERE release_year BETWEEN ? AND ? AND type = 'Movie'
                            LIMIT 100
                            """
        cursor.execute(sqlite_query, (first_year, second_year))  # Выполняем запрос с помощью курсора
        data = cursor.fetchall()
        sql_dict = []
        for row in data:
            row = {"title": row[0],
                   "release_year": row[1]}
            sql_dict.append(row)

        return sql_dict


def get_movie_by_rating_child():
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()  # Запускаем курсор, с помощью которого мы будем получать данные из БД
        sqlite_query = """
                            SELECT title, rating, description
                            FROM netflix
                            WHERE rating = "G"
                            LIMIT 100
                            """
        cursor.execute(sqlite_query)  # Выполняем запрос с помощью курсора
        data = cursor.fetchall()
        sql_dict = []
        for row in data:
            row = {"title": row[0],
                   "rating": row[1],
                   "description": row[2]}
            sql_dict.append(row)

        return sql_dict


def get_movie_by_rating_family():
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()  # Запускаем курсор, с помощью которого мы будем получать данные из БД
        sqlite_query = """
                            SELECT title, rating, description
                            FROM netflix
                            WHERE rating IN ("G", "PG", "PG-13")
                            LIMIT 100
                                """
        cursor.execute(sqlite_query)  # Выполняем запрос с помощью курсора
        data = cursor.fetchall()
        sql_dict = []
        for row in data:
            row = {"title": row[0],
                   "rating": row[1],
                   "description": row[2]}
            sql_dict.append(row)

        return sql_dict


def get_movie_by_rating_adult():
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()  # Запускаем курсор, с помощью которого мы будем получать данные из БД
        sqlite_query = """
                            SELECT title, rating, description
                            FROM netflix
                            WHERE rating IN ("R", "NC-17")
                            LIMIT 100
                                """
        cursor.execute(sqlite_query)  # Выполняем запрос с помощью курсора
        data = cursor.fetchall()
        sql_dict = []
        for row in data:
            row = {"title": row[0],
                   "rating": row[1],
                   "description": row[2]}
            sql_dict.append(row)

        return sql_dict


def get_movie_genre(genre):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()  # Запускаем курсор, с помощью которого мы будем получать данные из БД
        sqlite_query = """
                            SELECT title, description
                            FROM netflix
                            WHERE listed_in = ?
                            ORDER BY release_year DESC
                            LIMIT 10
                            """
        cursor.execute(sqlite_query, (genre,))  # Выполняем запрос с помощью курсора
        data = cursor.fetchall()
        sql_dict = []
        for row in data:
            row = {"title": row[0],
                   "description": row[1]}
            sql_dict.append(row)

        return sql_dict


def get_movie_by_cast(cast_1, cast_2):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()  # Запускаем курсор, с помощью которого мы будем получать данные из БД
        sqlite_query = """
                            SELECT "cast"
                            FROM netflix
                            GROUP BY "cast"
                            HAVING "cast" LIKE ? AND ?
                            """
        cursor.execute(sqlite_query, (cast_1, cast_2))  # Выполняем запрос с помощью курсора
        data = cursor.fetchall()

        return data


def get_movie_year_genre(type, release_year, genre):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()  # Запускаем курсор, с помощью которого мы будем получать данные из БД
        sqlite_query = """
                            SELECT title, description
                            FROM netflix
                            WHERE "type" = ? AND release_year = ? AND listed_in = ? AND description != ''
                            """
        cursor.execute(sqlite_query, (type, release_year, genre))  # Выполняем запрос с помощью курсора
        data = cursor.fetchall()
        sql_dict = []
        for row in data:
            row = {"title": row[0],
                   "description": row[1]}
            sql_dict.append(row)

        return sql_dict


