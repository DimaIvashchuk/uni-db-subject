import time
from model import Model
from view import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        while True:
            choice = self.view.show_menu()

            if choice == '5':
                break
            elif choice in ['1', '2', '3', '4']:
                self.process_menu_choice(choice)
            else:
                self.view.show_message("Wrong choice. Try again.")

    def process_menu_choice(self, choice):
        while True:
            table = self.view.show_tables()

            if choice == '1':
                self.process_add_option(table)
            elif choice == '2':
                self.process_view_option(table)
            elif choice == '3':
                self.process_update_option(table)
            elif choice == '4':
                self.process_delete_option(table)

    def process_add_option(self, table):
        if table == '1':
            self.view.show_message("\nAdding vacancy:")
            self.add_vacancy()
        elif table == '2':
            self.view.show_message("\nAdding author:")
            self.add_author()
        elif table == '3':
            self.view.show_message("\nAdding executor:")
            self.add_executor()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_view_option(self, table):
        if table == '1':
            self.view_vacancies()
        elif table == '2':
            self.view_authors()
        elif table == '3':
            self.view_executors()
        elif table == '4':
            self.view.show_menu()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_update_option(self, table):
        if table == '1':
            self.view.show_message("\nUpdating vacancy:")
            self.update_vacancy()
        elif table == '2':
            self.view.show_message("\nUpdating author:")
            self.update_author()
        elif table == '3':
            self.view.show_message("\nUpdating executor:")
            self.update_executor()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_delete_option(self, table):
        if table == '1':
            self.view.show_message("\nDeleting vacancy:")
            self.delete_vacancy()
        elif table == '2':
            self.view.show_message("\nDeleting author:")
            self.delete_author()
        elif table == '3':
            self.view.show_message("\nDeleting executor:")
            self.delete_executor()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def add_vacancy(self):
        try:
            title, description, create_date, author_id, executor_id = self.view.get_vacancy_input()
            self.model.insert_vacancy(title, description, create_date, author_id, executor_id)
            self.view.show_message("Vacancy added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_author(self):
        try:
            name, phone_number, website = self.view.get_author_input()
            self.model.insert_author(name, phone_number, website)
            self.view.show_message("Author added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_executor(self):
        try:
            name, phone_number, rating = self.view.get_executor_input()
            self.model.insert_executor(name, phone_number, rating)
            self.view.show_message("Executor added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def view_vacancies(self):
        try:
            vacancies = self.model.show_vacancies()
            self.view.show_vacancies(vacancies)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def view_authors(self):
        try:
            authors = self.model.show_authors()
            self.view.show_authors(authors)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def view_executors(self):
        try:
            executors = self.model.show_executors()
            self.view.show_executors(executors)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_vacancy(self):
        try:
            vacancy_id = self.view.get_id()
            title, description, create_date, author_id, executor_id = self.view.get_vacancy_input()
            self.model.update_vacancy(title, description, create_date, author_id, executor_id, vacancy_id)
            self.view.show_message("Vacancy updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_author(self):
        try:
            author_id = self.view.get_id()
            name, phone_number, website = self.view.get_author_input()
            self.model.update_author(name, phone_number, website, author_id)
            self.view.show_message("Author updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_executor(self):
        try:
            executor_id = self.view.get_id()
            name, phone_number, rating = self.view.get_executor_input()
            self.model.update_executor(name, phone_number, rating, executor_id)
            self.view.show_message("Executor updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_vacancy(self):
        try:
            vacancy_id = self.view.get_id()
            self.model.delete_vacancy(vacancy_id)
            self.view.show_message("Vacancy deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_author(self):
        try:
            author_id = self.view.get_id()
            self.model.delete_author(author_id)
            self.view.show_message("Author deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_executor(self):
        try:
            executor_id = self.view.get_id()
            self.model.delete_executor(executor_id)
            self.view.show_message("Executor deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")