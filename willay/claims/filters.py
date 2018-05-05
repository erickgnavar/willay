import django_filters

from .models import Claim


class ClaimFilter(django_filters.FilterSet):

    class Meta:
        model = Claim
        fields = (
            'category',
        )
