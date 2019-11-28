"""
luzeiros URL Configuration
https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt import views as jwt_views
from django.views.i18n import JavaScriptCatalog

api_schema_docs = get_swagger_view(title='Luzeiros API')

js_info_dict = {
    'packages': ('recurrence', ),
}

urlpatterns = [
    # Application urls
    path('', include('luzeiros.core.urls')),
    path('', include('luzeiros.blog.urls')),
    path('', include('luzeiros.radio.urls')),

    # Administrative dashboard
    path('admin/', admin.site.urls),

    # Documentation endpoint
    path('documentation/', api_schema_docs),

    # Application urls
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),

    # Static asset
    # jsi18n can be anything you like here
    path('jsi18n/', JavaScriptCatalog.as_view(), js_info_dict),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
