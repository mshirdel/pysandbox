from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import timezone


class HomepageView(TemplateView):
    template_name = "web/index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["today"] = timezone.now()
        return context
