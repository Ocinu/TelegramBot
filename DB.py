import sqlite3


class DB:
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    # Управление подпиской
    def get_subscriptions(self, status=True):
        with self.connection:
            return self.cursor.execute(f"SELECT * FROM 'subscribles' WHERE 'status' = {status}").fetchall()

    def subscriber_exist(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'subscribles' WHERE User_ID = %d" % user_id).fetchall()
            return bool(len(result))

    def add_subscriber(self, user_id, status=True):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'subscribles' ('User_ID', 'status') "
                                       "VALUES (?, ?)", (user_id, status))

    def update_subscription(self, user_id, status):
        self.cursor.execute(f"UPDATE 'subscribles' SET 'status' = {status} WHERE User_ID = {user_id}")
        self.connection.commit()

    # Логи
    def save_log(self, user_id, user_name, date, section):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'logs' ('User_ID', 'User_Name', 'date', 'section')"
                                       "VALUES(?,?,?,?)", (user_id, user_name, date, section))

    def close(self):
        self.connection.close()
