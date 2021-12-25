from django.urls import path
from . import views

urlpatterns = [
    

    # testing
    path('all_chart_view/', views.all_charts_view, name='all_chart_view'),
    path('chart_detail_view/<int:pk>', views.chart_detail_view, name='chart_detail_view'),
    path('chart_create_view/', views.chart_create_view, name='chart_create_view'),
    path('chart_delete/<int:pk>', views.chart_delete, name='chart_delete'),
    path('chart_data_delete/<int:pk>', views.chart_data_delete, name='chart_data_delete')


]