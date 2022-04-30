from django.db.models import Avg, Count
from django.shortcuts import redirect
from catalog.models import Item, Category, Gallery
from django.shortcuts import get_object_or_404
from catalog.forms import FeedbackForm
from raitng.models import Raiting
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView


# def item_list(request):
#     categories = Category.objects.get_items_group_by_categories()
#     return render(request, "catalog/list.html", {'categories': categories})

# def item_detail(request, id):
#     raitings = Raiting.objects.filter(item__id=id).only("star")
#     item = get_object_or_404(Item, pk=id, is_published=True)
#     photos = Gallery.objects.filter(item_id=item.id)
#     form = FeedbackForm(request.POST or None)
#     stars = raitings.filter(item=item, star__in=[1, 2, 3, 4, 5]).aggregate(Avg('star'), Count('star'))
#     user_star = raitings.filter(user__id=request.user.id).first()
#     if form.is_valid():
#         if user_star:
#             user_star.star = form.cleaned_data["star"]
#             user_star.save(update_fields=['star'])
#         else:
#             Raiting.objects.create(
#                 star=form.cleaned_data["star"],
#                 item=item,
#                 user=request.user
#             )
#         return redirect(f"/catalog/{id}/")
#     context = {"item": item, "stars": stars, "form": form, "user_star": user_star, "photos": photos}
#     return render(request, "catalog/detail.html", context)


class ItemListView(TemplateView):
    template_name = "catalog/list.html"

    def get_context_data(self, **kwargs):
        categories = Category.objects.get_items_group_by_categories()
        return {'categories': categories}


class ItemDetailView(FormView):
    template_name = "catalog/detail.html"
    form_class = FeedbackForm

    def get_context_data(self, **kwargs):
        id = self.kwargs['id']
        item = get_object_or_404(Item, pk=id, is_published=True)
        raitings = Raiting.objects.filter(item__id=id).only("star")
        stars = raitings.filter(item=item, star__in=[1, 2, 3, 4, 5]).aggregate(Avg('star'), Count('star'))
        form = self.form_class()
        user_star = raitings.filter(user__id=self.request.user.id).first()
        photos = Gallery.objects.filter(item_id=item.id)
        context = {"item": item, "stars": stars, "form": form, "user_star": user_star, "photos": photos}

        return context

    def form_valid(self, form, **kwargs):
        id = self.kwargs['id']
        item = get_object_or_404(Item, pk=id, is_published=True)
        raitings = Raiting.objects.filter(item__id=id).only("star")
        user_star = raitings.filter(user__id=self.request.user.id).first()
        if user_star:
            user_star.star = form.cleaned_data["star"]
            user_star.save(update_fields=['star'])
        else:
            Raiting.objects.create(
                star=form.cleaned_data["star"],
                item=item,
                user=self.request.user
            )
        return redirect(f"/catalog/{id}/")
