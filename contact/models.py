from django.db import models
from django.utils.translation import gettext_lazy as _
from modelcluster.models import ParentalKey
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField

from wagtailcaptcha.models import WagtailCaptchaEmailForm

FORM_FIELD_CHOICES = (
    ("singleline", _("Single line text")),
    ("multiline", _("Multi-line text")),
    ("email", _("Email")),
    ("url", _("URL")),
    ("radio", _("Radio buttons")),
)


class CustomAbstractFormField(AbstractFormField):
    field_type = models.CharField(
        verbose_name="Field Type",
        max_length=16,
        choices=FORM_FIELD_CHOICES,
    )

    class Meta:
        abstract = True
        ordering = ["sort_order"]


class FormField(CustomAbstractFormField):
    page = ParentalKey(
        "ContactPage", on_delete=models.CASCADE, related_name="form_fields"
    )


class ContactPage(WagtailCaptchaEmailForm):
    template = "contact/contact_page.html"
    landing_page_template = "contact/contact_page_landing.html"
    parent_page_types = ["home.HomePage"]
    subpage_types = []
    max_count = 1

    intro = RichTextField(
        blank=True,
        features=["bold", "link", "ol"],
        help_text="Text that will appear directly under the page title.",
    )
    thank_you_text = RichTextField(
        blank=True,
        features=["bold", "link", "ol"],
        help_text="Message to user on submission of form.",
    )
    from_address = models.EmailField(
        default="stevestanleyweb@gmail.com",
        blank=False,
        null=False,
        help_text="Email address to use to send email from.",
    )
    contact_page_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        help_text="Image will fill the left column and be cropped to 580px by 355px",
        related_name="+",
    )

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel("intro"),
        FieldPanel("contact_page_image"),
        InlinePanel(
            "form_fields",
            label="Form Fields",
            help_text="Build a form here, will fill the right column.",
        ),
        FieldPanel("thank_you_text"),
        FieldPanel("from_address"),
        FieldPanel("to_address", help_text="Email address message should go to."),
        FieldPanel("subject"),
    ]
