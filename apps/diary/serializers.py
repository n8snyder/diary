from rest_framework import serializers

from apps.diary.models import Page


class PageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Page
        fields = "__all__"
        read_only_fields = ["date_created", "last_updated"]
        extra_kwargs = {
            "url": {"lookup_field": "number",},
        }

    id = serializers.ReadOnlyField()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    text = serializers.CharField(
        label="",
        style={"autofocus": True, "rows": 10, "base_template": "textarea.html"},
    )
    number = serializers.ReadOnlyField()
    date_created = serializers.SerializerMethodField()

    def get_date_created(self, obj):
        return obj.date_created.date()
