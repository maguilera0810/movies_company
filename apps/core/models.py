from django.db import models
from resources.enums.enums import StatusEnum

STATUS_LIST = (
    (StatusEnum.draft.value, StatusEnum.draft.value),
    (StatusEnum.enabled.value, StatusEnum.enabled.value),
)


class DatedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class StatusModel(models.Model):
    status = models.CharField(
        max_length=10, choices=STATUS_LIST, default=StatusEnum.draft.value)

    class Meta:
        abstract = True
