from django.http.response import JsonResponse
from api.models import Product
from api.models import Category



def product_list(request):
    products=Product.objects.all()
    products_json=[product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)

def product_detail(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(product.to_json())

def category_list(request):
    categories=Category.objects.all()
    categories_json = [ category.to_json_c() for category in categories]
    return JsonResponse(categories_json, safe=False)

def category_detail(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(category.to_json_c())

def  category_products (request, id):
    products=Product.objects.all()
    products_json=[]
    for product in products:
        if product.category_id==id:
            products_json.append(product.to_json())
    return JsonResponse(products_json, safe=False)