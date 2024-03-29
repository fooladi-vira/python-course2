import sqlite3

# ایجاد یک پایگاه داده جدید
conn = sqlite3.connect('test.db')

# ایجاد یک جدول در پایگاه داده
conn.execute('''CREATE TABLE students
             (id INT PRIMARY KEY NOT NULL,
             name TEXT NOT NULL,
             age INT NOT NULL,
             email CHAR(50));''')

# وارد کردن داده‌ها به جدول
conn.execute("INSERT INTO students (id, name, age, email) \
              VALUES (1, 'John Doe', 20, 'john.doe@example.com')")
conn.execute("INSERT INTO students (id, name, age, email) \
              VALUES (2, 'Jane Doe', 22, 'jane.doe@example.com')")

# ذخیره تغییرات
conn.commit()

# بازیابی و چاپ داده‌ها
cursor = conn.execute("SELECT id, name, age, email from students")
for row in cursor:
    print("ID = ", row[0])
    print("Name = ", row[1])
    print("Age = ", row[2])
    print("Email = ", row[3], "\n")

# حذف جدول
conn.execute("DROP TABLE students")

# ذخیره تغییرات
conn.commit()

# بستن اتصال
conn.close()