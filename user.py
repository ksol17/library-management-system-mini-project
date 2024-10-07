class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    # Getters
    def get_name(self):
        return self.__name

    def get_library_id(self):
        return self.__library_id

    def get_borrowed_books(self):
        return self.__borrowed_books

    # Borrow and return books
    def borrow_book(self, book_title):
        self.__borrowed_books.append(book_title)

    def return_book(self, book_title):
        if book_title in self.__borrowed_books:
            self.__borrowed_books.remove(book_title)

    def display_user_info(self):
        borrowed_books_str = ", ".join(self.__borrowed_books) if self.__borrowed_books else "No books borrowed"
        return f"User: {self.__name}, Library ID: {self.__library_id}, Borrowed Books: {borrowed_books_str}"
