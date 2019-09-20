from django.urls import path, reverse
from pyestoque.produto import views as v


app_name = 'produto'

urlpatterns = [
    path('', v.produto_list, name='produto_list'),
    path('<int:pk>/', v.produto_detail, name='produto_detail'),
    path('add/', v.produtoCreate.as_view(), name='produto_add'),
    path('<int:pk>/edit/', v.produtoUpdate.as_view(), name='produto_edit'),

]