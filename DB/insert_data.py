import sqlite3

# برقراری ارتباط با پایگاه داده
conn = sqlite3.connect('example.db')

# افزودن یک رکورد جدید به جدول
conn.execute("INSERT INTO students (name, age) VALUES ('Ali', 20)")


# درج یک رکورد جدید در جدول "users"
conn.execute("INSERT INTO users (id, name) VALUES (?, ?)", (1, "John"))




# ذخیره تغییرات
conn.commit()

# بستن اتصال
conn.close()