from django.db import connection

def selectTest():
    cursor = connection.cursor()
    query_string = "select * from saving"
    cursor.execute(query_string)

    rows = cursor.fetchall()
    posts = []
    for row in rows:
        dic = {'id':row[0], 'money':row[1], 'time':row[2], 'date':row[3], 'userid':row[4]}
        posts.append(dic)

    return posts