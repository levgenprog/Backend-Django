from products import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'product-images', views.ProductImageViewSet)
router.register(r'products', views.ProductViewSet)

urlpatterns = router.urls