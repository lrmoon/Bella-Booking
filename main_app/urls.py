from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("blog/", views.blog, name="blog"),
    path("contact/", views.contact, name="contact"),

    path("team/", views.contact, name="team"),
    path("pricing/", views.contact, name="pricing"),
    path("eye-makeup/", views.contact, name="eye-makeup"),

    path("404/", views.nope404, name="404"),
    path("coming-soon/", views.comingSoon, name="coming-soon")
    

]