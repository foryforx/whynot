import datetime
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import loader
from django.http import Http404
from .models import Productdata,Wishlist

# Create your views here.
# def index(request):
#     try:
#         latest_sku_list = Productdata.objects.order_by('-created_date')[:5]
#         print(latest_sku_list)
#         context = {'latest_sku_list': latest_sku_list,}
#     except Productdata.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'productentity/index.html', context)

# def detail(request,sku_id):
#     product = get_object_or_404(Productdata, pk=sku_id)
#     return render(request, 'productentity/detail.html', {'product': product})

# def getsku(request,identifier):
#     return HttpResponse("you want sku of this identifier:%s" % identifier)

class IndexView(generic.ListView):
    template_name = 'productentity/index.html'
    context_object_name = 'latest_sku_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Productdata.objects.order_by('-created_date')[:5]

class DetailView(generic.DetailView):
    model = Productdata
    context_object_name = 'product'
    template_name = 'productentity/detail.html'
    
class GetskuView(generic.DetailView):
    model = Productdata
    context_object_name = 'product'
    template_name = 'productentity/detail.html'
    
    
def wishlist(request,identifier):
    product = get_object_or_404(Productdata, pk=identifier)
    
    try:
        email = request.POST.get('email', '')
        
    except (KeyError, email.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'productentity/detail.html', {
            'product': product,
            'error_message': "Please enter valid email id.",
        })
    else:
        try:
            wishlist = product.wishlist_set.get(email=email)
        except Wishlist.DoesNotExist:
            wishlist = None
        print(wishlist)
        if wishlist is None :
            print("Wishlist created")
            wishlist = Wishlist(productdata = product, email = email)
        # wishlist.email = email
        # wishlist.created_date = datetime.datetime.now()
        wishlist.updated_date = datetime.datetime.now()
        wishlist.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('productentity:detail', args=(product.skuid,)))