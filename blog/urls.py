from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    # post views
    path('', views.PostListView.as_view(), name='post_list'),
    path('submit/',views.post_submit,name='post_submit'),
    #path('', views.post_list, name='post_list'),
    path('<year>/<month>/<day>/<post>/',
         views.post_detail,
         name='post_detail'),
    path('<post_id>/share/',
 views.post_share, name='post_share'),
  path('<post_id>/comment/',
         views.post_comment, name='post_comment'),]