from rest_framework.routers import DefaultRouter

from seller_products import views

router = DefaultRouter()
router.register(r'seller-produts', views.SellerProdutViewSet)

urlpatterns = router.urls