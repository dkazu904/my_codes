import sqlite3

db_name = 'baseball.db'

print("Welcome to my database program!")
print("Main menu: ")

def connect_to_db():
    # connect to the database
    db_conn = sqlite3.connect(db_name)  # connect is a function
    db_cursor = db_conn.cursor()  # cursor is a method
    return db_conn, db_cursor


def create_table(db_cursor):
    sql = "CREATE TABLE baseball (team TEXT, location TEXT, player TEXT, salary REAL, height REAL, weight REAL)"
    db_cursor.execute(sql)
    print("Table created.")


def drop_table(db_cursor):
    sql = "DROP TABLE IF EXISTS baseball"
    db_cursor.execute(sql)
    print("Table dropped.")


def insert_row(db_cursor):
    sql = "INSERT INTO baseball (team, location, player, salary, height, weight) VALUES (?, ?, ?, ?, ?, ?)"

    t = input("Enter the team: ")
    l = input("Enter the location: ")
    p = input("Enter the player: ")
    b = float(input("Enter the salary: "))
    h = float(input("Enter the height: "))
    w = float(input("Enter the weight: "))

    # create the tuple object that holds the data
    tuple_of_values = (t, l, p, b, h, w)

    db_cursor.execute(sql, tuple_of_values)
    print("Row inserted")


def select_all(db_cursor):
    sql = "SELECT * from baseball"
    result_set = db_cursor.execute(sql)
    row = None
    for row in result_set:
        print(row)
    if row is None:
        print("No rows found")


def ask_for_float(prompt):
    while True:
        try:
            user_input = float(input(prompt))
            break
        except ValueError:
            print("Enter a valid float. Try again. ")
    return user_input


def update_row(db_cursor):
    team = input("Enter the team for the baseball you wish to update: ")
    salary = float(input("Enter the new salary: "))
    height = float(input("Enter the new height: "))
    weight = float(input("Enter the new weight: "))
    sql = "Update baseball set salary = ?, height = ?, weight = ? where team = ?"

    tuple_of_values = (salary, height, weight, team)
    db_cursor.execute(sql, tuple_of_values)
    print("Row updated.")


def delete_row(db_cursor):
    team = input("Enter the team for the baseball you wish to delete: ")
    sql = " delete from baseball where team = ?"
    tuple_of_value = (team,)
    db_cursor.execute(sql, tuple_of_value)
    print("Row deleted. ")


def select_row(db_cursor):
    team = input("Enter the team you wish to select: ")
    sql = "select * from  baseball where team = ?"
    tuple_of_value = (team,)
    result_set = db_cursor.execute(sql, tuple_of_value)
    for row in result_set:
        print(row)


def display_menu(db_conn, db_cursor):
    while True:
        print("\nEnter S to get started & create/refresh the table")
        print("Enter C to create a new roll")
        print("Enter R to retrieve data")
        print("Enter U to update data")
        print("Enter D to delete data")
        print("Enter Q to quit the program")
        choice = input("Enter your choice: ").upper()
        if choice == 'S':
            drop_table(db_cursor)
            create_table(db_cursor)
        elif choice == 'C':
            insert_row(db_cursor)
        elif choice == 'R':
            select_row(db_cursor)
        elif choice == 'U':
            update_row(db_cursor)
        elif choice == 'D':
            delete_row(db_cursor)
        elif choice == 'Q':
            break
        else:
            print("invalid option. Please try again. ")
            continue

        db_conn.commit()
        select_all(db_cursor)


def main():
    db_conn, db_cursor = connect_to_db()
    display_menu(db_conn, db_cursor)
    db_conn.close()  # do this once


# call main
main()
