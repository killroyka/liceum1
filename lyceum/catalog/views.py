from django.db.models import Avg, Count
from django.shortcuts import render, redirect
from catalog.models import Item, Category
from django.shortcuts import get_object_or_404
from catalog.forms import FeedbackForm
from raitng.models import Raiting


def item_list(request):
    categories = Category.objects.get_items_group_by_categories()
    return render(request, "catalog/list.html", {'categories': categories})





def item_detail(request, id):
    raitings = Raiting.objects.filter(item__id=id).only("star")
    item = get_object_or_404(Item, pk=id, is_published=True)
    form = FeedbackForm(request.POST or None)
    stars = Raiting.objects.filter(item=item, star__in=[1, 2, 3, 4, 5]).aggregate(Avg('star'), Count('star'))

    if form.is_valid():
        raiting = raitings.get(user__id=request.user.id)
        if raiting:
            raiting.star = form.cleaned_data["star"]
            raiting.save(update_fields=['star'])
        else:
            Raiting.objects.create(
                star=form.cleaned_data["star"],
                item=item,
                user=request.user
            )
        return redirect(f"/catalog/{id}/")
    context = {"item": item, "stars": stars, "form": form}
    return render(request, "catalog/detail.html", context)
