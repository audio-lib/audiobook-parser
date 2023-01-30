import sqlite3


class Connection:
    def __init__(self):
        self.conn = sqlite3.connect('tele.db')
        self.conn.cursor().execute("""CREATE TABLE if not exists records(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            link TEXT NOT NULL,
            author TEXT NOT NULL,
            title TEXT NOT NULL
        );
        """)

    def save_record(self, link: str, author: str, title: str):
        record = (link, author, title)
        conn = self.conn.cursor()
        conn.execute("INSERT INTO records(link, author, title) VALUES (?, ?, ?)", record)
        self.conn.commit()
