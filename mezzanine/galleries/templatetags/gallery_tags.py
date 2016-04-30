import random
from django import template

register = template.Library()

@register.filter(name='gallery_highlight')
def gallery_highlight(value):
    images = value.gallery.images

    q = images.filter(description__contains='*').order_by('?')

    if(q.count() > 0):
        return q[0]
    elif(images.count() > 0):
        return images.order_by('?')[0]
    else:
        child_gallery = random.choice(
            [child for child in value.children.all() if child.gallery]
        )
        if(child_gallery):
            return gallery_highlight(child_gallery)
        else:
            return ''
