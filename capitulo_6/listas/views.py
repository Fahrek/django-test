from django.shortcuts import render, HttpResponse


# Create your views here.

def home_page_view(request):
    return render(request, 'home.html')

# def insert(request):
#     return render(request, 'insert.html')

def insert(request):
    prioridad = request.POST['prioridad']
    titulo    = request.POST['subject']
    nota      = request.POST['msg']

    return HttpResponse(f'<h2> Insertado </h2> <br> '
                        '<dl>'
                        f'<dt><h3> prioridad: </h3></dt> <dd>{prioridad}</dd> <br>'
                        f'<dt><h3> titulo: <h3></dt> <dd>{titulo}</dd> <br>'
                        f'<dt><h3> nota: </h3></dt> <dd>{nota}</dd>'
                        '</dl>')
