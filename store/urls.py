from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('read_post_all', views.read_cart_all),
	path('add_product/', views.add_product),
	path('delete_product/<str:id>', views.delete_product),
	path('update_product/<str:id>', views.update_product),
	path('read_product/<str:id>', views.read_product),
	path('emp', views.emp),
	path('edit/<str:id>', views.edit), 
	path('update/<str:id>', views.update), 
	path('show',views.show),
	path('delete/<str:id>', views.delete),  
]
