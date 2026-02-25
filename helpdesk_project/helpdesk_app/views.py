from django.shortcuts import render, redirect
from .models import Query

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        question = request.POST.get("question")

        Query.objects.create(
            name=name,
            email=email,
            question=question
        )
        return redirect("home")

    queries = Query.objects.all().order_by("-created_at")
    return render(request, "home.html", {"queries": queries})