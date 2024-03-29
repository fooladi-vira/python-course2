import sqlite3
# ایجاد پایگاه داده

class DB_Vira:
    
    def __init__(self,name_DB,table_sql):
        self.db = sqlite3.connect(name_DB)
        self.cursor = self.db.cursor()
        self.cursor.execute(table_sql)

   
    def add_user(self,name,last_name,code,phone,ID_course,name_course,price_course,pay):
        try:
            self.cursor.execute('''INSERT INTO user
                (code, name , last_name ,id_course , course ,phone ,price ,pay) VALUES (?, ?, ?,?, ?, ?,?, ?)''',
                (code, name , last_name ,ID_course , name_course ,phone ,price_course ,pay))
            self.db.commit()
        except:
            print('خطا ورود دیتا')

    def edit_user(self,name,last_name,code,phone,ID_course,name_course,price_course,pay):
                         
            try:
                self.cursor.execute("UPDATE user SET name = ?,last_name=?,id_course=?,course=?  , phone=? ,price=?,pay=? WHERE code = ?", ( name , last_name ,ID_course , name_course ,phone ,price_course ,pay,code))
                self.db.commit()
            except:
               print('خطا ویرایش داده')


    def delete_user(self,code):
        
        try:
            self.cursor.execute("DELETE FROM user WHERE code = ?", (code,))
            self.db.commit()
        except:
               print('خطا  ')

    def select_users(self):
        
        try:
            row_data=self.cursor.execute("SELECT * FROM user")
            return row_data
        except:
               print('خطا  ')


















# name_DB='vira.db'
# sql_create_table='''CREATE TABLE IF NOT EXISTS user
#                 (code INTEGER PRIMARY KEY ,
#                 name TEXT, last_name TEXT,id_course INTEGER, course TEXT,phone TEXT,price INTEGER,pay TEXT)'''
# db=DB_Vira(name_DB,sql_create_table)
# db.add_user('ali','fooladi',3579957295,'09107102595',123,'Python',1500000,'yes')
# db.edit_user('zeinab','fooladi',3579957295,'09107102595',123,'Python',1500000,'yes')
# #db.delete_user(3579957295)