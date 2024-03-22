import sqlite3
db = sqlite3.connect('sql4.db')
c=db.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS user(
hobby TEXT,
name TEXT,
surname TEXT,
birthday DATE,
marks INTEGER
)   
''')
c.execute('''
DELETE FROM user;
''')
users_data = [
    ('Играть на гитаре', 'Иван', 'Иванововавоныч', '1990-01-01', 0),
    ('Читать книги', 'Петр', 'Петров', '1991-02-02', 78),
    ('Плавать', 'Анна', 'Сидорова', '1992-03-03', 92),
    ('Играть в футбол', 'Сергей', 'Козлов', '1993-04-04', 75),
    ('Рисовать', 'Мария', 'Кузнецова', '1994-05-05', 9),
    ('Смотреть фильмы', 'Алексей', 'Васильевеевич', '1995-06-06', 1),
    ('Готовить', 'Елена', 'Иванова', '1996-07-07', 82),
    ('Слушать музыку', 'Дмитрий', 'Смирновецов', '1997-08-08', 79),
    ('Фотографировать', 'Ольга', 'Попова', '1998-09-09', 7),
    ('Путешествовать', 'Артем', 'Соколов', '1999-10-10', 87)
]
c.executemany('''
INSERT INTO user (hobby, name, surname, birthday, marks)
VALUES (?, ?, ?, ?, ?)
''', users_data)
c.execute('''
SELECT * FROM user
WHERE LENGTH(surname) > 10;
''')

students_with_long_surname = c.fetchall()

print('Surname that has 10 or more symbols')
for student in students_with_long_surname:
    print(student)

c.execute('''
UPDATE user
SET name = 'genius'
WHERE marks > 10;
''')
c.execute('''
SELECT * FROM user
WHERE marks>10;
''')
genius_students = c.fetchall()
print('Students who has scored 10 or more balls in exam')
for student in genius_students:
    print(student)
c.execute('''
DELETE FROM user WHERE rowid % 2 == 0;
''')
db.commit()
db.close()