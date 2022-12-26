from django.db.models import QuerySet, Avg, Q, Count
from product.models import  Product, Category, Reviews, Brand, Media






# all products
def list_products() -> QuerySet:
    return Product.objects.all()


def list_brands() -> QuerySet:
    return Brand.objects.all()


# Get product
def get_product(id) -> QuerySet:
    return Product.objects.get(id = id)

def get_brand(id) -> QuerySet:
    return Brand.objects.get(id = id)

# that returns products of the entered category
def get_productsby_category(category_id) -> QuerySet:
    return Product.objects.filter(category_id = category_id)


# that returns reviews of the entered product
def get_reviews(product_id) -> QuerySet:
    return Reviews.objects.filter(product_id = product_id)







# Get id of spesific product
def get_product_id_with_slug(slug) -> int:
    return Product.objects.get(slug = slug)


# Get image url
def get_product_image_url(id) -> QuerySet:
    return Media.objects.filter(product_id = id)

# Get category
def get_category() -> QuerySet:
    return  Reviews.objects.all().aggregate(
        Avg('rating')
    ).order_by('-rating__avg')[:5]

# Get colors of product
def get_color_of_product(id) -> QuerySet:
    return Product.objects.values_list('color__color', 'color__name').filter(id = id)

# The most popular 5 products tags
def get_most_popular_tags() -> QuerySet:
    return Product.objects.values_list("tag_id__name", flat=True).annotate(
        Count('tag_id')
    ).order_by(
        '-tag_id__count'
    )[:5]

# Get similar products
def get_simmilar_products(category_id) -> QuerySet:
    return Product.objects.filter(category_id = category_id).order_by()[:8]



# that sorts the product by price and date of addition
def sort_by_price_and_date() -> QuerySet:
    return Product.objects.all().order_by('price', 'added_date')

# Get product categories with at least 1 product
def get_categories() -> QuerySet:
    # return Products.objects.values('catregory_id').filter(products__categery_id__gte=1)
    query = Product.objects.values_list('category_id', flat=True).all()
    category = Category.objects.filter(Q(id__in =query))
    return category


# Find product by its name
def search_product(query) -> QuerySet:
    return Product.objects.filter(product_name__contains = query)

def get_popular_products() -> QuerySet:
    popular_prods = Product.objects.annotate(
        count = Count("reviews_id")
        ).order_by("-count")
    
    return popular_prods
