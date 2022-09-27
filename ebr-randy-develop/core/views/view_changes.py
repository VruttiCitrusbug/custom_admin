# -*- coding: utf-8 -*-
"""
This is a view module to define list, create, update, delete views.

You can define different view properties here.
"""

from django.db.models import Q
from django.template.loader import get_template
from django_datatables_too.mixins import DataTableMixin
from django.shortcuts import reverse
from core.mixins import HasPermissionsMixin
from core.views.generic import (
    MyListView, MyDetailView, MyCreateView, MyUpdateView, MyDeleteView, MyLoginRequiredView,
)
from core.forms import ReviewCategoryChangeForm, ReviewCategoryCreationForm,YearCreationForm
from core.models import ReviewCategory, Review,ModelYear
from django.http import JsonResponse
from django.shortcuts import render
# -----------------------------------------------------------------------------
# ReviewCategory Views
# -----------------------------------------------------------------------------


class YearListView(MyListView):
    """
    View for ReviewCategory listing
    """
    # paginate_by = 25
    ordering = ["-id"]
    model = ModelYear
    queryset = model.objects.all()
    template_name = "core/template_change/ModelYear.html"
    # permission_required=None
    # permission_required = ("core.view_reviewcategory",)



# class ReviewCategoryListView(MyListView):
#     # reviewcategory-list
#     """
#     View for ReviewCategory listing
#     """
#     # paginate_by = 25
#     ordering = ["-id"]
#     model = ReviewCategory
#     queryset = model.objects.all()
#     template_name = "core/review_category/review_category_list.html"
#     permission_required = ("core.view_reviewcategory",)






class YearCreateView(MyCreateView):
    """
    View to create ReviewCategory
    """
    model = ModelYear
    form_class = YearCreationForm
    template_name = "core/template_change/modelyear_form.html"
    permission_required = ("core.add_reviewcategory",)

    def form_valid(self, form):
        form.instance.create_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # opts = self.model._meta
        return reverse("core:modelyear-list")


class YearAjaxPagination(DataTableMixin, HasPermissionsMixin, MyLoginRequiredView):
    """
    Ajax-Pagination view for ReviewCategory
    """
    model = ModelYear
    queryset = model.objects.all().order_by("-id")

    def _get_is_superuser(self, obj):
        """Get boolean column markup."""
        t = get_template("core/partials/list_boolean.html")
        return t.render({"bool_val": obj.is_superuser})

    def is_orderable(self):
        """Check if order is defined in dictionary."""
        # if self._querydict.get("order"):
        #     return True
        return True

    def _get_actions(self, obj):
        """Get actions column markup."""
        t = get_template("core/partials/list_row_actions.html")
        opts = self.model._meta
        return t.render({
            "o": obj,
            "opts": opts,
            "has_change_permission": self.has_change_permission(self.request),
            "has_delete_permission": self.has_delete_permission(self.request),
        })

    def filter_queryset(self, qs):
        """Return the list of items for this view."""
        # If a search term, filter the query
        if self.search:
            return qs.filter(
                Q(year__icontains=self.search) |
                Q(year__icontains=self.search)
            )
        return qs

    def prepare_results(self, qs):
        """Prepare final result data here."""
        # Create row data for datatables
        data = []
        for o in qs:
            if o.year:
                year = o.year
            else:
                slug = '-'
            url = reverse("core:reviewcategory-detailview", kwargs={'pk': o.pk})
            data.append(
                {
                    "id": o.id,
                    # "name":  "<a href='" + url + "'>" + o.name + "</a>",
                    "year": o.year,
                }
            )
        return data

    def get(self, request, *args, **kwargs):
        context_data = self.get_context_data(request)
        total_filter_data = len(self.filter_queryset(self.model.objects.all().order_by("-id")))
        context_data['recordsTotal'] = len(self.model.objects.all().order_by("-id"))
        context_data['recordsFiltered'] = total_filter_data
        return JsonResponse(context_data)