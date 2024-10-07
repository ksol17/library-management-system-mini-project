class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    # Getters
    def get_name(self):
        return self.__name

    def get_biography(self):
        return self.__biography

    def display_author_info(self):
        return f"Author: {self.__name}, Biography: {self.__biography}"
