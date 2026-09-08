from django.db import models


class HeroVideo(models.Model):
    video_url = models.URLField(verbose_name="رابط الفيديو (يوتيوب)")
    is_active = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"فيديو رئيسي — {self.uploaded_at:%Y-%m-%d}"

    def video_id(self):
        """يستخرج معرّف الفيديو من أي صيغة رابط يوتيوب شائعة"""
        url = self.video_url
        if 'embed/' in url:
            return url.split('embed/')[-1].split('?')[0]
        if 'youtu.be/' in url:
            return url.split('youtu.be/')[-1].split('?')[0]
        if 'v=' in url:
            return url.split('v=')[-1].split('&')[0]
        return ''

    def thumbnail_url(self):
        vid = self.video_id()
        return f"https://img.youtube.com/vi/{vid}/hqdefault.jpg" if vid else ''


      

class VerifiedClient(models.Model):
    """القسم الثاني: موثّقون من قبل"""
    name = models.CharField(max_length=100, verbose_name="اسم العميل")
    avatar = models.ImageField(upload_to='verified_clients/', verbose_name="صورة العميل")
    followers_count = models.CharField(max_length=20, verbose_name="عدد المتابعين", help_text="مثال: 440K أو 3.2M")
    order = models.PositiveIntegerField(default=0, verbose_name="الترتيب")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class ReelShowcase(models.Model):
    image = models.ImageField(upload_to='reels/')
    views_label = models.CharField(max_length=20, blank=True, verbose_name="عدد المشاهدات (مثال: 7.4M)")
    row = models.PositiveSmallIntegerField(choices=[(1, 'الصف الأول'), (2, 'الصف الثاني'), (3, 'الصف الثالث')], default=1, verbose_name="الصف")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"ريلز #{self.id} — صف {self.row}"



class TransformationClient(models.Model):
    """القسم الرابع: قبل / بعد"""
    before_image = models.ImageField(upload_to='transformations/before/', verbose_name="صورة قبل")
    after_image = models.ImageField(upload_to='transformations/after/', verbose_name="صورة بعد")
    caption = models.CharField(max_length=150, verbose_name="الجملة أسفل الصورتين")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.caption


class SuccessStory(models.Model):
    """القسم الخامس: قصص نجاح (فيديو يوتيوب + عنوان)"""
    title = models.CharField(max_length=150, verbose_name="العنوان")
    youtube_url = models.URLField(verbose_name="رابط فيديو يوتيوب")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    def youtube_id(self):
        """يستخرج معرّف الفيديو من الرابط تلقائياً (يدعم صيغتين شائعتين)"""
        url = self.youtube_url
        if 'youtu.be/' in url:
            return url.split('youtu.be/')[-1].split('?')[0]
        if 'v=' in url:
            return url.split('v=')[-1].split('&')[0]
        return ''

    def thumbnail_url(self):
        vid = self.youtube_id()
        return f"https://img.youtube.com/vi/{vid}/hqdefault.jpg" if vid else ''




class Testimonial(models.Model):
    """قسم: ماذا قال عنّا المبدعين — سكرين شوت فقط"""
    screenshot = models.ImageField(upload_to='testimonials/', verbose_name="صورة الرأي (سكرين شوت)")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"رأي #{self.id}"   