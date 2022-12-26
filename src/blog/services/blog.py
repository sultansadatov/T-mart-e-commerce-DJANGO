from unicodedata import category
from django.db.models import QuerySet, Q, F, Count
from blog.models import Blog, Tags, Comments
from product.models import Category


def list_blog() -> QuerySet:
    return Blog.objects.all()


def list_tag() -> QuerySet:
    return Tags.objects.all()


def get_blog(id) -> QuerySet:
    return Blog.objects.get(id=id)



def list_comment() -> QuerySet:
    return Comments.objects.all()


# Get similar blogs
def get_similar_blog(blog_id: int, category_id: int) -> QuerySet:
    return Blog.objects.filter(
        Q(category_id = category_id) & ~Q(id = blog_id)
    )



# Get category of blog
def get_category_blog(id: int) -> str:
    return Blog.objects.filter(
        id = id
    ).first().category_id



# Get blog by data
def get_blog(name: str) -> QuerySet:
    return Blog.objects.filter(
        Q(title__icontains=name) | Q(header__icontains=name)
    )


# Get tags of blog
def get_tags(id: int) -> str:
    return Tags.objects.filter(
        id__in = (Blog.objects.filter(id = id).values(
            'tag_id',
        ))
    )


# The most popular 5 blog
def popular_tag():
    return Blog.objects.all().annotate(
        Count('tag_id')
    ).order_by(
        '-tag_id__count'
    )[:3]


# Get most recent 3 blogs
def recent_blogs() -> QuerySet:
    return Blog.objects.order_by('-created_at')[:3]

