from django.urls import path
from . import views

urlpatterns = [
    path('<int:commid>/<int:memid>', views.index, name="index"),
    path('<int:commid>/<int:memid>/add', views.add_post, name="addposts"),
    path('<int:memid>/<int:postid>/<int:commid>/edit',views.edit,name="edit"),
    path('<int:memid>/<int:commid>/memberpage',views.mem_post, name="memberpage"),
    path('<int:memid>/<str:name>/<int:commid>/profile',views.profile, name="profile"),
    path('<int:postid>/delete', views.del_post, name="delete"),
    path('<int:memid>/<int:postid>/<int:commid>/comment',views.post_comment,name="comment"),
    path('<int:commentid>/<int:memid>/<int:postid>/<int:commid>/delcomm',views.del_comment, name="del_comm")
]
