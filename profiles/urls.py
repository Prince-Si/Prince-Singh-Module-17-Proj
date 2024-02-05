from django.urls import path

from . import views

app_name = "profiles"

urlpatterns = [
    path("<str:username>/", views.ProfileDetailView.as_view(), name="detail"),
    path("<str:username>/follow/", views.FollowView.as_view(), name="follow"),
    path('</render_account_page/', views.render_account_page, name='render_account_page'),
]
