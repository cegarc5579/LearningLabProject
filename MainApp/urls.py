from django.urls import path 


from . import views


app_name = 'MainApp'

urlpatterns = [
    path("", views.index, name="index"),
    path("topics/", views.topics, name="topics"),
    path('topics/<int:topic_id>/', views.topic,name='topic'), #the forward slash is where it will show up on the bar when you click on the link 
    path('new_topic/', views.new_topic, name='new_topic'),
    path("new_entry/<int:topic_id>/",views.new_entry,name='new_entry'),
    path('edit_entry/<int:entry_id/', views.edit_entry, name="edit_entry"),
]