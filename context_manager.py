import psycopg2

connection = psycopg2.connect(
    host='localhost',
    database='Azamat',
    user='postgres',
    password='123',
    port=5432,
)


class Person:
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.connection = None

    def __enter__(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port
            )

            return self.connection
        except psycopg2.DatabaseError as e:
            print(e)

    def __exit__(self, exc_type, exc_value, exc_tb):
        if self.connection and not self.connection.closed:
            self.connection.close()

    @staticmethod
    def get_one_person(connection, person_id):
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM persons WHERE id = %s", (person_id,))
                result = cursor.fetchone()
                return result
        except Exception as e:
            print(f"Xato: {e}")

    @staticmethod
    def get_all_person(connection):
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM persons")
                return cursor.fetchall()
        except Exception as e:
            print(f"Xato: {e}")
            return []


#
with Person('localhost', 'Azamat', 'postgres', '123', 5432) as conn:
    one_person = Person.get_one_person(conn, 1)
    all_persons = Person.get_all_person(conn)
    print(one_person)
    print(all_persons)
