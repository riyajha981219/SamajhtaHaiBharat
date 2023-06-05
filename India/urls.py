from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('signup',views.signup, name="signup"),
    path('login', views.login_view, name="login"),
    path('logout',views.logout_view, name="logout"),
    path('<int:state_id>/add', views.add_member, name="add"),
    path('<int:state_id>/state', views.state, name="state")
]
