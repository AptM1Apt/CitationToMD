import sqlite3 as s 
import os 

filepath = 'citation.db'

def ConnectToDB():
    con = s.connect(filepath)
    cur = con.cursor()
    return cur, con

def CheckDB():
    if os.path.exists(filepath) and os.path.isfile(filepath):
        print("DB is here, no need to worry about it")
    else: 
        CreateDB()
        print("Created DB, just for you!")

def CreateDB():
    # Создаем подключение     
    cur, con = ConnectToDB()
    # Создаем БД для того, чтобы сохранять в нее цитаты. 
    # Если она есть - не создаем. Логично? Логично.
    scr = '''
    -- Таблица с авторами 
    CREATE TABLE Author(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(80)
    );

    -- Таблица с книгами 
    CREATE TABLE Book(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Title VARCHAR(80),
    Author_id INTEGER NOT NULL,
    FOREIGN KEY (Author_id) REFERENCES Author(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
    ); 

    -- Таблица с самими цитатами 
    CREATE TABLE Citation (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    Text TEXT,  -- Исправлено
    Book_id INTEGER NOT NULL,
    FOREIGN KEY (Book_id) REFERENCES Book(id)
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
    );
    '''

    cur.executescript(scr)
    con.close()

def AddAuthor(name: str):
    cur, con = ConnectToDB()
    check = cur.execute("SELECT Name FROM Author where Name = ?", (name)).fetchone()
    if check is None: 
        cur.execute("INSERT INTO Author (Name) VALUES (?)", (name))
    con.close()
    return 


def AddBook(name: str, title: str):
    cur, con = ConnectToDB()
    id = cur.execute("SELECT id FROM Author where Name = ?", (name)).fetchone
    check = cur.execute("SELECT Title FROM Book where Name = ?", (title)).fetchone()
    if check is None: 
        cur.execute("INSERT INTO Book (Title, Author_id) VALUES (?, ?)", (title, id))
    con.close()
    return 

def AddCitation(text: str, title: str): 
    cur, con = ConnectToDB()
    id = cur.execute("SELECT id FROM Book where Title = ?", (title)).fetchone
    check = cur.execute("SELECT id FROM Citation where Text = ?", (text)).fetchone()
    if check is None: 
        cur.execute("INSERT INTO Citation (Text, Book_id) VALUES (?, ?)", (text, id))
    con.close()
    return 

# TODO: Все взаимодействия с БДшкой, а именно
# Чтения записей из нее 
# Добавление записей в нее 
# Сортировки 
# Выдача записей
