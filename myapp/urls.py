
from django.contrib import admin
from django.urls import path
from . import  views
urlpatterns = [
    path('',views.loginTemp,name='loginTemp'),
    path('logout',views.logout,name='logout'),
    path('AdminHome',views.AdminHome,name='AdminHome'),
    path('loginPost',views.loginPost,name='loginPost'),
    path('feedback',views.feedback,name='feedback'),
    path('expert_Add',views.expert_Add,name='expert_Add'),
    path('admin_view_user',views.admin_view_user,name='admin_view_user'),
    path('admin_view_tips',views.admin_view_tips,name='admin_view_tips'),
    path('admin_view_expert',views.admin_view_expert,name='admin_view_expert'),
    path('edit_expert_post',views.edit_expert_post,name='edit_expert_post'),
    path('delete_expert/<id>',views.delete_expert,name='delete_expert'),
    path('edit_expert/<id>',views.edit_expert,name='edit_expert'),


    path('expert_home',views.expert_home,name='expert_home'),
    path('add_tips',views.add_tips,name='add_tips'),
    path('add_solution',views.add_solution,name='add_solution'),
    path('expert_view_solutions',views.expert_view_solutions,name='expert_view_solutions'),
    path('expert_view_tips',views.expert_view_tips,name='expert_view_tips'),
    path('delete_tips/<id>',views.delete_tips,name='delete_tips'),
    path('edit_tips/<id>',views.edit_tips,name='edit_tips'),
    path('delete_solution/<id>',views.delete_solution,name='delete_solution'),
    path('edit_solutions/<id>',views.edit_solutions,name='edit_solutions'),


    path('flutter_login',views.flutter_login,name='flutter_login'),
    path('user_reg',views.user_reg,name='user_reg'),
    path('user_view_tips',views.user_view_tips,name='user_view_tips'),
    path('user_view_suggestions',views.user_view_suggestions,name='user_view_suggestions'),
    path('user_send_feedback',views.user_send_feedback,name='user_send_feedback'),

    path('chatbot_response',views.chatbot_response,name='chatbot_response'),


    path('add_dataset',views.add_dataset,name='add_dataset'),
    path('expert_view_dataset',views.expert_view_dataset,name='expert_view_dataset'),
    path('delete_dataset/<id>',views.delete_dataset,name='delete_dataset'),



    path('get_forcast_data',views.get_forcast_data,name='get_forcast_data'),
    path('get_forcast_data1',views.get_forcast_data1,name='get_forcast_data1'),


]
