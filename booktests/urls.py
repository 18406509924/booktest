from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from booktests import views

urlpatterns = [
    url(r'^books/$', views.BookListView.as_view()),
    url(r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view())
]

router = DefaultRouter()  # 路由Router
router.register('books', views.BookInfoViewSet)  # 向路由Router中注册视图集

urlpatterns += router.urls