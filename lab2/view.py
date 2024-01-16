from datetime import datetime

class View:

    def show_menu(self):
        self.show_message("\nМеню:")
        self.show_message("1. Додати рядок")
        self.show_message("2. Показати таблицю")
        self.show_message("3. Редагувати рядок")
        self.show_message("4. Видалити рядок")
        self.show_message("5. Вихід")
        choice = input("Виберіть пункт: ")
        return choice

    def show_tables(self):
        self.show_message("\nТаблиці:")
        self.show_message("1. Vacancies (вакансії)")
        self.show_message("2. Authors (автори)")
        self.show_message("3. Executors (фрілансери)")
        self.show_message("4. Повернутися до меню")
        table = input("Оберіть потрібну таблицю: ")
        return table

    def show_vacancies(self, vacancies):
        print("\nVacancies:")
        for vacancy in vacancies:
            print(f"ID: {vacancy[0]}, Title: {vacancy[1]}, Description: {vacancy[2]}, Create date: {vacancy[3]}, Author ID: {vacancy[4]}, Executor ID: {vacancy[5]}")

    def show_authors(self, authors):
        print("\nAuthors:")
        for author in authors:
            print(f"ID: {author[0]}, Name: {author[1]}, Phone number: {author[2]}, Website: {author[3]}")

    def show_executors(self, executors):
        print("\nExecutors:")
        for executor in executors:
            print(f"ID: {executor[0]}, Name: {executor[1]}, Phone number: {executor[2]}, Rating: {executor[3]}")

    def get_vacancy_input(self):
        while True:
            try:
                title = input("Enter vacancy title: ")
                if title.strip():
                    break
                else:
                    print("Title cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                description = input("Enter vacancy description: ")
                if description.strip():
                    break
                else:
                    print("Description cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                date = input("Enter creation date (YYYY-MM-DD): ")
                create_date = datetime.strptime(date, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        while True:
            try:
                author_id = int(input("Enter vacancy author ID: "))
                break
            except ValueError:
                print("Author ID must be a number.")
        while True:
            try:
                executor_id = int(input("Enter vacancy executor ID: "))
                break
            except ValueError:
                print("Executor ID must be a number.")
        return title, description, create_date, author_id, executor_id

    def get_author_input(self):
        while True:
            try:
                name = input("Enter author name: ")
                if name.strip():
                    break
                else:
                    print("Name cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                phone_number = input("Enter author phone number: ")
                if phone_number.strip():
                    break
                else:
                    print("Phone number cannot be empty.")
            except ValueError:
                print("It must be a string.")

        while True:
            try:
                website = input("Enter author website: ")
                if website.strip():
                    break
                else:
                    print("Website cannot be empty.")
            except ValueError:
                print("It must be a string.")
        return name, phone_number, website

    def get_executor_input(self):
        while True:
            try:
                name = input("Enter executor name: ")
                if name.strip():
                    break
                else:
                    print("Name cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                phone_number = input("Enter executor phone number: ")
                if phone_number.strip():
                    break
                else:
                    print("Phone number cannot be empty.")
            except ValueError:
                print("It must be a string.")

        while True:
            try:
                rating = input("Enter executor rating: ")
                if rating.strip():
                    break
                else:
                    print("Rating cannot be empty.")
            except ValueError:
                print("It must be a string.")
        return name, phone_number, rating

    def get_id(self):
        while True:
            try:
                id = int(input("Enter ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    def show_message(self, message):
        print(message)