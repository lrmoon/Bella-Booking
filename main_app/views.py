from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'main_app/services.html')

def about(request):
    return render(request, 'main_app/about.html')

def portfolio(request):
    return render(request, 'main_app/portfolio.html')

def blog(request):
    return render(request, 'main_app/blog.html')

def contact(request):
    return render(request, 'main_app/contact.html')


#subpages render
def team(request):
    return render(request, 'main_app/pages/team.html')

def pricing(request):
    return render(request, 'main_app/pages/pricing.html')

def eyeMakeup(request):
    return render(request, 'main_app/pages/service-type/eye-makeup.html')



def nope404(request):
    return render(request, 'main_app/pages/misc/404.html')

def comingSoon(request):
    return render(request, 'main_app/pages/misc/coming-soon.html')





