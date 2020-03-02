from django.urls import path
from .views import (
	ItemDetailView,
    ItemListView,
    ItemCreateView,
    ItemUpdateView,
    login_view,
    logout_view,
    ItemDeleteView,
    BoletoCreateView,
    BoletoDetailView,
    BoletoListView,
    # ItemDeleteView,
    # home_view,
    # OrderSummaryView,
    # add_to_cart,
    # remove_from_cart,
    # remove_single_item_from_cart,
    )

app_name = 'core'

urlpatterns = [
	path('', login_view, name='login'),
	path('logout/', logout_view, name='logout'),
	path('list/', ItemListView.as_view(), name='item-list'),
	path('boleto_list/', BoletoListView.as_view(), name='boleto-list'),
	# path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
	
	# path('add-to-cart/<int:id>/', add_to_cart, name='add-to-cart'),
	path('create/', ItemCreateView.as_view(),name='item-create'),
	path('create_boleto/', BoletoCreateView.as_view(),name='boleto-create'),
	# path('<slug:slug>,<int:id>//', ItemDetailView.as_view(), name='item'),
	# path('remove-from-cart/<int:id>/', remove_from_cart, name='remove-from-cart'),
	# path('remove-item-from-cart/<int:id>/', remove_single_item_from_cart,
 #         name='remove-single-item-from-cart'),
 	path('<int:id>/detail/', ItemDetailView.as_view(), name='item-detail'),
 	path('<int:id>/detail_boleto/', BoletoDetailView.as_view(), name='boleto-detail'),
	path('<int:id>/delete/', ItemDeleteView.as_view(), name='item-delete'),
	# path('<int:id>/update/', ItemUpdateView.as_view(), name='item-create'),
	# path('', home_view, name='home_view'),
]


