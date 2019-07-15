import sqlite3

# def getListNam


dbname = 'todo.db'

# initail table


def create_todolist_table():
    c = sqlite3.connect(dbname)
    c.execute('drop table todolist;')
    c.execute(
        'create table todolist ('
        + '[id]            integer PRIMARY KEY autoincrement, '
        + '[name]          varchar(50) not null,'
        + '[orderid]         int default 999,'
        + '[createdate]      datetime default (datetime(\'now\', \'localtime\'))'
        + ');'
    )
    c.close()


def create_todoitem_table():
    c = sqlite3.connect(dbname)
    c.execute('drop table todoitem;')
    res = c.execute('create table todoitem('
                    + '[id] integer PRIMARY KEY autoincrement,'
                    + '[listcode] int default -1,'
                    + '[content] varchar(300) default \'\','
                    + '[orderid] int default 999'
                    + '[createdate]      datetime default (datetime(\'now\', \'localtime\')));'
                    )
    c.close()


def create_tables():
    create_todolist_table()
    create_todoitem_table()


def add_todolist(name, orderid):
    c = sqlite3.connect(dbname)
    res = c.execute(
        'insert into todolist values(null,?,?,null);', name, orderid)
    c.close()

# def del_todolist(id):
#     c = sqlite3.connect(dbname)
#     res = c.execute