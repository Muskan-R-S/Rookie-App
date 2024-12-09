from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import User, Candidate, Mandate
from .forms import MandateForm


@login_required
def index(request):
    return render(request, "network/index.html")


@login_required
def candidates(request):
    return render(request, "network/candidates.html", {
        "title": "Candidates",
        "candidates": Candidate.objects.all(),
    })


@login_required
def mandates(request):
    user_mandates = Mandate.objects.filter(user=request.user) 
    return render(request, "network/mandates.html", {
        "title": "Mandates",
        "mandates": user_mandates,
    })


@login_required
def add_candidate(request):

    if request.method == "POST":
        fname = request.POST.get("first_name")
        lname = request.POST.get("last_name")
        emailid = request.POST.get("email_id")
        dob = request.POST.get("DOB")
        cur_role = request.POST.get("current_role")
        cur_ctc = request.POST.get("current_ctc")
        exp = request.POST.get("experience")

        try:
            new_candidate = Candidate(first_name = fname, last_name = lname, 
            email_id = emailid, DOB = dob, current_role = cur_role,
            current_ctc = cur_ctc, experience = exp)
            new_candidate.save()
        except Exception as e:
            print(e)
            return render(request, "network/add_candidate_form.html", {
                "message": "Could not save, try again later"
            })
        
        return HttpResponseRedirect(reverse("candidates"))


    return render(request, "network/add_candidate_form.html")

@login_required
def add_mandate(request):

    if request.method == "POST":
        company = request.POST.get("c_name")
        requirement = request.POST.get("requirement")
        role_name = request.POST.get("role_name")

        try:
            new_mandate = Mandate(company_name = company, 
                requirement = requirement, 
                role_name = role_name)
            new_mandate.save()
        except Exception as e:
            print(e)
            return render(request, "network/add_candidate_form.html", {
                "message": "Could not save, try again later"
            })
        
        return HttpResponseRedirect(reverse("candidates"))


    return render(request, "network/add_candidate_form.html")



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    '''Register a new user'''
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        user_role = request.POST["role"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        print(username, email, password, confirmation)
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username,
                                            first_name=first_name, last_name=last_name, user_role=user_role, email=email, password=password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
    

def update_status(request, candidate_id):
    if request.method == "POST":
        candidate = get_object_or_404(Candidate, id=candidate_id)
        new_status = request.POST.get('status')
        if new_status:
            candidate.status = new_status
            candidate.save() 
        return redirect('candidates') 
    return render(request, "error.html", {"message": "Invalid request"})


@login_required
def add_mandate(request):
    if request.method == "POST":
        form = MandateForm(request.POST)
        if form.is_valid():
            mandate = form.save(commit=False)
            mandate.user = request.user  # Associate the logged-in user
            mandate.save()
            return redirect('mandates')  # Redirect to the mandates page
    else:
        form = MandateForm()
    return render(request, "network/add_mandate.html", {"form": form})
