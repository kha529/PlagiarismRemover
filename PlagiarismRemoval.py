import os

def load_library():
    library = Dint
    with open("Books.txt", "r") as file:
        for line in file:
            book_title, book_copies = line.strip().split(',')
            library[book_title] = int(book_copies)
    return library bo

def save_library(library):
    with open("Books.txt", "w") as file:
        for book_title, book_copies in library.items():
            file.write(f"{book_title},{book_copies}\n")

def load_clients():
    clients = {}
    with open("Customers.txt", "r") as file:
        for line in file:
            client_id, client_name = line.strip().split(',')
            clients[int(client_id)] = client_name
    return clients

def save_clients(clients):
    with open("Customers.txt", "w") as file:
        for client_id, client_name in clients.items():
            file.write(f"{client_id},{client_name}\n")

def load_transactions():
    transactions = []
    with open("Circulations.txt", "r") as file:
        for line in file:
            book_title, client_id, transaction_type = line.strip().split(',')
            transactions.append((book_title, int(client_id), transaction_type))
    return transactions

def save_transaction(book_title, client_id, transaction_type):
    with open("Circulations.txt", "a") as file:
        file.write(f"{book_title},{client_id},{transaction_type}\n")

def add_new_book(library):
    book_title = input("Enter the book's title: ")
    if book_title in library:
        print("Error: The book is already in the system.")
        return
    book_copies = int(input("Enter the number of copies: "))
    library[book_title] = book_copies
    save_library(library)
    print("The book has been added to the system.")

def add_new_client(clients):
    client_id = int(input("Enter the client’s number: "))
    if client_id in clients:
        print("Error: The number is already used.")
        return
    client_name = input("Enter the client's name: ")
    clients[client_id] = client_name
    save_clients(clients)
    print("The client has been added to the system.")

def borrow_book(library, clients, transactions):
    book_title = input("Enter the book's title: ")
    if book_title not in library:
        print("Error: The book is not in the system.")
        return
    client_id = int(input("Enter the client number: "))
    if client_id not in clients:
        print("Error: Client number not found.")
        return

    borrowed_count = sum(1 for title, cid, action in transactions if title == book_title and action == 'b')
    returned_count = sum(1 for title, cid, action in transactions if title == book_title and action == 'r')
    current_borrowed = borrowed_count - returned_count

    if current_borrowed < library[book_title]:
        print("The book is checked out.")
        save_transaction(book_title, client_id, 'b')
    else:
        print("No available copy.")

def return_book(library, clients, transactions):
    book_title = input("Enter the book's title: ")
    if book_title not in library:
        print("Error: The book is not in the system.")
