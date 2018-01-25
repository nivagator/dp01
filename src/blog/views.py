from django.http import HttpResponse

from django.shortcuts import render

from .models import PostModel

# Create your views here.
# CRUD (and list)
# CREATE 

# RETRIEVE 

# UPDATE 

# DELETE

# LIST
def post_model_list_view(request):
    qs = PostModel.objects.all()
    print(qs)
    return HttpResponse("some data")