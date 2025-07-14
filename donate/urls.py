from django.urls import path
from . import views

urlpatterns=[
    path('',views.landing_page,name='landingpage'),
    path('user_register/',views.user_reg,name='user_register'),
    path('users_home/',views.user_home,name='users_home'),
    path('ngos_home/',views.ngo_home,name='ngos_home'),
    path('login/',views.logins,name='login'),
    path('logout/',views.logout,name='logout'),
    path('profile_edit/',views.donor_profile,name='profile_edit'),
    path('add_donation/',views.donate,name='add_donation'),
    path('donations/',views.donation_view,name='donations'),
    path('all_donations/',views.view_donation,name='all_donations'),
    path('requested_food/<int:id>/',views.request_donation,name='requested_food'),
    path('admins/',views.admin_home,name='admins'),
    path('allusers/',views.admin_users,name='allusers'),
    path('alldonations/',views.admin_donations,name='alldonations'),
    path('allrequests/',views.admin_requests,name='allrequests'),
]