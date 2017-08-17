from django.db import models

# upload handlers/paths for maker page

def stgdUpload_handler(show, filename):
    stgd_path = "{0}/{0}_{1}/{2}".format(show.tree, 'stgd', filename)
    return stgd_path


def stgdImgUpload_handler(show, filename):
    stgdImg_path = "{0}/{0}_{1}/{2}".format(show.tree, 'stgd_img', filename)
    return stgdImg_path


def binderUpload_handler(show, filename):
    binder_path = "{0}/{0}_{1}/{2}".format(show.tree, 'binder', filename)
    return binder_path


def binderImgUpload_handler(show, filename):
    binderImg_path = "{0}/{0}_{1}/{2}".format(show.tree, 'binder_img', filename)
    return binderImg_path


def splashUpload_handler(show, filename):
    splash_path = "{0}/{0}_{1}/{2}".format(show.tree, 'splash', filename)
    return splash_path


def text_upload_handler(instance, filename):
    text_path = "{0}/{0}_{1}/{2}".format(instance.show.tree, 'text', filename)
    return text_path


def image_upload_handler(instance, filename):
    img_path = "{0}/{0}_{1}/{2}".format(instance.show.tree, 'images', filename)
    return img_path


def pdf_upload_handler(instance, filename):
    pdf_path = "{0}/{0}_{1}/{2}".format(instance.show.tree, 'text', filename)
    return pdf_path


def sound_upload_handler(instance, filename):
    sound_path = "{0}/{0}_{1}/{2}".format(instance.show.tree, 'sound', filename)
    return sound_path


def video_upload_handler(instance, filename):
    video_path = "{0}/{0}_{1}/{2}".format(instance.show.tree, 'video', filename)
    return video_path


def misc_upload_handler(instance, filename):
    return "{0}/{0}_{1}/{2}".format(instance.show.tree, 'misc', filename)

# show model. lose prod_date field
class Show(models.Model):
    name = models.CharField(max_length=100)
    tree = models.CharField(max_length=100)
    house = models.CharField(max_length=100, blank=True, null=True)
    prod_date = models.CharField(max_length=100, blank=True, null=True)
    run_date = models.CharField(max_length=100, blank=True, null=True)
    director = models.CharField(max_length=100, blank=True, null=True)
    wright = models.CharField(max_length=100, blank=True, null=True)
    binder = models.FileField(blank=True, null=True, help_text="PDF", upload_to=binderUpload_handler)
    binder_img = models.FileField(blank=True, null=True, upload_to=binderImgUpload_handler)
    stgd = models.FileField(blank=True, null=True, upload_to=stgdUpload_handler)
    stgd_img = models.FileField(blank=True, null=True, upload_to=stgdImgUpload_handler)
    splash = models.FileField(blank=True, null=True, upload_to=splashUpload_handler)

    def __str__(self):
        return "{}'s {} (listed as {})".format(self.wright, self.name, self.tree)

# classes for all files types for upload handlers
class TextFile(models.Model):
    file = models.FileField(upload_to=text_upload_handler)
    show = models.ForeignKey(Show, related_name= 'text')

    def __str__(self):
        return "this is a {} file associated with {} show".format('text file', self.show.tree)


class ImageFile(models.Model):
    file = models.FileField(upload_to=image_upload_handler)
    show = models.ForeignKey(Show, related_name='image')

    def __str__(self):
        return "this is an {} file associated with {} show".format('image file', self.show.tree)


class PDFFile(models.Model):
    file = models.FileField(upload_to=pdf_upload_handler)
    show = models.ForeignKey(Show, related_name='pdf')

    def __str__(self):
        return "this is a {} file associated with {} show".format('PDF file', self.show.tree)


class MiscFile(models.Model):
    file = models.FileField(upload_to=misc_upload_handler)
    show = models.ForeignKey(Show, related_name='misc')

    def __str__(self):
        return "this is a {} file associated with {} show".format('misc file', self.show.tree)


class VideoFile(models.Model):
    file = models.FileField(upload_to=video_upload_handler)
    show = models.ForeignKey(Show, related_name='video')

    def __str__(self):
        return "this is a {} file associated with {} show".format('video file', self.show.tree)


class SoundFile(models.Model):
    file = models.FileField(upload_to=sound_upload_handler)
    show = models.ForeignKey(Show)

    def __str__(self):
        return "this is a {} file associated with {} show".format('sound file', self.show.tree)
