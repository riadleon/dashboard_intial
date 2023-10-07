from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('parsed-output/', views.parsed_output_view, name='parsed_output'),
    path('dirty-seo/', views.dirty_seo_view, name='dirty_seo'),
    path('move-to-cleanlist/', views.move_to_cleanlist, name='move_to_cleanlist'),
    path('cleanlist/', views.cleanlist_view, name='cleanlist')

]
