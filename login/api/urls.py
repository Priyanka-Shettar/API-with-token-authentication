from django.conf.urls import url
from django.urls import path
from rest_framework import routers
from .views import StudentViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register('students', StudentViewSet)
#router.register(r'universities', UniversityViewSet)

urlpatterns = router.urls
