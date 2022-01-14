from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Ititems(TimestampedModel):
    name = models.CharField(max_length=100, db_index=True,
                             validators=[
                                 MinLengthValidator(3),
                                 RegexValidator(r"[ㄱ-힣]", message="제품명(한글)을 입력해주세요."),
                             ])
    company = models.CharField(max_length=30)
    product_link = models.URLField(blank=True)
    content = models.TextField(max_length=200)
    picture = models.ImageField(blank=True)