from django.shortcuts import render

# Create your views here.
def index(request):
    print(request.method)
    return render(request,
    'portfolio_app/index.html')

def index2(request):
    print(request.method)
    return render(request,
    'portfolio_app/index2.html')
