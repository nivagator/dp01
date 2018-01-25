from django.urls import path

from .views import (
    post_model_list_view, 
    post_model_detail_view,
)

urlpatterns = [
    path('', post_model_list_view, name='list'),
    path('1/', post_model_detail_view, name='detail'),
    # path('admin/', admin.site.urls),
    # path('', home, name='home'),
    # path('redirect/', redirect_somewhere, name='redir')
    
]
