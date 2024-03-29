import sqlite3

# برقراری ارتباط با پایگاه داده
conn = sqlite3.connect('example.db')

# ایجاد جدول با کلید اصلی
conn.execute('CREATE TABLE students (name TEXT PRIMARY KEY, age INT)')



# # افزودن ستون به جدول
# conn.execute('ALTER TABLE students ADD COLUMN email TEXT')



# # حذف ستون
# conn.execute('ALTER TABLE students DROP COLUMN email')


# ذخیره تغییرات
conn.commit()

# بستن اتصال
conn.close()



