import sqlite3

# باز کردن ارتباط با پایگاه داده
conn = sqlite3.connect('mydatabase.db')

# ساخت یک cursor برای اجرای دستور SQL
cursor = conn.cursor()

# اجرای دستور SQL برای بازیابی نام و ایمیل کاربرانی که سفارشی با قیمت بیشتر از 100 دلار ثبت کرده‌اند
cursor.execute('''SELECT users.name, users.email
                  FROM orders
                  JOIN users ON orders.user_id = users.id
                  WHERE orders.price > 100''')

# دریافت تمام سطرهای بازگشتی
rows = cursor.fetchall()

# چاپ سطرهای بازگشتی
for row in rows:
    print(row)

# بستن cursor و ارتباط با پایگاه داده
cursor.close()
conn.close()



# SELECT students.name, courses.course_name
# FROM students
# JOIN enrollments ON students.id = enrollments.student_id
# JOIN courses ON courses.id = enrollments.course_id