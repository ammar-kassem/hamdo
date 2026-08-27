from django.shortcuts import render
from .models import (
    HeroVideo, VerifiedClient, ReelShowcase,
    TransformationClient, SuccessStory, Testimonial,
)


def home(request):
    context = {
        'hero_video': HeroVideo.objects.filter(is_active=True).first(),
        'verified_clients': VerifiedClient.objects.filter(is_active=True),
        'reels_row1': ReelShowcase.objects.filter(is_active=True, row=1),
        'reels_row2': ReelShowcase.objects.filter(is_active=True, row=2),
        'reels_row3': ReelShowcase.objects.filter(is_active=True, row=3),
        'transformations': TransformationClient.objects.filter(is_active=True),
        'success_stories': SuccessStory.objects.filter(is_active=True),
        'testimonials': Testimonial.objects.filter(is_active=True),
    }
    return render(request, 'landing/index.html', context)