from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>/', views.UserDetails.as_view(), name='user_details'),
    path('auctions/', views.AuctionList.as_view(), name='auction_list'),
    path('auctions/<int:pk>/', views.AuctionDetails.as_view(), name='auction_details'),
    path('bids/', views.BidList.as_view(), name='bid_list'),
    path('bids/<int:pk>/', views.BidDetails.as_view(), name='bid_details'),
    path('categories/', views.CategoryList.as_view(), name='category_list'),
    path('categories/<int:pk>/', views.CategoryDetails.as_view(), name='category_details'),
]
