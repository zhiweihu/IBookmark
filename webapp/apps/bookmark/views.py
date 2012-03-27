from django.shortcuts import render_to_response
from django.template.context import RequestContext
from forms import BookmarkForm

def bookmark(request, template_name='bookmark/bookmark.html'):
    form = BookmarkForm()
    return render_to_response(template_name, RequestContext(request, {
        'form': form,
        }))


def my_bookmark(request, template_name='bookmark/my_bookmark.html'):
    form = BookmarkForm()
    return render_to_response(template_name, RequestContext(request, {
        'form': form,
        }))