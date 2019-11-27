import os
from datetime import timedelta


JSON_API_FORMAT_FIELD_NAMES = 'dasherize'

JSON_API_FORMAT_TYPES = 'dasherize'

JSON_API_PLURALIZE_TYPES = False

REST_FRAMEWORK = {
    'PAGE_SIZE': 10,

    'DEFAULT_PAGINATION_CLASS': 'rest_framework_json_api.pagination.JsonApiPageNumberPagination',

    'EXCEPTION_HANDLER': 'rest_framework_json_api.exceptions.exception_handler',

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],

    'DEFAULT_PARSER_CLASSES': (
        'rest_framework_json_api.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ),

    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework_json_api.renderers.JSONRenderer',
    ),

    'DEFAULT_METADATA_CLASS': 'rest_framework_json_api.metadata.JSONAPIMetadata',

    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework_json_api.filters.QueryParameterValidationFilter',
        'rest_framework_json_api.filters.OrderingFilter',
        'rest_framework_json_api.django_filters.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
    ),

    'SEARCH_PARAM': 'filter[search]',

    'TEST_REQUEST_RENDERER_CLASSES': (
        'rest_framework_json_api.renderers.JSONRenderer',
    ),

    'TEST_REQUEST_DEFAULT_FORMAT': 'vnd.api+json'
}

