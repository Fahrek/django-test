from django.shortcuts import render, HttpResponse
import psycopg2


# Create your views here.

def insert(request):

    conn = psycopg2.connect(dbname   = 'capitulo_4_db',
                            user     = 'capitulo_4_user',
                            password = 'patata')

    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO emp VALUES ('7364', 'HUGO', 'OFICINISTA', '7903', date '1980-12-17', '800.00', null, '20');"
    )

    conn.commit()

    cursor.close()
    conn.close()

    # with open('debug.log', 'a+') as debug_file:
    #     print('Funka!', file = debug_file)

    return HttpResponse('Registro insertado.')


def select(request):

    conn = psycopg2.connect(dbname   = 'capitulo_4_db',
                            user     = 'capitulo_4_user',
                            password = 'patata')

    cursor = conn.cursor()

    cursor.execute("select * from emp;")

    # Pinta los datos devueltos en HTML

    html = '<html>'

    columns = [col[0] for col in cursor.description]

    for column in columns:
        html += str(column) + '|'

    html += '<br>'

    for empleado in cursor.fetchall():
        for columna in empleado:
            html += str(columna) + '|'
        html += '<br>'

    html += '</html>'

    cursor.close()
    conn.close()

    return HttpResponse(html)
