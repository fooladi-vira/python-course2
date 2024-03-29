import sqlite3

# برقراری ارتباط با پایگاه داده
conn = sqlite3.connect('example.db')

# اجرای یک دستور SELECT برای گرفتن تمام داده‌ها
cursor = conn.execute('SELECT * FROM students')

# چاپ داده‌ها
for row in cursor:
    print(row)

# بستن اتصال
conn.close()




# import sqlite3

# # باز کردن ارتباط با پایگاه داده
# conn = sqlite3.connect('mydatabase.db')

# # ساخت یک cursor برای اجرای دستور SQL
# cursor = conn.cursor()

# # اجرای دستور SQL برای فراخوانی داده‌ها از جدول users با شرط name='John' و age=30
# cursor.execute("SELECT * FROM users WHERE name=? AND age=?", ("John", 30))

# # دریافت تمام سطرهای بازگشتی
# rows = cursor.fetchall()

# # چاپ سطرهای بازگشتی
# for row in rows:
#     print(row)

# # بستن cursor و ارتباط با پایگاه داده
# cursor.close()
# conn.close()




# import sqlite3

# # باز کردن ارتباط با پایگاه داده
# conn = sqlite3.connect('mydatabase.db')

# # ساخت یک cursor برای اجرای دستور SQL
# cursor = conn.cursor()

# # اجرای دستور SQL برای فراخوانی داده‌ها از جدول orders با شرط user_id=1 و product='Laptop'
# cursor.execute("SELECT * FROM orders WHERE user_id=? AND product=?", (1, 'Laptop'))

# # دریافت تمام سطرهای بازگشتی
# rows = cursor.fetchall()

# # چاپ سطرهای بازگشتی
# for row in rows:
#     print(row)

# # بستن cursor و ارتباط با پایگاه داده
# cursor.close()
# conn.close()








# import sqlite3

# # باز کردن ارتباط با پایگاه داده
# conn = sqlite3.connect('mydatabase.db')

# # ساخت یک cursor برای اجرای دستور SQL
# cursor = conn.cursor()

# # اجرای دستور SQL برای فراخوانی داده‌ها از جدول orders و مرتب‌سازی بر اساس قیمت به صورت صعودی
# cursor.execute("SELECT * FROM orders ORDER BY price ASC")

# # دریافت تمام سطرهای بازگشتی
# rows = cursor.fetchall()

# # چاپ سطرهای بازگشتی
# for row in rows:
#     print(row)

# # بستن cursor و ارتباط با پایگاه داده
# cursor.close()
# conn.close()



# # مرتب‌سازی نتایج بر اساس قیمت به صورت نزولی
# cursor.execute("SELECT * FROM orders ORDER BY price DESC")




