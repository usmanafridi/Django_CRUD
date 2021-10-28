
from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name="index"),
    path('hello', views.say_hello),
    path('logout', views.logout),
    path('echo/<int:day>/<int:month>/<int:year>', views.echo),
    path('echo/<int:day>/<int:month>/<int:year>', views.echo),
    path('products/<str:name>', views.list_products),

    path('management/<str:heirarchy>/<int:id>',
         views.search_by_heirarchy_and_id),
    path('management/<str:heirarchy>/<slug:slug>',
         views.search_by_heirarchy_and_slug),
    path('management/<str:heirarchy>/age/<int:age>',
         views.search_by_heirarchy_and_age),

    path('products/', views.list_products, name="product-list"),
    path('products/add/', views.add_product, name="product-add"),
    path('products/form-receiver/', views.form_receiver, name="product-receiver"),
    # path('products/<int:id>/', views.product_detail),

    # Mobile URLS
    path('mobiles/', views.list_mobiles, name="mobile-list"),
    path('mobiles/add', views.create_mobile, name="mobile-add"),
    # path('mobiles/add', views.MobileCreate.as_view(), name="mobile-add"),
    path('mobiles/<int:id>/', views.retrieve_mobile, name="mobile-detail"),
    path('mobiles/<int:id>/edit', views.update_mobile, name="mobile-edit"),
    path('mobiles/<int:id>/delete', views.delete_mobile, name="mobile-delete"),




    #Hotel Booking

    path('hotels/', views.list_bookings, name="booking-list"),
    path('hotels/add', views.create_booking, name="booking-add"),
    path('hotels/<int:id>/', views.retrieve_booking, name="booking-detail"),
    path('hotels/<int:id>/edit', views.update_booking, name="booking-edit"),
    path('hotels/<int:id>/delete', views.delete_booking, name="booking-delete"),



]
