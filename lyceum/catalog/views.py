from django.shortcuts import render, redirect
from catalog.models import Item, Category
from django.shortcuts import get_object_or_404
from django import forms
from raitng.models import Raiting


def item_list(request):
    categories = Category.objects.get_items_group_by_categories()
    return render(request, "catalog/list.html", {'categories': categories})


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Raiting
        fields = ("star",)


def item_detail(request, id):
    raitings = Raiting.objects.filter(item__id=id).only("star")
    if raitings:
        average_raiting = sum(list(map((lambda x: int(x.star)), raitings))) / raitings.count()
    else:
        average_raiting = 0
    item = get_object_or_404(Item, pk=id, is_published=True)
    form = FeedbackForm(request.POST or None)
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
    context = {"items": [item], "average_rating": average_raiting, "count": raitings.count(), "form": form}

    return render(request, "catalog/detail.html", context)
