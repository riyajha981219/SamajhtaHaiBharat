from django import template
from ..models import Post

register=template.Library()
@register.filter
def count(postid):
    post=Post.objects.get(pk=postid)
    post.likes +=1
    try:
        post.save()
    except:
        return ValueError("Something went wrong")
    return post.likes