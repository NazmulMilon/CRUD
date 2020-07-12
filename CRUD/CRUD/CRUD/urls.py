
from django.contrib import admin
from django.urls import path
from Crudapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.insert_view),
    path('show/', views.show_view),
    path('delete/<int:id>', views.delete_view),
    path('update/<int:id>', views.update_view)
]
