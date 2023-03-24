from django.urls import include, path
from rest_framework import routers
from students import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'teacher', views.TeacherViewSet)
router.register(r'subject', views.SubjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
