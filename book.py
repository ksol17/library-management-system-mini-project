class Book:
    def __init__(self, title, author, genre, pub_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__pub_date = pub_date
        self.__available = True  # Default availability status

    # Getters
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_genre(self):
        return self.__genre

    def get_pub_date(self):
        return self.__pub_date

    def is_available(self):
        return self.__available

    # Setters
    def set_availability(self, availability):
        self.__available = availability

    def display_book_info(self):
        availability_status = "Available" if self.__available else "Not Available"
        return (f"Title: {self.__title}, Author: {self.__author}, Genre: {self.__genre}, "
                f"Publication Date: {self.__pub_date}, Status: {availability_status}")
