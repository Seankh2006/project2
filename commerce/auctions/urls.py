from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("display", views.displaylist, name="display"),
    path("auction/<int:id>", views.auctiondetails, name="auctions"),
    path("lists/<int:id>", views.lists, name="lists"),
    path("removewatchlist/<int:id>", views.remove, name="remove"),
    path("watchlist1", views.watchlist1, name="watchlist1")
]
