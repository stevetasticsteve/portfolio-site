from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from . import blocks as myblocks
from wagtail.core import blocks


from projects.models import CategoryPage


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
    maentx_count = 1
    par_page_types = ["HomePage"]

    body = myblocks.full_streamfield
    # body = StreamField([
    #     ('heading', blocks.CharBlock(form_classname="full title")),
    #     ('paragraph', blocks.RichTextBlock()),
    #     ('image', ImageChooserBlock()),
    # ], null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel("body"),
        ]