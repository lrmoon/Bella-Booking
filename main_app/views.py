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
    return render(request, 'main_app/pages/pages-services.html')

def hairMakeup(request):
    return render(request, 'main_app/pages/service-type/hair-makeup.html')

def faceMakeup(request):
    return render(request, 'main_app/pages/service-type/face-makeup.html')

def bridalMakeup(request):
    return render(request, 'main_app/pages/service-type/bridal-makeup.html')

def fashionMakeup(request):
    return render(request, 'main_app/pages/service-type/fashion-makeup.html')

def fantasticMakeup(request):
    return render(request, 'main_app/pages/service-type/fantastic-makeup.html')

def effectMakeup(request):
    return render(request, 'main_app/pages/service-type/effect-makeup.html')

def childFacePainting(request):
    return render(request, 'main_app/pages/service-type/child-face-painting.html')



def nope404(request):
    return render(request, 'main_app/pages/misc/404.html')

def comingSoon(request):
    return render(request, 'main_app/pages/misc/coming-soon.html')





