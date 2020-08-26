from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import URLform
from .models import BigUrl
# Create your views here.
def getUrl(request):
    if request.method == 'POST':
        form = URLform(request.POST)
        if form.is_valid:
            temp_obj = form.save(commit=False)
            temp_obj.save()
            url = '<a href="http://127.0.0.1:8000/{}">127.0.0.1:8000/{}'.format(str(temp_obj.id),str(temp_obj.id))
            return HttpResponse(url)    
    else:
        form = URLform()
        return render(request, 'url/shortner.html', {'form':form})        
        
def handleUrl(request, pk, *args,**kwargs):
    temp = getattr(BigUrl.objects.get(id=pk),'inputurl')
    return redirect(str(temp))