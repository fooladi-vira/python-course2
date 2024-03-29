import sqlite3

# برقراری ارتباط با پایگاه داده
db = sqlite3.connect('company.db')
#ایجاد شی برای اجرای دستورات sql
cursor = db.cursor()

sql='CREATE TABLE IF NOT EXISTS students (name TEXT , age INT,course TEXT)'
cursor.execute(sql)
db.commit()
cursor.execute('CREATE TABLE IF NOT EXISTS courses(name TEXT,len INT,price INT,date TEXT)')
db.commit()

for i in range(1,5):
    name=input('enter your name  ')
    age=int(input('enter your age   '))
    course=input('enter name course  ')
    cursor.execute("INSERT INTO students (name, age,course) VALUES (?, ?,?)", (name, age ,course))
    db.commit()


data_rows = cursor.execute('SELECT * FROM students')
for row in data_rows:
    print(row)

#cursor.execute("DROP TABLE students")
db.close()





# #######################3####################
# # ایجاد یک جدول به نام "users" با دو ستون "id" و "name"
# cursor.execute('''CREATE TABLE IF NOT EXISTS  users
#                  (id INTEGER PRIMARY KEY, name TEXT)''')







# # #######################7####################
# cursor.execute("UPDATE users SET name = ? WHERE id = ?", ("Jack", 1))
# db.commit()



# # #######################8####################
# # بازیابی و چاپ داده‌ها
# cursor = cursor.execute("SELECT id, name, age, email from students")
# for row in cursor:
#     print("ID = ", row[0])
#     print("Name = ", row[1])
#     print("Age = ", row[2])
#     print("Email = ", row[3], "\n")

# # حذف جدول
# cursor.execute("DROP TABLE students")

# # ذخیره تغییرات
# cursor.commit()