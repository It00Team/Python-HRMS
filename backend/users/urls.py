from django.urls import path
from . import views

urlpatterns = [
    path('api/user-login/', views.UserAuth.as_view({'post': 'user_login'}), name='user-login'),
    path('api/user-logout/', views.UserAuth.as_view({'post': 'user_logout'}), name='user-logout'),

    path('api/users/', views.UserListView.as_view(), name='user-list'),
    path('api/users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),

    path('api/user-profiles/', views.UserProfileListView.as_view(), name='userprofile-list'),
    path('api/user-profiles/<int:pk>/', views.UserProfileDetailView.as_view(), name='userprofile-detail'),

]
