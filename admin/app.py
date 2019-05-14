import MySQLdb
import time
import sys

print("Database init..")
time.sleep(2)

while True:
    print("\nSelect your option:")
    print("1. Add Account")
    print("2. Remove account")
    print("3. See accounts")
    print("4. Exit")
    option = raw_input()
    if option.strip() == '1':
        print("Add Account Selected")
        print("User Pass Money")
        line = str(sys.stdin.readline())
        line1 = line.rstrip("\n")
        line2 = line.split(" ")
        user = line2[0]
        passwd = line2[1]
        money = int(line2[2])
        my = MySQLdb.connect(
                user = 'admin',
                passwd = '1234',
                host = 'database',
                db = 'tema',
                port = 3306)
        cursor = my.cursor()

        sql = "INSERT INTO users (user, passwd, money) VALUES (\"{0}\", \"{1}\", {2})".format(user, passwd, money)
        cursor.execute(sql)
        my.commit()
    elif option.strip() == '2':
        print("Remove account Selected")
        print("User:")
        user = str(raw_input())
        my = MySQLdb.connect(
            user='admin',
            passwd='1234',
            host='database',
            db='tema',
            port=3306)
        cursor = my.cursor()
        #aici
        sql = "DELETE FROM users WHERE user = %s"
        cursor.execute(sql, (user,))
        my.commit()
    elif option.strip() == '3':
        users = []
        my = MySQLdb.connect(
            user='admin',
            passwd='1234',
            host='database',
            db='tema',
            port=3306)
        cursor = my.cursor()
        cursor.execute("select * from users")
        res = cursor.fetchall()
        #aici vezi
        for x in res:
            users.append(list(x))
        for x in users:
            print(str(x))
    elif option.strip() == '4':
        print("Sesion is ending..")
        exit()
