from django.urls import path
from .views import registFunc, loginFunc, listFunc, logoutFunc, mypageFunc, detailFunc, goodFunc, readFunc, BoardCeate

urlpatterns = [
    path('regist/', registFunc, name='regist'),
    path('login/', loginFunc, name='login'),
    path('logout/', logoutFunc, name='logout'),
    path('list/', listFunc, name='list'),
    path('mypage/', mypageFunc, name="mypage"),
    path('detail/<int:pk>', detailFunc, name='detail'),
    path('good/<int:pk>', goodFunc, name='good'),
    path('read/<int:pk>', readFunc, name='read'),
    path('create/', BoardCeate.as_view(), name='create')
]
