from ast import literal_eval as make_tuple

import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(
    host='localhost',
    database='hms',
    user='postgres',
    password='deepti123'
)

cursor = conn.cursor()
cursor.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
tables = [i[0] for i in cursor.fetchall()]


def get_pk(table):
    query = "select indexdef from pg_indexes where tablename = '%s';" % (table,)
    cursor.execute(query)
    rows = cursor.fetchall()
    pk = None
    if rows:
        row = rows[0][0].split()
        result = row[-1]
        pk = result[1:-1]

    return pk


def show_table():
    print("\n\nThese are the following tables available for you to see")
    count = 1
    for table in tables:
        print(count, ") ", table.capitalize())
        count += 1
    print()

    choice = input("Enter the name or number associated with the table to see the contents or type menu to go back: ")
    if choice == 'menu':
        menu()
    try:
        choices = int(choice)

        if choices > len(tables):
            print("You seem to have entered an incorrect table number please check from the list below and try again.")
            show_table()

        else:
            print("\n\n")
            print("You are now viewing the {name} table.".format(name=tables[choices - 1]))
            print("To see all data in table press 1 ")
            print("To check particular record in table press 2")

            inp = input("Enter choice : ")
            if inp == "1":
                print("Showing all records")

                query = sql.SQL("select * from {table};").format(
                    table=sql.Identifier(tables[choices - 1]))
                cursor.execute(query)
                result = cursor.fetchall()
                for r in result:
                    print(r)

            elif inp == '2':
                pkey = get_pk(tables[choices - 1])
                id = input("Please enter the id of the record : ")
                field = input("Please enter the field of the record : ")
                query = sql.SQL("select {field} from {table} where {pkey} = %s").format(
                    # field=sql.Identifier(field),
                    table=sql.Identifier(tables[choices - 1]),
                    pkey=sql.Identifier(pkey))
                cursor.execute(query, (field, id))

            else:
                print("Please enter the correct choice")
                print("Returning")
                show_table()

        menu()

    except ValueError:
        if choice not in tables:
            print("You seem to have entered an incorrect table name please check from the list below and try again.")
            show_table()
        else:
            print("\n\n")
            print("You are now viewing the {name} table.".format(name=choice))
            print("To see all data in table press 1 ")
            print("To check particular record in table press 2")

            inp = input("Enter choice : ")
            if inp == '1':
                query = sql.SQL("select * from {table};").format(
                    table=sql.Identifier(choice))
                cursor.execute(query)
                result = cursor.fetchall()
                for r in result:
                    print(r)

            elif inp == '2':
                id = input("Please enter the id of the record : ")
                print(id)

            else:
                print("Please enter the correct choice")
                print("Returning")

                show_table()


def add_to_table():
    print("\n\nWhich table would you want to insert data into")
    count = 1
    for table in tables:
        print(count, ") ", table.capitalize())
        count += 1
    print()

    choice = input("Enter the name or number associated with the table to see the contents or type menu to go back: ")
    if choice == 'menu':
        menu()

    try:
        choices = int(choice)

        if choices not in range(1, len(tables)):
            print("You seem to have entered an incorrect table number please"
                  " check from the list below and try again.")
            show_table()

        else:
            print("\n\n")
            print("You are now using the {name} table.".format(name=tables[choices - 1]))
            confirm = 'n'
            while confirm != 'y':
                tup = input("Input the values in tuple form : ")
                confirm = input("Is the input correct? (y/n) ")

            new_tup = make_tuple(tup)

            query = sql.SQL("insert into {table} values %s;").format(
                table=sql.Identifier(tables[choices - 1])

            )
            cursor.execute(query, (new_tup,))
            conn.commit()
            print("Record added successfully..")

            inp = input("Press any character to continue ")
            if inp:
                menu()

    except ValueError:
        if choice not in tables:
            print("You seem to have entered an incorrect table name please check from the list below and try again.")
            show_table()
        else:
            print("\n\n")
            print("You are now using the {name} table.".format(name=choice))
            confirm = 'n'
            while confirm != 'y':
                tup = input("Input the values in tuple form : ")
                confirm = input("Is the input correct? (y/n) ")

            new_tup = make_tuple(tup)

            query = sql.SQL("insert into {table} values %s;").format(
                table=sql.Identifier(choice)

            )
            cursor.execute(query, (new_tup,))
            conn.commit()
            print('\n\n')

            inp = input("Press any character to continue ")
            if inp:
                menu()

    except psycopg2.Error as e:
        print(e)
        print('Taking you back..')
        conn.rollback()
        add_to_table()


def update_table():
    print("\n\nWhich table would you want to update the records of")
    count = 1
    for table in tables:
        print(count, ") ", table.capitalize())
        count += 1
    print()

    choice = input("Enter the name or number associated with the table to see the contents or type menu to go back: ")
    if choice == 'menu':
        menu()

    try:
        choices = int(choice)
        if choices not in range(1, len(tables)):
            print("You seem to have entered an incorrect table number please"
                  " check from the list below and try again.")
            show_table()

        else:

            print("You are now using the {name} table.".format(name=tables[choices - 1]))

            pkey = get_pk(tables[choices - 1])
            if pkey is None:
                pkey = input("Enter attribute for where clause : ")
            field = input("Enter the field you want to update : ")
            id = int(input("Enter the id of the record you want to update :  "))
            value = input("Enter updated value : ")

            query = sql.SQL("update {table} set {field} = %s where {pkey} = %s").format(
                field=sql.Identifier(field),
                table=sql.Identifier(tables[choices - 1]),
                pkey=sql.Identifier(pkey))
            cursor.execute(query, (value, id))
            conn.commit()
            print("Record updated successfully")
            inp = input("Press any character to continue ")
            if inp:
                menu()

    except ValueError:
        if choice not in tables:
            print("You seem to have entered an incorrect table name please check from the list below and try again.")
            show_table()
        else:
            print("\n\n")
            print("You are now using the {name} table.".format(name=choice))
            pkey = get_pk(choice)
            if pkey is None:
                pkey = input("Enter attribute for where clause : ")
            field = input("Enter the field you want to update : ")
            id = int(input("Enter the id of the record you want to update :  "))
            value = input("Enter updated value : ")

            query = sql.SQL("update {table} set {field} = %s where {pkey} = %s").format(
                field=sql.Identifier(field),
                table=sql.Identifier(choice),
                pkey=sql.Identifier(pkey))
            cursor.execute(query, (value, id))
            conn.commit()
            print("Record updated successfully")
            inp = input("Press any character to continue ")
            if inp:
                menu()

    except psycopg2.Error as e:
        print(e)
        print('Taking you back..')
        conn.rollback()
        add_to_table()


def delete_from_table():
    print("\n\nWhich table would you want to delete the records from")
    count = 1
    for table in tables:
        print(count, ") ", table.capitalize())
        count += 1
    print()

    choice = input("Enter the name or number associated with the table to see the contents or type menu to go back: ")
    if choice == 'menu':
        menu()

    try:
        choices = int(choice)
        if choices not in range(1, len(tables)):
            print("You seem to have entered an incorrect table number please"
                  " check from the list below and try again.")
            show_table()

        else:

            print("You are now using the {name} table.".format(name=tables[choices - 1]))

            pkey = get_pk(tables[choices - 1])
            if pkey is None:
                pkey = input("Enter attribute for WHERE clause : ")
            id = int(input("Enter the id of the record you want to delete :  "))

            query = sql.SQL("delete from {table} where {pkey} = %s").format(
                table=sql.Identifier(tables[choices - 1]),
                pkey=sql.Identifier(pkey))
            cursor.execute(query, (id,))
            conn.commit()
            print("Record deleted successfully")
            inp = input("Press any character to continue ")
            if inp:
                menu()

    except ValueError:
        if choice not in tables:
            print("You seem to have entered an incorrect table name please check from the list below and try again.")
            show_table()
        else:
            print("\n\n")
            print("You are now using the {name} table.".format(name=choice))
            pkey = get_pk(choice)
            if pkey is None:
                pkey = input("Enter attribute for WHERE clause : ")
            id = int(input("Enter the id of the record you want to delete :  "))

            query = sql.SQL("delete from {table} where {pkey} = %s").format(
                table=sql.Identifier(choice),
                pkey=sql.Identifier(pkey))
            cursor.execute(query, (id,))
            conn.commit()
            print("Record deleted successfully")
            inp = input("Press any character to continue ")
            if inp:
                menu()

    except psycopg2.Error as e:
        print(e)
        print('Taking you back..')
        conn.rollback()


def menu():
    print("Welcome to the Hospital Database System")
    print('\n')
    print("To view contents to table press (1)")
    print("To add records to table press (2)")
    print("To update records of table press (3)")
    print("To delete records of table press (4)")
    print("Press any other key to exit")
    choice = input("Enter your choice : ")

    if choice == '1':
        show_table()

    elif choice == '2':
        add_to_table()

    elif choice == '3':
        update_table()

    elif choice == '4':
        delete_from_table()

    else:
        exit()

    # print("here")


menu()
