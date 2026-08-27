from django.contrib import admin
from django.utils.html import format_html
from .models import HeroVideo, VerifiedClient, ReelShowcase, TransformationClient, SuccessStory
from .models import Testimonial


@admin.register(HeroVideo)
class HeroVideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_active', 'uploaded_at')
    list_filter = ('is_active',)


@admin.register(VerifiedClient)
class VerifiedClientAdmin(admin.ModelAdmin):
    list_display = ('avatar_preview', 'name', 'followers_count', 'order', 'is_active')
    list_editable = ('order', 'is_active')

    def avatar_preview(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" style="height:40px;border-radius:50%;">', obj.avatar.url)
        return "—"
    avatar_preview.short_description = "الصورة"


@admin.register(ReelShowcase)
class ReelShowcaseAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'order', 'is_active')
    list_editable = ('order', 'is_active')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:60px;border-radius:8px;">', obj.image.url)
        return "—"
    image_preview.short_description = "الصورة"


@admin.register(TransformationClient)
class TransformationClientAdmin(admin.ModelAdmin):
    list_display = ('caption', 'order', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(SuccessStory)
class SuccessStoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'youtube_url', 'order', 'is_active')
    list_editable = ('order', 'is_active')



@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_active')
    list_editable = ('order', 'is_active')