from django.contrib import admin
from .models import Show, SoundFile, VideoFile, MiscFile, ImageFile, TextFile, PDFFile
# Register your models here.
admin.site.register(Show)
admin.site.register(SoundFile)
admin.site.register(VideoFile)
admin.site.register(MiscFile)
admin.site.register(ImageFile)
admin.site.register(TextFile)
admin.site.register(PDFFile)