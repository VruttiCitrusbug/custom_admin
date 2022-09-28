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
from core.forms import BikeClassCreationForm,YearCreationForm,YearChangeForm,FrameTypeCreationForm,WheelSizeCreationForm,BreakTypeCreationForm,FrameTypeChangeForm,BikeClassChangeForm,WheelSizeChangeForm,BreakTypeChangeForm
from core.models import BreakType,ModelYear,BikeClass,FrameType,WheelSize
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

class BikeClassListView(MyListView):
    """
    View for ReviewCategory listing
    """
    # paginate_by = 25
    ordering = ["-id"]
    model = BikeClass
    queryset = model.objects.all()
    template_name = "core/template_change/BikeClass.html"

class FrameTypeListView(MyListView):
    """
    View for ReviewCategory listing
    """
    # paginate_by = 25
    ordering = ["-id"]
    model = FrameType
    queryset = model.objects.all()
    template_name = "core/template_change/FrameType.html"

class WheelSizeListView(MyListView):
    """
    View for ReviewCategory listing
    """
    # paginate_by = 25
    ordering = ["-id"]
    model = WheelSize
    queryset = model.objects.all()
    template_name = "core/template_change/WheelSize.html"

class BreakTypeListView(MyListView):
    """
    View for ReviewCategory listing
    """
    # paginate_by = 25
    ordering = ["-id"]
    model = BreakType
    queryset = model.objects.all()
    template_name = "core/template_change/BreakType.html"






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


class FrameTypeCreateView(MyCreateView):
    """
    View to create ReviewCategory
    """
    model = FrameType
    form_class = FrameTypeCreationForm
    template_name = "core/template_change/frametype_form.html"
    permission_required = ("core.add_reviewcategory",)

    def form_valid(self, form):
        form.instance.create_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # opts = self.model._meta
        return reverse("core:frametype-list")

class BikeClassCreateView(MyCreateView):
    """
    View to create ReviewCategory
    """
    model = BikeClass
    form_class = BikeClassCreationForm
    template_name = "core/template_change/bikeclass_form.html"
    permission_required = ("core.add_reviewcategory",)

    def form_valid(self, form):
        form.instance.create_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # opts = self.model._meta
        return reverse("core:bikeclass-list")

class WheelSizeCreateView(MyCreateView):
    """
    View to create ReviewCategory
    """
    model = WheelSize
    form_class = WheelSizeCreationForm
    template_name = "core/template_change/wheelsize_form.html"
    permission_required = ("core.add_reviewcategory",)

    def form_valid(self, form):
        form.instance.create_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # opts = self.model._meta
        return reverse("core:wheelsize-list")
class BreakTypeCreateView(MyCreateView):
    """
    View to create ReviewCategory
    """
    model = BreakType
    form_class =BreakTypeCreationForm
    template_name = "core/template_change/breaktype_form.html"
    permission_required = ("core.add_reviewcategory",)

    def form_valid(self, form):
        form.instance.create_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # opts = self.model._meta
        return reverse("core:breaktype-list")









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
                    "actions": self._get_actions(o),
                }
            )
        return data

    def get(self, request, *args, **kwargs):
        context_data = self.get_context_data(request)
        total_filter_data = len(self.filter_queryset(self.model.objects.all().order_by("-id")))
        context_data['recordsTotal'] = len(self.model.objects.all().order_by("-id"))
        context_data['recordsFiltered'] = total_filter_data
        return JsonResponse(context_data)


class BikeClassAjaxPagination(DataTableMixin, HasPermissionsMixin, MyLoginRequiredView):
    """
    Ajax-Pagination view for ReviewCategory
    """
    model = BikeClass
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
                Q(bike_class__icontains=self.search) |
                Q(bike_class__icontains=self.search)
            )
        return qs

    def prepare_results(self, qs):
        """Prepare final result data here."""
        # Create row data for datatables
        data = []
        for o in qs:
            if o.bike_class:
                bike_class = o.bike_class
            else:
                slug = '-'
            url = reverse("core:reviewcategory-detailview", kwargs={'pk': o.pk})
            data.append(
                {
                    "id": o.id,
                    # "name":  "<a href='" + url + "'>" + o.name + "</a>",
                    "bike_class": o.bike_class,
                    "actions": self._get_actions(o),
                }
            )
        return data

    def get(self, request, *args, **kwargs):
        context_data = self.get_context_data(request)
        total_filter_data = len(self.filter_queryset(self.model.objects.all().order_by("-id")))
        context_data['recordsTotal'] = len(self.model.objects.all().order_by("-id"))
        context_data['recordsFiltered'] = total_filter_data
        return JsonResponse(context_data)

class FrameTypeAjaxPagination(DataTableMixin, HasPermissionsMixin, MyLoginRequiredView):
    """
    Ajax-Pagination view for ReviewCategory
    """
    model = FrameType
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
                Q(frame_type__icontains=self.search) |
                Q(frame_type__icontains=self.search)
            )
        return qs

    def prepare_results(self, qs):
        """Prepare final result data here."""
        # Create row data for datatables
        data = []
        for o in qs:
            if o.frame_type:
                bike_class = o.frame_type
            else:
                slug = '-'
            url = reverse("core:reviewcategory-detailview", kwargs={'pk': o.pk})
            data.append(
                {
                    "id": o.id,
                    # "name":  "<a href='" + url + "'>" + o.name + "</a>",
                    "frame_type": o.frame_type,
                    "actions": self._get_actions(o),
                }
            )
        return data

    def get(self, request, *args, **kwargs):
        context_data = self.get_context_data(request)
        total_filter_data = len(self.filter_queryset(self.model.objects.all().order_by("-id")))
        context_data['recordsTotal'] = len(self.model.objects.all().order_by("-id"))
        context_data['recordsFiltered'] = total_filter_data
        return JsonResponse(context_data)



class WheelSizeAjaxPagination(DataTableMixin, HasPermissionsMixin, MyLoginRequiredView):
    """
    Ajax-Pagination view for ReviewCategory
    """
    model = WheelSize
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
                Q(wheel_size__icontains=self.search) |
                Q(wheel_size__icontains=self.search)
            )
        return qs

    def prepare_results(self, qs):
        """Prepare final result data here."""
        # Create row data for datatables
        data = []
        for o in qs:
            if o.wheel_size:
                wheel_size = o.wheel_size
            else:
                slug = '-'
            url = reverse("core:reviewcategory-detailview", kwargs={'pk': o.pk})
            data.append(
                {
                    "id": o.id,
                    # "name":  "<a href='" + url + "'>" + o.name + "</a>",
                    "wheel_size": o.wheel_size,
                    "actions": self._get_actions(o),
                }
            )
        return data

    def get(self, request, *args, **kwargs):
        context_data = self.get_context_data(request)
        total_filter_data = len(self.filter_queryset(self.model.objects.all().order_by("-id")))
        context_data['recordsTotal'] = len(self.model.objects.all().order_by("-id"))
        context_data['recordsFiltered'] = total_filter_data
        return JsonResponse(context_data)


class BreakTypeAjaxPagination(DataTableMixin, HasPermissionsMixin, MyLoginRequiredView):
    """
    Ajax-Pagination view for ReviewCategory
    """
    model = BreakType
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
                Q(break_type__icontains=self.search) |
                Q(break_type__icontains=self.search)
            )
        return qs

    def prepare_results(self, qs):
        """Prepare final result data here."""
        # Create row data for datatables
        data = []
        for o in qs:
            if o.break_type:
                break_type = o.break_type
            else:
                slug = '-'
            url = reverse("core:reviewcategory-detailview", kwargs={'pk': o.pk})
            data.append(
                {
                    "id": o.id,
                    # "name":  "<a href='" + url + "'>" + o.name + "</a>",
                    "break_type": o.break_type,
                    "actions": self._get_actions(o),
                }
            )
        return data

    def get(self, request, *args, **kwargs):
        context_data = self.get_context_data(request)
        total_filter_data = len(self.filter_queryset(self.model.objects.all().order_by("-id")))
        context_data['recordsTotal'] = len(self.model.objects.all().order_by("-id"))
        context_data['recordsFiltered'] = total_filter_data
        return JsonResponse(context_data)











class YearUpdateView(MyUpdateView):
    """
    View to update ReviewCategory
    """

    model = ModelYear
    form_class = YearChangeForm
    template_name = "core/template_change/modelyear_form.html"
    permission_required = permission_required = ("core.add_reviewcategory",)

    def get_success_url(self):
        return reverse("core:modelyear-list")
class BikeClassUpdateView(MyUpdateView):
    """
    View to update ReviewCategory
    """

    model = BikeClass
    form_class = BikeClassChangeForm
    template_name = "core/template_change/bikeclass_form.html"
    permission_required = permission_required = ("core.add_reviewcategory",)

    def get_success_url(self):
        return reverse("core:bikeclass-list")

class FrameTypeUpdateView(MyUpdateView):
    """
    View to update ReviewCategory
    """

    model = FrameType
    form_class = FrameTypeChangeForm
    template_name = "core/template_change/frametype_form.html"
    permission_required = permission_required = ("core.add_reviewcategory",)

    def get_success_url(self):
        return reverse("core:frametype-list")

class WheelSizeUpdateView(MyUpdateView):
    """
    View to update ReviewCategory
    """

    model = WheelSize
    form_class = WheelSizeChangeForm
    template_name = "core/template_change/wheelsize_form.html"
    permission_required = permission_required = ("core.add_reviewcategory",)

    def get_success_url(self):
        return reverse("core:wheelsize-list")

class BreakTypeUpdateView(MyUpdateView):
    """
    View to update ReviewCategory
    """

    model = BreakType
    form_class = BreakTypeChangeForm
    template_name = "core/template_change/breaktype_form.html"
    permission_required = permission_required = ("core.add_reviewcategory",)

    def get_success_url(self):
        return reverse("core:breaktype-list")




class YearDeleteView(MyDeleteView):
    """
    View to delete ReviewCategory
    """
    model = ModelYear
    template_name = "core/confirm_delete.html"
    permission_required = ("core.delete_reviewcategory",)

    def get_success_url(self):
        return reverse("core:modelyear-list")
class BikeClassDeleteView(MyDeleteView):
    """
    View to delete ReviewCategory
    """
    model = BikeClass
    template_name = "core/confirm_delete.html"
    permission_required = ("core.delete_reviewcategory",)

    def get_success_url(self):
        return reverse("core:bikeclass-list")
class FrameTypeDeleteView(MyDeleteView):
    """
    View to delete ReviewCategory
    """
    model = FrameType
    template_name = "core/confirm_delete.html"
    permission_required = ("core.delete_reviewcategory",)

    def get_success_url(self):
        return reverse("core:frametype-list")
        # WheelSize
class WheelSizeDeleteView(MyDeleteView):
    """
    View to delete ReviewCategory
    """
    model = WheelSize
    template_name = "core/confirm_delete.html"
    permission_required = ("core.delete_reviewcategory",)

    def get_success_url(self):
        return reverse("core:wheelsize-list")
class BreakTypeDeleteView(MyDeleteView):
    """
    View to delete ReviewCategory
    """
    model = BreakType
    template_name = "core/confirm_delete.html"
    permission_required = ("core.delete_reviewcategory",)

    def get_success_url(self):
        return reverse("core:breaktype-list")