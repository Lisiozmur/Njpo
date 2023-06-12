import sqlite3

def create_table():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS records (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, email TEXT)''')

    conn.commit()
    conn.close()

def add_row():
    name = input("Podaj imię: ")
    age = int(input("Podaj wiek: "))
    email = input("Podaj email: ")

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("INSERT INTO records (name, age, email) VALUES (?, ?, ?)", (name, age, email))

    conn.commit()
    conn.close()

    print("Wiersz został dodany.")

def delete_row():
    row_id = int(input("Podaj ID wiersza do usunięcia: "))

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("DELETE FROM records WHERE id=?", (row_id,))

    conn.commit()
    conn.close()

    print("Wiersz został usunięty.")

def update_row():
    row_id = int(input("Podaj ID wiersza do modyfikacji: "))
    field = input("Podaj pole do modyfikacji (name, age, email): ")
    new_value = input("Podaj nową wartość: ")

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute(f"UPDATE records SET {field}=? WHERE id=?", (new_value, row_id))

    conn.commit()
    conn.close()

    print("Pole wiersza zostało zaktualizowane.")

def display_rows():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("SELECT * FROM records")
    rows = c.fetchall()

    if len(rows) == 0:
        print("Baza danych jest pusta.")
    else:
        for row in rows:
            print(row)

    conn.close()

def display_menu():
    print("======== MENU ========")
    print("1. Dodaj wiersz")
    print("2. Usuń wiersz")
    print("3. Zmień pole wiersza")
    print("4. Wyświetl wiersze")
    print("0. Zakończ program")
    print("======================")

def main():
    create_table()

    while True:
        display_menu()
        choice = input("Wybierz opcję: ")

        if choice == "1":
            add_row()
        elif choice == "2":
            delete_row()
        elif choice == "3":
            update_row()
        elif choice == "4":
            display_rows()
        elif choice == "0":
            print("Koniec programu.")
            break
        else:
            print("BŁĄD!!!")

