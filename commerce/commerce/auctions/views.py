
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

import auctions
from .models import User, category, listing, command


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
    wlist = request.user in auction1.watchlist.all()
    message = "welcome"
    if request.method == "POST":
        price1 = request.POST["bid"]
        if float(price1) > auction1.price:
            auction1.price = price1
            auction1.save()
            message = "Congratulations, you won the bid!"
        else:
            message = "Sorry, you're not the highest bidder!"
    return render(request, "auctions/auction.html", {"auctions" : auction1, "watchlist" : wlist, "message" : message})

def lists(request, id):
    auction1 = listing.objects.get(pk = id)
    currentuser = request.user
    auction1.watchlist.add(currentuser)
    wlist = request.user in auction1.watchlist.all()
    return render(request, "auctions/auction.html", {"auctions" : auction1, "watchlist" : wlist})

def remove(request, id):
    auction1 = listing.objects.get(pk = id)
    currentuser = request.user
    auction1.watchlist.remove(currentuser)
    wlist = request.user in auction1.watchlist.all()
    return render(request, "auctions/active.html", {"auctions" : auction1, "watchlist" : wlist})

def watchlist1(request):
    currentuser = request.user
    list = currentuser.watchlist2.all()
    return render(request, "auctions/watchlist.html", {"current" : currentuser, "list" : list})

def comments(request, id):
    name1 = request.user
    listing2 = listing.objects.get(pk = id)
    message1 = request.POST["textbox"]
    createcomment = command(name = name1, listing = listing2, message = message1)
    createcomment.save()
    allcomments = command.objects.all()
    wlist = request.user in listing2.watchlist.all()
    return render(request, "auctions/auction.html", {"comment" : allcomments, "auctions" : listing2, "watchlist" : wlist})

def closebid(request, id):
    list = listing.objects.get(pk = id)
    list.listing.remove(pk = id)
    currentuser = request.user
    list.watchlist.remove(currentuser)
    wlist = request.user in list.watchlist.all()
    currentuser = request.user
    list2 = currentuser.watchlist2.all()
    category4 = request.POST["e-commerce"]
    category1 = category.objects.get(categorylist = category4)
    activelisting = listing.objects.filter(categorylist1 = category1)
    categorylist3 = category.objects.all()
    return render(request, "auctions/active.html", {"auctions" : list2, "watchlist" : wlist, "activelisting" : activelisting, "list" : categorylist3})
