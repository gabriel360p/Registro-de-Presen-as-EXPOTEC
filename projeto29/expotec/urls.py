from django.urls import path
from . import views

app_name = 'expotec'

urlpatterns=[
	path('index/',views.viewindex,name="viewindex"),
	path('',views.viewindex,name="viewindex"),
	path('insere/',views.viewinsere,name="viewinsere"),
	path('registra/',views.viewregistra,name="viewregistra"),
	path('presencas/',views.viewlistapresencas,name="viewlistapresencas"),
	path('inseridos/',views.viewinseridos,name="viewinseridos"),


	path('definsere/',views.definsere,name="definsere"),
	path('defpresenca/',views.defpresenca,name="defpresenca"),
	path('defbusca/',views.defbusca,name="defbusca"),
	

]

