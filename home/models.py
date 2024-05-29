from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

from . import blocks as myblocks
from projects.models import CategoryPage, ProjectPage


class HomePage(Page):
    max_count = 1
    parent_page_types = ["wagtailcore.Page"]

    lead_text = models.CharField(
        max_length=50, blank=False, help_text="Text to appear in top banner"
    )
    body = RichTextField(
        blank=True, help_text="Centered text to appear below banner above links "
    )
    avatar_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        help_text="Avatar to go in home page banner",
        on_delete=models.PROTECT,
    )

    content_panels = Page.content_panels + [
        FieldPanel("lead_text"),
        FieldPanel("body"),
        FieldPanel("avatar_image"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        categories = CategoryPage.objects.live()
        for c in categories:
            c.pages = c.get_children().live().specific()[:4]

        context["categories"] = categories

        return context


class AboutPage(Page):
    max_count = 1
    parent_page_types = ["HomePage"]
    subpage_types = []

    body = myblocks.full_streamfield

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        projects = ProjectPage.objects.live().order_by("created")
        context["projects"] = projects

        return context


class GeneralPage(Page):
    body = myblocks.full_streamfield

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]
