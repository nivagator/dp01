from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from .models import PostModel

# Create your views here.
# CRUD (and list)
# CREATE 

# RETRIEVE 
def post_model_detail_view(request):
    obj = get_object_or_404(PostModel, id=1)
    context = {
        "object": obj,
        }
    template = "blog/detail-view.html"
    return render(request, template, context)

# UPDATE 

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
