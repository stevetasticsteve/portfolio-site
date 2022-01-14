from django.db import models
from django import forms

from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from modelcluster.fields import ParentalManyToManyField
from wagtail.snippets.models import register_snippet


@register_snippet
class Technology(models.Model):
    name = models.CharField(max_length=50, blank=False, null=True)
    link = models.URLField(blank=False, null=True)

    panels = [FieldPanel("name"), FieldPanel("link")]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "project technologies"
        ordering = ("name",)


class ProjectPage(Page):
    parent_page_types = ["CategoryPage"]
    technologies = ParentalManyToManyField("Technology", blank=False, null=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        help_text="Image to represent project",
        on_delete=models.PROTECT,
    )
    short_description = models.CharField(
        max_length=200,
        blank=False,
        null=True,
        help_text="Short description to go in card.",
    )
    created = models.DateField(blank=True, null=True, help_text="date created")
    github_url = models.URLField(blank=True, null=True)
    example_url = models.URLField(blank=True, null=True)
    body = StreamField(
        [
            ("heading", blocks.CharBlock(form_classname="full title")),
            ("paragraph", blocks.RichTextBlock()),
            ("image", ImageChooserBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("technologies", widget=forms.CheckboxSelectMultiple),
        ImageChooserPanel("image"),
        FieldPanel("short_description"),
        FieldPanel("created"),
        FieldPanel("github_url"),
        FieldPanel("example_url"),
        StreamFieldPanel("body"),
    ]


class CategoryPage(Page):
    parent_page_types = ["home.HomePage"]
    short_description = models.CharField(max_length=250, blank=False, null=True)
    icon = models.CharField(
        max_length=50, blank=False, null=True, help_text="Font awesome icon to use."
    )

    content_panels = Page.content_panels + [
        FieldPanel("short_description"),
        FieldPanel("icon"),
    ]
