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


# RETRIEVE (detail) and LIST view
def post_model_detail_view(request, id=None):
    if id != None: 
    # Detail View
        obj = get_object_or_404(PostModel, id=id)
        context = {
            "object": obj,
            }
        template = "blog/detail-view.html"
    else: 
    # list view
        qs = PostModel.objects.all()
        context = {
                "object_list": qs,
            }
        template = "blog/list-view.html"
    return render(request, template, context)


# DELETE
def post_model_delete_view(request, id=None):
    # using detail view as a template here
    obj = get_object_or_404(PostModel, id=id)
    if request.method == "POST":
        obj.delete()
        messages.success(request, "successfully deleted post")
        return HttpResponseRedirect("/blog/")
    context = {
        "object": obj,
        }
    template = "blog/delete-view.html"
    return render(request, template, context)

