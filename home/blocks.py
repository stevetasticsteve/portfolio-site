from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.fields import StreamField
from wagtail.contrib.table_block.blocks import TableBlock as WagtailTableBlock
from wagtailcodeblock.blocks import CodeBlock


class ParagraphBlock(blocks.StructBlock):
    """
    Single column rich text block
    """

    text = blocks.RichTextBlock(
        help_text="Text to display",
        features=[
            "bold",
            "italic",
            "h2",
            "h3",
            "h4",
            "ol",
            "ul",
            "strikethrough",
            "link",
            "document-link",
            "hr",
        ],
    )

    class Meta:
        template = "streams/paragraph_block.html"
        icon = "edit"
        label = "Paragraph"
        help_text = "Formatted text to make up paragraphs"


class ImageBlock(ImageChooserBlock):
    """
    Upload an image.
    """

    class Meta:
        template = "streams/image_block.html"
        icon = "fa-picture-o"
        label = "Image"
        help_text = "Upload an image. Will be centered with a border"


class VideoBlock(blocks.StructBlock):
    """
    An embeddable video block.
    """

    video = EmbedBlock(help_text="Embed a video from Youtube")
    caption = blocks.CharBlock(
        max_length=50, required=False, help_text="Optional caption for video"
    )

    # custom init so column can be passed to template
    def __init__(self, required=False, label=None, help_text=None, *args, **kwargs):
        self._required = required
        self._help_text = help_text
        self._label = label
        self.column = kwargs.get("column")
        super().__init__(*args, **kwargs)

    def get_context(self, value, parent_context=None):
        ctx = super().get_context(value, parent_context=parent_context)
        ctx["column"] = self.column
        return ctx

    class Meta:
        template = "streams/embed_block.html"
        icon = "media"
        label = "Video Embed"
        help_text = "Embed a video"


class DownloadBlock(blocks.StructBlock):
    """
    Link to a file that can be downloaded.
    """

    button_title = blocks.CharBlock(
        max_length=25, required=True, help_text="Text to go on download button"
    )
    downloadable_file = DocumentChooserBlock(required=True, help="Document to download")

    class Meta:
        template = "streams/download_block.html"
        icon = "download"
        help_text = "Display a button that downloads a file"


class QuoteBlock(blocks.StructBlock):
    """
    A <blockquote>.
    """

    text = blocks.TextBlock(
        required=True,
        rows=4,
        label="Quote Text",
    )
    author = blocks.CharBlock(
        required=False,
        max_length=255,
        label="Author",
    )

    class Meta:
        template = "streams/quote_block.html"
        icon = "openquote"
        label = "Quote"
        help_text = "A quotation"


class TableBlock(blocks.StructBlock):
    """
    A simple table.
    """

    table = WagtailTableBlock()

    class Meta:
        template = "streams/table_block.html"
        icon = "table"
        label = "Table"
        help_text = "Insert a table"


class ColumnBlock(blocks.StructBlock):
    """
    Renders a row of md-6 columns.
    """

    # todo coudn't find a way to avoid circular name errors, so copy pasted here
    local_blocks = (
        ("paragraph", ParagraphBlock()),
        ("image", ImageBlock()),
        ("video", VideoBlock(column="2")),
        ("download", DownloadBlock()),
        ("quote", QuoteBlock()),
        ("table", TableBlock()),
        ("code", CodeBlock()),
    )

    class Meta:
        template = "streams/two_column_block.html"
        icon = "fa-columns"
        label = "2 Column block"
        help_text = "The first block will go on the left."

    def __init__(self, local_blocks=local_blocks):
        local_blocks = (
            (
                "content",
                blocks.StreamBlock(
                    local_blocks, label="Select two columns.", min_num=2, max_num=2
                ),
            ),
        )
        super().__init__(
            local_blocks,
        )


def single_column_blocks():
    """Function to return all block types suitable for full width"""
    single_column_blocks = [
        ("column_block", ColumnBlock()),
        ("paragraph", ParagraphBlock()),
        ("image", ImageBlock()),
        ("video", VideoBlock(column="1")),
        ("download", DownloadBlock()),
        ("quote", QuoteBlock()),
        ("table", TableBlock()),
        ("code", CodeBlock()),
    ]
    return single_column_blocks


full_streamfield = StreamField(
    single_column_blocks(), null=True, blank=True, use_json_field=True
)
