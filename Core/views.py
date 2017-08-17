from django.shortcuts import render, redirect
from .models import Show, SoundFile, VideoFile, MiscFile, ImageFile, TextFile, PDFFile


# from .forms import

# sets up context dict for index. How the db iterates through show objects

def index(request):
    shows = Show.objects.all().order_by( '-id' )
    return render( request, 'core/index.html', {'shows': Show.objects.all()} )


# POST method for use with forms
def maker(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        # file fields fro maker page. Maybe lose prod_date field
        show = Show()
        show.name = request.POST.get( 'name' )
        show.tree = request.POST.get( 'tree' )
        show.house = request.POST.get( 'house' )
        show.prod_date = request.POST.get( 'prod_date' )
        show.run_date = request.POST.get( 'run_date' )
        show.director = request.POST.get( 'director' )
        show.wright = request.POST.get( 'wright' )
        show.binder = request.FILES.get( 'binder', None )
        show.binder_img = request.FILES.get('binder_img', None)
        show.stgd = request.FILES.get( 'stgd', None )
        show.stgd_img = request.FILES.get('stgd_img', None)
        show.splash = request.FILES.get( 'splash', None )
        show.save()
        # [] included because it takes more than one file.
        files = request.FILES.getlist('bulk[]', None)
        # sorts bulk by file extensions.
        if files:
            for x in files:
                ext = x.name.split('.')[-1]
                if ext.lower() == 'pdf':
                    PDFFile.objects.create(file=x, show=show)
                elif ext.lower() in ['png', 'jpg', 'jpeg', 'gif', 'dmg']:
                    ImageFile.objects.create(file=x, show=show)
                elif ext.lower() in ['txt', 'doc', 'docx']:
                    TextFile.objects.create(file=x, show=show)
                elif ext.lower() in ['wav', 'mp3', 'wma']:
                    SoundFile.objects.create(file=x, show=show)
                elif ext.lower() in ['avi', 'flv', 'mov','wmv' ]:
                    VideoFile.objects.create(file=x, show=show)
                else:
                    MiscFile.objects.create(file=x, show=show)
                    # TODO: make success message
        # redirects to base url
        return redirect('/')
    return render(request, 'core/maker.html', {})
