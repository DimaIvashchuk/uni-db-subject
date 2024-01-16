from db import Base, Session, engine
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, Date, CheckConstraint

s = Session()


class Vacancy(Base):
    __tablename__ = 'vacancies'
    vacancy_id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    create_date = Column(Date)

    author_id = Column(Integer, ForeignKey('authors.author_id'))
    executor_id = Column(Integer, ForeignKey('executors.executor_id'))

    def __init__(self, title, description, create_date, author_id, executor_id):
        self.title = title
        self.description = description
        self.create_date = create_date
        self.author_id = author_id
        self.executor_id = executor_id

    def __repr__(self):
        return f"<Vacancies(vacancy_id={self.vacancy_id}, title={self.title}, description={self.description}, create_date={self.create_date}, author_id={self.author_id}, executor_id={self.executor_id})>"


class Author(Base):
    __tablename__ = 'authors'
    author_id = Column(Integer, primary_key=True)
    name = Column(String)
    phone_number = Column(String)
    website = Column(String)

    vacancy = relationship("Vacancy")

    def __init__(self, name, phone_number, website):
        self.name = name
        self.phone_number = phone_number
        self.website = website

    def __repr__(self):
        return f"<Authors(author_id={self.author_id}, name={self.name}, phone_number={self.phone_number}, website={self.website})>"


class Executor(Base):
    __tablename__ = 'executors'
    executor_id = Column(Integer, primary_key=True)
    name = Column(String)
    phone_number = Column(String)
    rating = Column(Numeric, CheckConstraint('rating >= 1 AND rating <= 5'))

    vacancy = relationship("Vacancy")

    def __init__(self, name, phone_number, rating):
        self.name = name
        self.phone_number = phone_number
        self.rating = rating

    def __repr__(self):
        return f"<Executors(author_id={self.author_id}, name={self.name}, phone_number={self.phone_number}, rating={self.rating})>"


class Model:
    def __init__(self):
        self.session = Session()
        self.connection = engine.connect()

    def insert_vacancy(self, title: str, description: str, create_date: Date, author_id: int, executor_id: int) -> None:
        vacancy = Vacancy(title=title, description=description, create_date=create_date, author_id=author_id, executor_id=executor_id)
        s.add(vacancy)
        s.commit()

    def insert_author(self, name: str, phone_number: str, website: str) -> None:
        author = Author(name=name, phone_number=phone_number, website=website)
        s.add(author)
        s.commit()

    def insert_executor(self, name: str, phone_number: str, rating: float) -> None:
        executor = Executor(name=name, phone_number=phone_number, rating=rating)
        s.add(executor)
        s.commit()

    def show_vacancies(self):
        return s.query(Vacancy.vacancy_id, Vacancy.title, Vacancy.description, Vacancy.create_date, Vacancy.author_id, Vacancy.executor_id).all()

    def show_authors(self):
        return s.query(Author.author_id, Author.name, Author.phone_number, Author.website).all()

    def show_executors(self):
        return s.query(Executor.executor_id, Executor.name, Executor.phone_number, Executor.rating).all()

    def update_vacancy(self, title: str, description: str, create_date: Date, author_id: int, executor_id: int, vacancy_id: int) -> None:
        s.query(Vacancy).filter_by(vacancy_id=vacancy_id).update({Vacancy.title: title, Vacancy.description: description, Vacancy.create_date: create_date, Vacancy.author_id: author_id, Vacancy.executor_id: executor_id})
        s.commit()

    def update_author(self, name: str, phone_number: str, website: str, author_id: int) -> None:
        s.query(Author).filter_by(author_id=author_id).update({Author.name: name, Author.phone_number: phone_number, Author.website: website})
        s.commit()

    def update_executor(self, name: str, phone_number: str, rating: float, executor_id: int) -> None:
        s.query(Executor).filter_by(executor_id=executor_id).update({Executor.name: name, Executor.phone_number: phone_number, Executor.rating: rating})
        s.commit()

    def delete_vacancy(self, vacancy_id) -> None:
        vacancy = s.query(Vacancy).filter_by(vacancy_id=vacancy_id).one()
        s.delete(vacancy)
        s.commit()

    def delete_author(self, author_id) -> None:
        author = s.query(Author).filter_by(author_id=author_id).one()
        s.delete(author)
        s.commit()

    def delete_executor(self, executor_id) -> None:
        executor = s.query(Executor).filter_by(executor_id=executor_id).one()
        s.delete(executor)
        s.commit()