from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from . import views
from .views import Home,Signup,logout,Cart,Checkout,OrderView
from .middlewares import LoginCheckMiddleware

from .views.home import CommentUpdateView, CommentDeleteView, ProductDetailView

schema_views = get_swagger_view(title='Online Shopping API')
router = DefaultRouter()
router.register(r"categories",views.CategoryViewSet,"categories")
router.register(r"comments",views.CommentViewSet,"comments")
router.register(r"orders",views.OrderViewSet,"orders")
router.register(r"products",views.ProductViewSet,"products")
router.register(r"customers",views.CustomerViewSet,"customers")

urlpatterns = [
    path('',Home.as_view(), name='home'),
    path('api/', include(router.urls)),

    path('signup',Signup.as_view(), name='signup'),
    #path('login',Login.as_view(), name='login'),
    path('logout',LoginCheckMiddleware(logout), name='logout'),
    path('cart',LoginCheckMiddleware(Cart.as_view()), name='cart'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('checkout',LoginCheckMiddleware(Checkout.as_view()), name='checkout'),
    path('order',LoginCheckMiddleware(OrderView.as_view()), name='order'),
    # path('create/<str:content_type>/<int:object_id>/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
