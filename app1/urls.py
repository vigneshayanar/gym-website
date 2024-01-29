from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login_user,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout_user,name='logout'),
    path('members/',views.view_member,name='member'),
    path('addmembers/',views.view_add,name='add_member'),
    path('enquries/',views.view_enquiries,name='enquries'),
    path('addenquries/',views.view_enq,name='add_enq'),
    path('plan/',views.view_plan,name='plan'),\
    path('addplan/',views.view_planadd,name='planadd'),
    path('nutri/',views.nutrition,name='nutrition'),
    path('query/',views.query,name='query'),
    path('equipment',views.view_equipment,name="equipment"),

]