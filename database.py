import sqlite3 as s 
import os 

filepath = 'citation.db'

def CreateDB():
    if os.path.exists(filepath) and os.path.isfile(filepath):
        print("DB is here, no need to worry about it")
    else: 
        _CreateDB()
        print("Created DB, just for you!")

def _CreateDB():

    # Создаем подключение     
    connection = s.connect(filepath)
    cur = connection.cursor()

    # Создаем БД для того, чтобы сохранять в нее цитаты. 
    # Если она есть - не создаем. Логично? Логично.
    scr = '''
    -- Таблица с авторами 
    CREATE TABLE Author(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(80));

    -- Таблица с книгами 
    CREATE TABLE Book(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(80));

    -- Таблица с самими цитатами 
    CREATE TABLE Citation (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    Text LONGTEXT, 
    Author_id INTEGER NOT NULL, 
    Book_id INTEGER NOT NULL,
    FOREIGN KEY (Author_id) REFERENCES Author(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (Book_id) REFERENCES Book(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE);
    '''

    cur.executescript(scr)
    connection.close()

# TODO: Все взаимодействия с БДшкой, а именно
# Чтения записей из нее 
# Добавление записей в нее 
# Сортировки 
# Выдача записей
