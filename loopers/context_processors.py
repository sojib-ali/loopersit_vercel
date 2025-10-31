from .models import Page


def extra_pages(request):
    pages = Page.objects.filter(link_on_footer=True)
    return {'extra_pages': pages}