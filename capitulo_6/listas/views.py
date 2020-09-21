from django.shortcuts import render, HttpResponse
import psycopg2


# Create your views here.

def home_page_view(request):
    return render(request, 'home.html')

# def insert(request):
#     return render(request, 'insert.html')


def insert(request):

    conn = psycopg2.connect(dbname   = "notas",
                            user     = "capitulo_4_user",
                            password = "patata")

    prioridad = request.POST['prioridad']
    titulo    = request.POST['subject']
    nota      = request.POST['msg']

    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO nota VALUES ('{prioridad}', '{titulo}', '{nota}')")

    conn.commit()

    cursor.close()
    conn.close()

    return HttpResponse('Insertado')

    # return HttpResponse(f'<h2> Insertado </h2> <br> '
    #                     '<dl>'
    #                     f'<dt><h3> prioridad: </h3></dt> <dd>{prioridad}</dd> <br>'
    #                     f'<dt><h3> titulo: <h3></dt> <dd>{titulo}</dd> <br>'
    #                     f'<dt><h3> nota: </h3></dt> <dd>{nota}</dd>'
    #                     '</dl>')


def select(request):

    conn = psycopg2.connect(dbname   = "notas",
                            user     = "capitulo_4_user",
                            password = "patata")

    cursor = conn.cursor()
    cursor.execute("select * from nota")

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


