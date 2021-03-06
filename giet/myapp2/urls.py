from django.urls import path
from myapp2 import views
urlpatterns = [
	path('homeurl/',views.home,name="home"),
	path('index/',views.index , name= 'index'),
	path('student',views.student, name = 'student'),
	path('<int:val>',views.value,name= 'value'),#localhost:myapp2/67
	path("table/<int:v>",views.table, name= 'table'),
	path('sample/',views.sample),
	path('register/',views.register,name='register'),
	path('disply/',views.disply_details, name='details'),
	path('update/<int:id>',views.update_details,name= 'update'),
	path('delete/<int:id>',views.delete, name= 'delete'),
	path('signup/',views.signup,name="signup"),
	path('userregistration/',views.registration),
	path('showdata/',views.showdata,name='showdata')
]