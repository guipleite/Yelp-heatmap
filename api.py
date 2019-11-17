from fastapi import FastAPI
import pymysql


app = FastAPI()

def run_db_query(connection, query, args=None):
    with connection.cursor() as cursor:
        print('Executando query:')
        cursor.execute(query, args)
        for result in cursor:
            print(result)


def connect_db():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='MegaDados',
        database='yelp')
    return connection

@app.get('/user/{id}')
def insert_user(id: str):
    connection = connect_db()
    with connection.cursor() as cursor:
            cursor.execute('''  SELECT * 
                                FROM Usuarios_Business 
                                RIGHT JOIN idBusiness on idBusiness.business_id = Usuarios_Business.business_id  
                                WHERE Usuarios_Business.user_id = %s ''',(id))
            
            data = cursor.fetchall()
            print(data)
    return data