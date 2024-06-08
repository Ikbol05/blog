from django.urls import path, include
from .views import PostListCreate, PostDetail, CommentListCreate, like_article
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),

    path('api/v1/post-create/', PostListCreate.as_view(), name='article-list-create'),
    path('api/v1/detail/<int:pk>/', PostDetail.as_view(), name='article-detail'),
    path('api/v1/like/<int:pk>/like/', like_article, name='like-article'),
    path('api/v1/comments/', CommentListCreate.as_view(), name='comment-list-create'),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
