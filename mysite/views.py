#i have created this file - Arth
from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request, 'index.html')

def about(request):

    return HttpResponse('''<a href="https://www.youtube.com/c/CodeWithHarry">COde with harry bhaiiiii</a>''')

def myinfo(request):
    djtext = request.POST.get('text', 'default')
    print(djtext)
    removepunc = request.POST.get('removepunc', 'off')
    print('RP='+removepunc)
    capital = request.POST.get('capital', 'off')
    print('UC='+capital)

    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    analyzed = ''
    if removepunc == 'on':
        for i in djtext:
            if i not in punctuations :
                analyzed = analyzed + i
        params = {'purpose': 'remove punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyz.html', params)
    elif capital == 'on':
        for j in djtext:
            analyzed = analyzed + j.upper()
        params = {'purpose':'Upper Case', 'analyzed_text': analyzed}
        return render(request, 'analyz.html', params)
    else:
        return HttpResponse("Error")


def contact(request):
    return render(request, 'contact_us.html')

def artical(request):
    return render(request, 'artical.html')
