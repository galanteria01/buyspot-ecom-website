from django.shortcuts import render
from django.db.models import Q
from items.models import Item

# Create your views here.

def search_result(request):
    if request.method == "GET":
        query = request.GET.get('q')

        submitbutton = request.GET.get('submit')
        if query is not None:
            lookups = Q(productTitle=query) | Q(about=query)

            results = Item.objects.filter(lookups).distinct()

            context = {"results":results,"submitbutton":submitbutton}

            return render(request,'search/search_result.html',context)
        else:
            return render(request,'search/search_result.html')
    else:
        return render(request,'search/search_result.html')