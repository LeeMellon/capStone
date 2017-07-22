from django.shortcuts import render, redirect
from .models import Media, Show


# from .forms import


def index(request):
    shows = Show.objects.all().order_by( '-id' )
    art = Media.objects.filter( type='RLR', show__tree='GOC' )
    return render( request, 'core/index.html', {'shows': shows} )


def maker(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)

        show = Show()
        show.name = request.POST.get( 'name' )
        show.tree = request.POST.get( 'tree' )
        show.house = request.POST.get( 'house' )
        show.prod_date = request.POST.get( 'prod_date' )
        show.run_date = request.POST.get( 'run_date' )
        show.director = request.POST.get( 'director' )
        show.wright = request.POST.get( 'wright' )
        show.binder = request.FILES.get( 'binder', None )
        show.stgd = request.FILES.get( 'stgd', None )
        show.splash = request.FILES.get( 'splash', None )
        show.medias.type = request.FILES.get( 'bulk', None)
        show.save()

        # TODO: make success message
        return redirect('/')
    return render( request, 'core/maker.html', {} )

