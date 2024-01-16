import psycopg2


class Model:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname='vacancies',
            user='postgres',
            password='1111',
            host='localhost',
            port=3000
        )

    def add_vacancy(self, title, description, create_date, author_id, executor_id):
        c = self.conn.cursor()
        c.execute('INSERT INTO vacancies (title, description, create_date, author_id, executor_id) VALUES (%s, %s, %s, %s, %s)', (title, description, create_date, author_id, executor_id))
        self.conn.commit()

    def add_author(self, name, phone_number, website):
        c = self.conn.cursor()
        c.execute('INSERT INTO authors (name, phone_number, website) VALUES (%s, %s, %s)', (name, phone_number, website))
        self.conn.commit()

    def add_executor(self, name, phone_number, rating):
        c = self.conn.cursor()
        c.execute('INSERT INTO executors (name, phone_number, rating) VALUES (%s, %s, %s)', (name, phone_number, rating))
        self.conn.commit()

    def get_all_vacancies(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM vacancies')
        return c.fetchall()

    def get_all_authors(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM authors')
        return c.fetchall()

    def get_all_executors(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM executors')
        return c.fetchall()

    def update_vacancy(self, title, description, create_date, author_id, executor_id, id):
        c = self.conn.cursor()
        c.execute('UPDATE vacancies SET title=%s, description=%s, create_date=%s, author_id=%s, executor_id=%s WHERE vacancy_id=%s', (title, description, create_date, author_id, executor_id, id))
        self.conn.commit()

    def update_author(self, name, phone_number, website, id):
        c = self.conn.cursor()
        c.execute('UPDATE authors SET name=%s, phone_number=%s, website=%s WHERE author_id=%s', (name, phone_number, website, id))
        self.conn.commit()

    def update_executor(self, name, phone_number, rating, id):
        c = self.conn.cursor()
        c.execute('UPDATE executors SET name=%s, phone_number=%s, rating=%s WHERE executor_id=%s', (name, phone_number, rating, id))
        self.conn.commit()

    def delete_vacancy(self, vacancy_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM vacancies WHERE vacancy_id=%s', (vacancy_id,))
        self.conn.commit()

    def delete_author(self, author_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM authors WHERE author_id=%s', (author_id,))
        self.conn.commit()

    def delete_executor(self, executor_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM executors WHERE executor_id=%s', (executor_id,))
        self.conn.commit()

    def get_top_freelancers(self):
         c = self.conn.cursor()
         c.execute('SELECT "name" AS executor_name, rating FROM executors ORDER BY rating DESC LIMIT 5;')
         return c.fetchall()

    def get_authors_vacancies(self):
        c = self.conn.cursor()
        c.execute(
            "SELECT a.name AS author_name, COUNT(*) AS vacancy_count FROM authors a JOIN vacancies v ON a.author_id = v.author_id WHERE v.create_date >= CURRENT_DATE - INTERVAL '1 month' GROUP BY a.name;")
        return c.fetchall()

    def get_joint_vacancies(self):
        c = self.conn.cursor()
        c.execute(
            "SELECT a.name AS author_name, e.name AS executor_name, v.title AS vacancy_title FROM authors a JOIN vacancies v ON a.author_id = v.author_id JOIN executors e ON v.executor_id = e.executor_id;")
        return c.fetchall()

    def add_random_fields(self, number):
        c = self.conn.cursor()
        c.execute('''
        INSERT INTO vacancies (title, description, create_date, author_id, executor_id)
        SELECT chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int), 
        chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int),
        current_date - interval '1 day' * trunc(random() * 365)::int,
        trunc(random() * 4 + 1)::int,
        trunc(random() * 4 + 1)::int
        FROM generate_series(1, %s);
    ''',(number,))
        self.conn.commit()


