
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User, category, listing


def index(request):
    activelisting = listing.objects.all()
    categorylist3 = category.objects.all()
    return render(request, "auctions/active.html", {"activelisting" : activelisting, "list" : categorylist3})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create(request):
    if request.method == "GET":
        categorylist = category.objects.all()
        return render (request, "auctions/create.html", {'categorylist' : categorylist})
    else:
        title = request.POST["title"]
        description = request.POST["description"]
        price = request.POST["price"]
        date = request.POST["date"]
        image = request.POST["image"]
        category2 = request.POST["e-commerce"]
        owner = request.user
        category1 = category.objects.get(categorylist = category2)
        createlisting = listing(title = title,
        description = description, price = price,
        date = date, img = image,
        categorylist1 = category1)
        createlisting.save()
        return render(request, "auctions/index.html")

def displaylist(request):
    if request.method == "POST":
        category4 = request.POST["e-commerce"]
        category1 = category.objects.get(categorylist = category4)
        activelisting = listing.objects.filter(categorylist1 = category1)
        categorylist3 = category.objects.all()
        return render(request, "auctions/active.html", {"activelisting" : activelisting, "list" : categorylist3})

def auctiondetails(request, id):
    auction1 = listing.objects.get(pk = id)

    if request.method == "POST":
        price = request.POST["bid"]
        category5 = request.POST["e-commerce"]
        price1 = listing(price = price, category1 = category.objects.get())
        price1.save()
    return render(request, "auctions/auction.html", {"auctions" : auction1})
