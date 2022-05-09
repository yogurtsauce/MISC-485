import sqlite3

connect = sqlite3.connect('hw2.db')
cursor = connect.cursor()

cursor.execute('''
               create table Agent (
                   AgentId integer not null primary key autoincrement,
                   FirstName varchar not null,
                   LastName varchar not null
               )
               ''')
connect.commit()

cursor.execute('''
               create table Author (
                   AuthorId integer not null primary key autoincrement,
                   FirstName varchar not null,
                   LastName varchar not null,
                   AgentId int not null references Agent(AgentId)
               )
               ''')
connect.commit()

cursor.execute('''
               create table Book (
                   AuthorId int not null references Author(AuthorId),
                   EditorId int not null references Editor(EditorId),
                   Genre varchar not null,
                   BookName varchar not null,
                   PubDate date not null,
                   NumPages int not null,
                   primary key(AuthorId, EditorId)
               )
               ''')
connect.commit()

cursor.execute('''
               create table Editor (
                   EditorId integer not null primary key autoincrement,
                   FirstName varchar not null,
                   LastName varchar not null, 
                   MentorEditorId int references Mentor(MentorId)
               )
               ''')
connect.commit()

cursor.execute('''
               create table Mentor (
                   MentorId int,
                   EditorId int references Editor(EditorId),
                   primary key(MentorId, EditorId)
               )
               ''')

connect.commit()
connect.close()