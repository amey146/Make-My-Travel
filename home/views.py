from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from home.models import Flight, Home, Itinerary, ItineraryDay, Places

# Create your views here.

def index(request):
    ind = Home.objects.values()
    context = {
        'ind':ind
    }
    return render(request, 'index.html', context)

def details(request):
    # index to details mechanism
    if request.method == "POST":
        dtour = request.POST['dtour']
        srci = request.POST['dimg']
        request.session['sessiondest'] = dtour
        request.session['sessionsrci'] = srci
        
        # fetch itinerary mechanism
        itr = Itinerary.objects.get(Destination=request.session['sessiondest'])
        baseprice = itr.OfferPrice*1.5
        offerprice = itr.OfferPrice
        ditr = ItineraryDay.objects.filter(DestinationName=itr)
        days = ditr.count()

        # final context
        context = {
            'dtour' : dtour,
            'srci': srci,
            'days':days,
            'baseprice':baseprice,
            'offerprice':offerprice,
            'ditr':ditr
            }
        return render(request, 'details.html', context)


def flights(request):
    src = None
    if 'sessionsrc' not in request.session:
        src = 'Mumbai'
        request.session['sessionsrc'] = src

    else:
        try:
            request.session['sessionsrc'] = request.POST['src']
            request.session['sessiondest'] = request.POST['dstn']
            src = request.session['sessionsrc']
        except:
            src = 'Mumbai'
        
    dstn = request.session['sessiondest']
    flight = Flight.objects.filter(Source__iexact=src, Destination__iexact=dstn).order_by('eFare').values()
    place = Places.objects.all()
    context = {
        'src':src,
        'dstn':dstn,
        'place':place,
        'flight':flight
    }
    return render(request, 'flights.html', context)

def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')
def test(request):
    return render(request, 'test.html')
def ticket(request):
    return render(request, 'ticket.html')
def fbooking(request):
    return render(request, 'fbooking.html')

@csrf_exempt
def contact(request):
    finals = ''
    try:
        em = request.POST['email']
        ms = request.POST['message']
        finals += em+' : '+ms
    except:
        pass
    context = {
        'dtour':finals
    }
    return render(request, 'contact.html', context)

def s1(request, sr1):
    return HttpResponse(sr1)



