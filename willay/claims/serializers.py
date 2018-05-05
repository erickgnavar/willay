from django.core.serializers import get_serializer
from django.urls import reverse

GeoJSONSerializer = get_serializer('geojson')


class Serializer(GeoJSONSerializer):
    """
    Serializer used for Claim representation
    """

    def get_dump_object(self, obj):
        data = super().get_dump_object(obj)
        data['properties'].update({
            'id': obj.id,
            'category_name': obj.category.name,
            'url': reverse('claims:claim-detail', kwargs={'id': obj.id}),
        })
        return data
