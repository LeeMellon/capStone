from django.db import models


def bulkUpload_handler(media, filename):
    bulk_path = "{0}/{0}_{1}/{2}".format( media.show.tree,media.type, filename)
    return bulk_path
def stgdUpload_handler(show, filename):
    stgd_path = "{0}/{0}_{1}/{2}".format( show.tree, 'stgd', filename)
    return stgd_path
def binderUpload_handler(show, filename):
    binder_path = "{0}/{0}_{1}/{2}".format(show.tree,'binder', filename)
    return binder_path
def splashUpload_handler(show, filename):
    splash_path = "{0}/{0}_{1}/{2}".format(show.tree, 'splash', filename)
    return splash_path


class Show(models.Model):
    name = models.CharField(max_length=100)
    tree = models.CharField(max_length=100)
    house = models.CharField(max_length=100, blank=True, null=True)
    prod_date = models.CharField(max_length=100, blank = True, null=True)
    run_date = models.CharField(max_length=100, blank = True, null=True)
    director = models.CharField(max_length=100, blank=True, null=True)
    wright = models.CharField(max_length=100, blank=True, null=True)
    binder = models.FileField(blank=True, null=True, help_text="PDF", upload_to=binderUpload_handler)
    stgd = models.FileField(blank=True, null=True, upload_to=stgdUpload_handler)
    splash = models.ImageField(blank=True, null=True, upload_to=splashUpload_handler)


    def __str__(self):
        return"{}'s {} (listed as {})".format(self.wright, self.name, self.tree)


class Media(models.Model):
    UPLOAD_TYPES = (
        ('text', 'text'),
        ('video', 'video'),
        ('audio', 'audio'),
        ('roller', 'roller')

    )

    name = models.CharField(max_length=255 )
    show = models.ForeignKey(Show, related_name='medias')
    type = models.CharField(max_length=100, choices=UPLOAD_TYPES)

    def sort(self):
        for i in target:
            if i in ('/.txt', '/.doc', '/.pdf', '/.docx'):
                self.type = 'text'
            elif i == '/.jpeg' or '/.jpg' or '/.png' or '/.gif' or '/.dng':
                self.type = 'roller'
            elif i == '/.mp3' or '/.wav':
                self.type = 'audio'
            elif i == '/.avi' or '/.mov' or '/.flv' or '/.mp4' or '/.wmv':
                self.type = 'video'
            else:
                return "file not supported"


    def __str__(self):
        return "{} is a {} file associated with {} show".format(self.name, self.type, self.show)

