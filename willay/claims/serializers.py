from django.core.serializers import get_serializer
from django.urls import reverse

GeoJSONSerializer = get_serializer("geojson")


class Serializer(GeoJSONSerializer):
    """
    Serializer used for Claim representation
    """

    def get_dump_object(self, obj):
        data = super().get_dump_object(obj)
        data["properties"].update(
            {
                "id": obj.id,
                "category_name": obj.category.name,
                "url": reverse("claims:claim-detail", kwargs={"id": obj.id}),
                "marker_icon": self.category_marker_icon(obj.category),
            }
        )
        return data

    def category_marker_icon(self, category):
        if category.marker_icon.name:
            return category.marker_icon.url
        else:
            return "/static/vendor/leaflet/images/marker-icon.png"
