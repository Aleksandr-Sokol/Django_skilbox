from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='API')


urlpatterns = [
    path("admin/", admin.site.urls),
    path("docs/", schema_view),
    path('api/v1/', include('product.urls')),
]
