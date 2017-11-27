from django.shortcuts import render

def about(request):
    data = []
    if request.method == 'GET':
        data = request.GET
    if request.method == 'POST':
        data = request.POST
    return render(request, 'about.html',
    {'method': request.method, 'data': data.get('yourPost')})