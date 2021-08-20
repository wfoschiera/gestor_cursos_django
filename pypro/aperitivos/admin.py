from django.contrib.admin import ModelAdmin, register

from pypro.aperitivos.models import Video


@register(Video)
class VideoAdmin(ModelAdmin):
    list_display = ("titulo", "slug", "creation", "vimeo_id")
    ordering = ("creation",)
    prepopulated_fields = {"slug": ("titulo",)}  # aceita varios campos para criar a slug, por isso uma tupla
