from .models import Category
# add the function to the context processor options 
# under TEMPLATE makes it available to "ALL THE TEMPLATES" in the project
def menu_links(request):
    links = Category.objects.all()
    return dict(links = links)