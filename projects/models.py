from django.db import models
from django import forms

from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField, StreamField
from modelcluster.fields import ParentalManyToManyField
from wagtail.snippets.models import register_snippet

from home import blocks as myblocks


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
    subpage_types = []
    technologies = ParentalManyToManyField("Technology", blank=False)
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
    created = models.DateField(blank=False, null=True, help_text="date created")
    github_url = models.URLField(blank=True, null=True)
    example_url = models.URLField(blank=True, null=True)
    body = myblocks.full_streamfield
    learned = RichTextField(features=["ul"], blank=False, null=True)

    content_panels = Page.content_panels + [
        FieldPanel("technologies", widget=forms.CheckboxSelectMultiple),
        ImageChooserPanel("image"),
        FieldPanel("short_description"),
        FieldPanel("created"),
        FieldPanel("github_url"),
        FieldPanel("example_url"),
        StreamFieldPanel("body"),
        StreamFieldPanel("learned"),
    ]


class CategoryPage(Page):
    parent_page_types = ["home.HomePage"]
    subpage_types = ["ProjectPage"]
    short_description = RichTextField(blank=False, null=True)
    icon = models.CharField(
        max_length=50, blank=False, null=True, help_text="Font awesome icon to use."
    )

    content_panels = Page.content_panels + [
        FieldPanel("short_description"),
        FieldPanel("icon"),
    ]


class HelpIndexPage(Page):
    parent_page_types = ["home.HomePage"]
    subpage_types = ["HelpPage"]
    max_count = 1


class HelpPage(Page):
    parent_page_type = ["HelpIndexPage"]
    subpage_types = []
    body = myblocks.full_streamfield

    content_panels = Page.content_panels + [
        StreamFieldPanel("body"),
    ]
