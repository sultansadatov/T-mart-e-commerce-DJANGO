from django.urls import include, path


from api.views import (
    ProductListAPIView,
    ProductCreateAPIView,
    CategoryCreateAPIView,
    CategoryListAPIView,
    CategoryDeleteAPIView,
    CategoryUpdateAPIView
    
)

urlpatterns = [
    path("products", ProductListAPIView.as_view(), name="product_list_api"),
    path("categories", CategoryListAPIView.as_view(), name="category_list_api"),
    path("products/create/", ProductCreateAPIView.as_view(), name="product_create_api"),
    path("categories/create/", CategoryCreateAPIView.as_view(), name="category_create_api"),
    path('categories/delete/', CategoryDeleteAPIView.as_view(), name='category_delete'),
    path('categories/update/', CategoryUpdateAPIView.as_view(), name='category_upadate'),

]
