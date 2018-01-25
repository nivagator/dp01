from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .forms import PostModelForm
from .models import PostModel

# Create your views here.
# CRUD (and list)
# CREATE 
# @login_required(login_url='/login')
def post_model_create_view(request):
    # if request.method == 'POST':
    #     # print(request.POST)
    #     form = PostModelForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit=False)
    #         print(form.cleaned_data)
    #     else:
    #         print("invalid data")


    form = PostModelForm(request.POST or None)
    context = {
        "form": form,
        }
    if form.is_valid():
        print(form.cleaned_data)
        obj = form.save(commit=False)
        # print(obj.title)
        obj.save() # this writes to db
        messages.success(request, "Created a new blog post")
        context = { # putting context here clears the form
            "form": PostModelForm()
        }
        # return HttpResponseRedirect("/blog/{num}".format(num=obj.id))
    else:
        print("invalid data")
   
    template = "blog/create-view.html"
    return render(request, template, context)

# RETRIEVE 
def post_model_detail_view(request, id=None):
    # try: 
    #     obj = PostModel.objects.get(id=1)
    # except: 
    #     raise Http404

    # qs = PostModel.objects.filter(id=100)
    # obj = none
    # if not qs.exists() and qs.count() != 1:
    #     raise Http404
    # else:
    #     obj = qs.first()

    obj = get_object_or_404(PostModel, id=id)
    context = {
        "object": obj,
        }
    template = "blog/detail-view.html"
    return render(request, template, context)

# UPDATE 
# @login_required(login_url='/login')
def post_model_update_view(request, id=None):
    obj = get_object_or_404(PostModel, id=id)
    form = PostModelForm(request.POST or None, instance=obj)
    context = {
        "form": form,
        }
    if form.is_valid():
        print(form.cleaned_data)
        obj = form.save(commit=False)
        # print(obj.title)
        obj.save() # this writes to db
        messages.success(request, "Updated post!")
        return HttpResponseRedirect("/blog/{num}".format(num=obj.id))
    else:
        print("invalid data")
   
    template = "blog/update-view.html"
    return render(request, template, context)


# DELETE


# LIST
def post_model_list_view(request):
    qs = PostModel.objects.all()
    context = {
            "object_list": qs,
        }
    template = "blog/list-view.html"
    return render(request, template, context)

@login_required(login_url='/login')
def login_required_view(request):
    print(request.user)
    qs = PostModel.objects.all()
    context = {
            "object_list": qs,
        }
    if request.user.is_authenticated:
        print("logged in")
        template = "blog/list-view.html"
    else:
        print("not logged in")
        template = "blog/list-view-public.html"
        raise Http404
        # return HttpResponseRedirect("/login")
    return render(request, template, context)
