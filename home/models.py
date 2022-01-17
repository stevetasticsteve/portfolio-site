from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from . import blocks as myblocks
from projects.models import CategoryPage, ProjectPage


class HomePage(Page):
    max_count = 1
    parent_page_types = ["wagtailcore.Page"]

    lead_text = models.CharField(max_length=50, blank=False)
    body = RichTextField(blank=True)
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
        ImageChooserPanel("avatar_image"),
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        categories = CategoryPage.objects.live()
        for c in categories:
            c.pages = c.get_children().live().specific()
        context["categories"] = categories

        return context


class AboutPage(Page):
    max_count = 1
    parent_page_types = ["HomePage"]

    body = myblocks.full_streamfield


    content_panels = Page.content_panels + [
        StreamFieldPanel("body"),
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        projects = ProjectPage.objects.live().order_by("created")
        context["projects"] = projects

        return context

class GeneralPage(Page):
    body = myblocks.full_streamfield


    content_panels = Page.content_panels + [
        StreamFieldPanel("body"),
    ]
