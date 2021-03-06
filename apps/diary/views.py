from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.diary.serializers import PageSerializer
from apps.diary.models import Page


class Home(LoginRequiredMixin, APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "diary/home.html"

    def get(self, request, number=None):
        if not number:
            page = Page.objects.get_todays_page(request.user)
        else:
            number = int(number)
            pages = Page.objects.filter(user=request.user).order_by("-date_created")
            try:
                page = pages[number - 1]
            except IndexError:
                return Http404(f"Page {number} does not exist")
        serialized_page = PageSerializer(page, context={"request": request})

        pages = Page.objects.filter(user=request.user).order_by("-date_created")
        serialized_pages = PageSerializer(
            pages, many=True, context={"request": request}
        )
        return Response({"pages": serialized_pages.data, "serializer": serialized_page})

    def post(self, request):
        page = get_object_or_404(Page, id=request.data["id"])
        if page.user != request.user:
            return Http404("You cannot edit another user's diary")

        serializer = PageSerializer(
            page, data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
        return redirect("home")
