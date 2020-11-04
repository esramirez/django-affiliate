from django.shortcuts import render
from .models import amazonAffiliate


# Create your views here.

def home(request):
    listing = amazonAffiliate.objects.order_by('-pub_date')[:5]
    for i in listing:
        print(">>>> ", i)
    output = ', '.join([q.product_link for q in listing])
    print (output)
    return render(request,'home.html', dict(
                            affiliate_links=amazonAffiliate.objects.all()[:5]
                            ))