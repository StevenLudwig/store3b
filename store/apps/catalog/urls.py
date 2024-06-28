from rest_framework.routers import DefaultRouter
from .views import ProductModelViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'products', ProductModelViewSet, basename='catalog')
urlpatterns = router.urls
