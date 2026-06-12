import os
import sqlite3

def create_database():
    db = 'quiz.db'

    if not os.path.exists(db):
        con = sqlite3.connect(db)
        cur = con.cursor()

        script = '''
CREATE TABLE quiz(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    nos INTEGER NOT NULL
);
CREATE TABLE question(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer INTEGER NOT NULL
);
CREATE TABLE answers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ans_1 TEXT NOT NULL,
    ans_2 TEXT NOT NULL,
    ans_3 TEXT NOT NULL,
    ans_4 TEXT NOT NULL
);
CREATE TABLE qanda(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    quiz_id INTEGER NOT NULL,    
    ques_id INTEGER NOT NULL,
    ans_id INTEGER NOT NULL,
    FOREIGN KEY (quiz_id) REFERENCES quiz(id),
    FOREIGN KEY (ques_id) REFERENCES question(id),
    FOREIGN KEY (ans_id) REFERENCES answers(id)
);
        '''

        cur.executescript(script)
        con.commit()
        con.close()