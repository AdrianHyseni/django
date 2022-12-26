from django.urls import path
from . import views
urlpatterns = [
    path("s/<int:int>", views.sqrt_url),
    path("",views.index),
    path("gjeo",views.gjeo_page),
    #path("<str:text>",views.text_page),
    path("numer/<int:int>",views.int_page),
    path('redirect/<str:str>', views.redirect_page),
    path('sfida/<int:month_int>',views.sfida_mujore_int),
    path('sfida/<str:month>',views.sfida_mujore, name='sfida-mujore'),
    path('sfida/',views.sfida),
    path('rendered/',views.rendered_view),
    path('sfida1/<str:text>',views.sfida_rendered_view,name='sfida-1'),
    path('sfida1/', views.faqa_kryesore_sfides)
]