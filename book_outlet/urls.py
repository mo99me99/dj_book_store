from django.urls import path
from . import views


urlpatterns = [
    path('', view=views.index, name='index'),
    path('<int:id>/', view=views.book_detail_id, name='book-detail-id'),
    path('<slug:slug>/', view=views.book_detail, name='book-detail'),
]
