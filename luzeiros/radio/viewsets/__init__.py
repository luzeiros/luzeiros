from rest_framework import routers
from .program import ProgramViewSet


router = routers.SimpleRouter(trailing_slash=False)

router.register('programs', ProgramViewSet)
