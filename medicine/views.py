from django.http import Http404
from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render
from .models import Album


def index(request):
    all_albums =Album.objects.all()
#    template = loader.get_template('medicine/index.html')
    context = {
        'all_albums' : all_albums,
    }
    #return HttpResponse(template.render(context,request))
    return render (request,'medicine/index.html',context)
def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("album not exist")
    return render (request,'medicine/detail.html', {'album' : album })
    #return HttpResponse("<h2>Details for Album id: "+str(album_id)+"</h2>")
