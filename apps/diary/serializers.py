from rest_framework import serializers

from apps.diary.models import Page


class PageSerializer(serializers.HyperlinkedModelSerializer):
    number = serializers.Field()

    class Meta:
        model = Page
        fields = "__all__"
        read_only_fields = ["date_created", "last_updated"]
        extra_kwargs = {
            "url": {"lookup_field": "number",},
        }

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    text = serializers.CharField(
        label="",
        style={"autofocus": True, "rows": 10, "base_template": "textarea.html"},
    )
    number = serializers.ReadOnlyField()
