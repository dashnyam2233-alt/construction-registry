from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .models import Banner, PublicPost


LOGIN_URL = reverse_lazy("login")


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = PublicPost
        fields = ("title", "body")


@login_required(login_url=LOGIN_URL)
def community_home(request):
    banners = Banner.objects.filter(is_active=True).order_by("sort_order", "-created_at")[:10]
    posts = PublicPost.objects.filter(is_published=True).order_by("-created_at")[:50]
    return render(request, "registry/community_home.html", {"banners": banners, "posts": posts})


@login_required(login_url=LOGIN_URL)
def post_create(request):
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.is_published = True
            obj.save()
            return redirect("community:home")
    else:
        form = PostCreateForm()

    return render(request, "registry/post_create.html", {"form": form})
