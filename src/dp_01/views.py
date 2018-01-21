from django.http import HttpResponse, HttpResponseRedirect

# def home(request):
#     print(request)
#     print(dir(request))
#     print(request.method)
#     print(request.get_full_path())
#     print(request.user)
#     print(request.environ)
#     return HttpResponse("<!DOCTYPE html><html><head><style>h1{color: blue;}</style></head><body><h1>Hello World!</h1></body></html>")

def home(request):
    response = HttpResponse()
    response.content = ('<!DOCTYPE html><html><head><style>h1{color: blue;}</style></head><body><h1>Hello World!</h1></body></html>')
    print(response.status_code)
    print(response.content)
    print(dir(response))
    # response.content = 'some new content'
    # response.write("<p>Here's the text of the Web page.</p>")
    # response.write("<p>Here's the text of the Web page.</p>")
    # response.write("<p>Here's the text of the Web page.</p>")
    # response.write("<p>Here's the text of the Web page.</p>")
    # response.status_code = 200
    return response

def redirect_somewhere(request):
    return HttpResponseRedirect("/some/path") #