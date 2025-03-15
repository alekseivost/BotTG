import sqlite3

class db():
    def __init__(self,db_file_name):
        self.f_name = db_file_name

    def check_user_db(self,telegram_id):
        connection = sqlite3.connect(self.f_name)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users WHERE id_tg = ?', (telegram_id,))
        results = cursor.fetchall()
        connection.close()
        if(len(results) == 0):
            return 0
        else:
            return 1

    def create_user_db(self,telegram_id):
        connection = sqlite3.connect(self.f_name)
        cursor = connection.cursor()
        cursor.execute('INSERT INTO Users (id_tg, user_status) VALUES (?, ?)', (telegram_id, 0))
        connection.commit()
        connection.close()

    def reload_user_db(self,telegram_id):
        connection = sqlite3.connect(self.f_name)
        cursor = connection.cursor()
        cursor.execute('UPDATE Users SET user_status = ? WHERE id_tg = ?', (0, telegram_id))
        connection.commit()
        connection.close()

    def set_status_user_db(self,telegram_id,sts):
        connection = sqlite3.connect(self.f_name)
        cursor = connection.cursor()
        cursor.execute('UPDATE Users SET user_status = ? WHERE id_tg = ?', (sts, telegram_id))
        connection.commit()
        connection.close()

    def get_status_user_db(self,telegram_id):
        connection = sqlite3.connect(self.f_name)
        cursor = connection.cursor()
        cursor.execute('SELECT user_status FROM Users WHERE id_tg = ?', (telegram_id,))
        results = cursor.fetchall()
        connection.close()
        return results[0][0]

    def set_parametr_user_db(self,telegram_id,parametr,value):
        connection = sqlite3.connect(self.f_name)
        cursor = connection.cursor()
        cursor.execute(f'UPDATE Users SET {parametr} = ? WHERE id_tg = ?', (value, telegram_id))
        connection.commit()
        connection.close()

    def get_allinfo_user_db(self,telegram_id):
        connection = sqlite3.connect(self.f_name)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users WHERE id_tg = ?', (telegram_id,))
        results = cursor.fetchall()
        connection.close()
        user_info = []
        for i in results:
            user_info.append(i)
        return user_info

    def get_target_parametr_user_db(self,telegram_id,parametr):
        connection = sqlite3.connect(self.f_name)
        cursor = connection.cursor()
        cursor.execute(f'SELECT {parametr} FROM Users WHERE id_tg = ?', (telegram_id,))
        results = cursor.fetchall()
        connection.close()
        return results[0][0]
