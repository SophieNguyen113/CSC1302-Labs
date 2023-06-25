# Prolog
# Author:  Sophie Nguyen
# Email:  nnguyen177@student.gsu.edu
# Section: 034

# Below is Python code for input/output
import sys

# For getting input from input.txt file
sys.stdin = open('Encyclopedia/input.txt', 'r')

# Printing the Output to output.txt file
sys.stdout = open('Encyclopedia/output.txt', 'w')

class Book:
    def __init__(self, title, author, publisher, publication_date):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publication_date = publication_date
   
    def print_info(self):
        print('Book Information:')
        print(f'   Book Title: {self.title}')
        print(f'   Author: {self.author}')
        print(f'   Publisher: {self.publisher}')
        print(f'   Publication Date: {self.publication_date}')

class Encyclopedia(Book):
    def __init__(self, title, author, publisher, publication_date, edition, num_volumes):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publication_date = publication_date
        self.edition = edition
        self.num_volumes = num_volumes
   
    def print_info(self):
        print('Book Information:')
        print(f'   Book Title: {self.title}')
        print(f'   Author: {self.author}')
        print(f'   Publisher: {self.publisher}')
        print(f'   Publication Date: {self.publication_date}')
        print(f'   Edition: {self.edition}')
        print(f'   Number of Pages: {self.num_volumes}')
    

if __name__ == "__main__":
    title = input()
    author = input()
    publisher = input()
    publication_date = input()
    
    e_title = input()
    e_author = input()
    e_publisher = input()
    e_publication_date = input()
    edition = input()
    num_pages = int(input())
    
    my_book = Book(title, author, publisher, publication_date)
    my_book.print_info()
    
    my_encyclopedia = Encyclopedia(e_title, e_author, e_publisher, e_publication_date, edition, num_pages)
    my_encyclopedia.print_info()