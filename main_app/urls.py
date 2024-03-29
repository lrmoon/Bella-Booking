from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("portfolio/", views.portfolio, name="portfolio"),
    
    path("contact/", views.contact, name="contact"),

    

    path("pages/team/", views.team, name="team"),
    
    path("pages/pages-services/eye-makeup", views.eyeMakeup, name="eye-makeup"),
    path("pages/pages-services/hair-makeup/", views.hairMakeup, name="hair-makeup"),
    path("pages/pages-services/face-makeup/", views.faceMakeup, name="face-makeup"),
    path("pages/pages-services/bridal-makeup/", views.bridalMakeup, name="bridal-makeup"),
    path("pages/pages-services/fashion-makeup/", views.fashionMakeup, name="fashion-makeup"),
    path("pages/pages-services/fantastic-makeup/", views.fantasticMakeup, name="fantastic-makeup"),
    path("pages/pages-services/effect-makeup/", views.effectMakeup, name="effect-makeup"),
    path("pages/pages-services/child-face-painting/", views.childFacePainting, name="child-face-painting"),
    
    
    path("404/", views.nope404, name="404"),
    path("coming-soon/", views.comingSoon, name="coming-soon")
    

]