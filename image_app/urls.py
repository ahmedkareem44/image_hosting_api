from image_app import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'images', views.ImageViewSet, basename='image_view')
urlpatterns = router.urls

