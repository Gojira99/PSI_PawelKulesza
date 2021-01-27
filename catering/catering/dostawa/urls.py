from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [

   path('Klient/', views.KlientLista.as_view(), name=views.KlientLista.name),
   path('Klient/<int:pk>', views.KlientSczegoly.as_view(),name=views.KlientSczegoly.name),

   path('Lokalizacja/', views.LokalizacjaLista.as_view(), name=views.LokalizacjaLista.name),
   path('Lokalizacja<int:pk>', views.LokalizacjaSczegoly.as_view(), name=views.LokalizacjaSczegoly.name),

   path('Zamowienie/', views.ZamowienieLista.as_view(), name=views.ZamowienieLista.name),
   path('Zamowienie/<int:pk>', views.ZamowienieSzczegoly.as_view(), name=views.ZamowienieSzczegoly.name),

   path('Catering_dietetyczny/', views.Catering_dietetycznyLista.as_view(), name=views.Catering_dietetycznyLista.name),
   path('Catering_dietetyczny/<int:pk>', views.Catering_dietetycznySzczegoly.as_view(), name=views.Catering_dietetycznySzczegoly.name),

   path('Menu/', views.MenuLista.as_view(), name=views.MenuLista.name),
   path('Menu/<int:pk>', views.MenuSczegoly.as_view(), name=views.MenuSczegoly.name),

   path('Platnosc/', views.PlatnoscLista.as_view(), name=views.PlatnoscLista.name),
   path('Platnosc/<int:pk>',views.PlatnoscSczegoly.as_view(), name=views.PlatnoscSczegoly.name),
   path('', views.ApiRoot.as_view(), name=views.ApiRoot.name)
   #                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       path('', views.ApiRoot.as_view(), name=views.ApiRoot.name)
]
