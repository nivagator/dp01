from django.urls import path, include

from .views import (
    post_model_create_view,
    post_model_list_view, 
    post_model_delete_view,
    post_model_detail_view,
    post_model_update_view,
)

app_name='blog'

urlpatterns = [
    path('', post_model_list_view, name='list'),
    path('create/', post_model_create_view, name='create'),
    path('<id>/', post_model_detail_view, name='detail'),
    path('<id>/delete/', post_model_delete_view, name='delete'),
    path('<id>/edit/', post_model_update_view, name='update'),
    
    # path('admin/', admin.site.urls),
    # path('', home, name='home'),
    # path('redirect/', redirect_somewhere, name='redir')
    
]
