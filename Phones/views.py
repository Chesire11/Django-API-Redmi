from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Redmi, RedmiVariant
from django.http import JsonResponse

# Create your views here.
def index(request):
    return HttpResponse("Smartphones designed for you!")

def redmi_list(request):
    redmi_list = Redmi.objects.all()
    context = {
        'redmi_list': redmi_list,
    }
    return render(request, 'Phones/redmi_list.html', context)

def redmi_detail(request, redmi_id):
    redmi = get_object_or_404(Redmi, id=redmi_id)
    variants = RedmiVariant.objects.filter(redmi=redmi)
    print(f'Found {variants.count()} variants for {redmi.name}')
    return render(request, 'Phones/redmi_detail.html', {'redmi': redmi, 'variants': variants})


def redmi_with_variants(request):
    redmi_products = Redmi.objects.prefetch_related('variants').all()

    result = []
    for redmi in redmi_products:
        variants = redmi.variants.all()
        variant_list = [
            {
                'sku': variant.sku,
                'name': variant.name,
                'price': variant.price,
                'details': variant.details
            }
            for variant in variants
        ]
        result.append({
            'id': redmi.id,
            'name': redmi.name,
            'image': request.build_absolute_uri(redmi.image.url),  # Full URL for the image
            'variants': variant_list
        })

    return JsonResponse(result, safe=False)
