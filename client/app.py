import MySQLdb
import time
import sys

print("Hello, ATM is starting..")
time.sleep(2)

first = False

while True:

    if not first:
        print("Username:")
        user = raw_input().strip()
        print("Password:")
        passwd = raw_input().strip()
        my = MySQLdb.connect(
            user='admin',
            passwd='1234',
            host='database',
            db='tema',
            port=3306)
        cursor = my.cursor()
        cursor.execute("select * from users")
        res = cursor.fetchall()
        for x in res:
            if x[0] == user and x[1] == passwd:
                print("\nAccess granted\n")
                first = True
                break

        if not first:
            print("\nUser or passwd not found\n")
            continue

    print("\nWhat would you like?:")
    print("1. Take money - credit card")
    print("2. Deposit")
    print("3. Show my money")
    print("4. Exit\n")
    option = raw_input()

    if option == '1':
        print("Please enther the amount of money:")
        money = int(sys.stdin.readline())
        my = MySQLdb.connect(
            user='admin',
            passwd='1234',
            host='database',
            db='tema',
            port=3306)
        cursor = my.cursor()
        sql = """UPDATE users SET money = money - {0} WHERE user = \"{1}\"""".format(money, user)
        cursor.execute(sql)
        my.commit()
        print("\nDone: added {0} LEI to account\n").format(money)

    elif option == '2':
        print("Please enther the amount of money:")
        money = int(sys.stdin.readline())
        my = MySQLdb.connect(
            user='admin',
            passwd='1234',
            host='database',
            db='tema',
            port=3306)
        cursor = my.cursor()
        sql = """UPDATE users SET money = money + {0} WHERE user = \"{1}\"""".format(money, user)
        cursor.execute(sql)
        my.commit()
        print("\nDone: took {0} LEI to account\n").format(money)

    elif option == '3':
        my = MySQLdb.connect(
            user='admin',
            passwd='1234',
            host='database',
            db='tema',
            port=3306)
        cursor = my.cursor()
        cursor.execute("select * from users WHERE user = \"{0}\"".format(user))
        res = cursor.fetchall()
        print("\nSuma de bani este:")
        print(res[0][2])

    elif option == '4':
            print("Thanks for choosing our bank!")
            exit()
