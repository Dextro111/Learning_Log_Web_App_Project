"""Define URL ptterms for learning_Logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    #   Home Page.
    path('', views.index, name='index'),

    #   Show All Topics
    path('topics/', views.topics, name='topics'),

    #   Detail page for a single Topic
    path('topics/<int:topic_id>/', views.topic, name="topic"),

    #   Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),

    #   Page for adding new Entry
    path('new_entry/<int:topic_id>', views.new_entry, name="new_entry"),

    #   Page For Editing An Entry
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
]