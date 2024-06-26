# Generated by Django 3.2.11 on 2022-01-18 20:08

from django.db import migrations, models
import django.db.models.deletion
import home.blocks
import wagtail.contrib.table_block.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('wagtailimages', '0023_add_choose_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.fields.StreamField([('column_block', wagtail.blocks.StructBlock([('content', wagtail.blocks.StreamBlock([('paragraph', wagtail.blocks.StructBlock([('text', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'h2', 'h3', 'h4', 'ol', 'ul', 'strikethrough', 'link', 'document-link', 'hr'], help_text='Text to display'))])), ('image', home.blocks.ImageBlock()), ('video', wagtail.blocks.StructBlock([('video', wagtail.embeds.blocks.EmbedBlock(help_text='Embed a video from Youtube')), ('caption', wagtail.blocks.CharBlock(help_text='Optional caption for video', max_length=50, required=False))], column='2')), ('download', wagtail.blocks.StructBlock([('button_title', wagtail.blocks.CharBlock(help_text='Text to go on download button', max_length=25, required=True)), ('downloadable_file', wagtail.documents.blocks.DocumentChooserBlock(help='Document to download', required=True))])), ('quote', wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock(label='Quote Text', required=True, rows=4)), ('author', wagtail.blocks.CharBlock(label='Author', max_length=255, required=False))])), ('table', wagtail.blocks.StructBlock([('table', wagtail.contrib.table_block.blocks.TableBlock())])), ('code', wagtail.blocks.StructBlock([('language', wagtail.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('diff', 'diff'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')], help_text='Coding language', identifier='language', label='Language')), ('code', wagtail.blocks.TextBlock(identifier='code', label='Code'))]))], label='Select two columns.', max_num=2, min_num=2))])), ('paragraph', wagtail.blocks.StructBlock([('text', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'h2', 'h3', 'h4', 'ol', 'ul', 'strikethrough', 'link', 'document-link', 'hr'], help_text='Text to display'))])), ('image', home.blocks.ImageBlock()), ('video', wagtail.blocks.StructBlock([('video', wagtail.embeds.blocks.EmbedBlock(help_text='Embed a video from Youtube')), ('caption', wagtail.blocks.CharBlock(help_text='Optional caption for video', max_length=50, required=False))], column='1')), ('download', wagtail.blocks.StructBlock([('button_title', wagtail.blocks.CharBlock(help_text='Text to go on download button', max_length=25, required=True)), ('downloadable_file', wagtail.documents.blocks.DocumentChooserBlock(help='Document to download', required=True))])), ('quote', wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock(label='Quote Text', required=True, rows=4)), ('author', wagtail.blocks.CharBlock(label='Author', max_length=255, required=False))])), ('table', wagtail.blocks.StructBlock([('table', wagtail.contrib.table_block.blocks.TableBlock())])), ('code', wagtail.blocks.StructBlock([('language', wagtail.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('diff', 'diff'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')], help_text='Coding language', identifier='language', label='Language')), ('code', wagtail.blocks.TextBlock(identifier='code', label='Code'))]))], blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='GeneralPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.fields.StreamField([('column_block', wagtail.blocks.StructBlock([('content', wagtail.blocks.StreamBlock([('paragraph', wagtail.blocks.StructBlock([('text', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'h2', 'h3', 'h4', 'ol', 'ul', 'strikethrough', 'link', 'document-link', 'hr'], help_text='Text to display'))])), ('image', home.blocks.ImageBlock()), ('video', wagtail.blocks.StructBlock([('video', wagtail.embeds.blocks.EmbedBlock(help_text='Embed a video from Youtube')), ('caption', wagtail.blocks.CharBlock(help_text='Optional caption for video', max_length=50, required=False))], column='2')), ('download', wagtail.blocks.StructBlock([('button_title', wagtail.blocks.CharBlock(help_text='Text to go on download button', max_length=25, required=True)), ('downloadable_file', wagtail.documents.blocks.DocumentChooserBlock(help='Document to download', required=True))])), ('quote', wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock(label='Quote Text', required=True, rows=4)), ('author', wagtail.blocks.CharBlock(label='Author', max_length=255, required=False))])), ('table', wagtail.blocks.StructBlock([('table', wagtail.contrib.table_block.blocks.TableBlock())])), ('code', wagtail.blocks.StructBlock([('language', wagtail.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('diff', 'diff'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')], help_text='Coding language', identifier='language', label='Language')), ('code', wagtail.blocks.TextBlock(identifier='code', label='Code'))]))], label='Select two columns.', max_num=2, min_num=2))])), ('paragraph', wagtail.blocks.StructBlock([('text', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'h2', 'h3', 'h4', 'ol', 'ul', 'strikethrough', 'link', 'document-link', 'hr'], help_text='Text to display'))])), ('image', home.blocks.ImageBlock()), ('video', wagtail.blocks.StructBlock([('video', wagtail.embeds.blocks.EmbedBlock(help_text='Embed a video from Youtube')), ('caption', wagtail.blocks.CharBlock(help_text='Optional caption for video', max_length=50, required=False))], column='1')), ('download', wagtail.blocks.StructBlock([('button_title', wagtail.blocks.CharBlock(help_text='Text to go on download button', max_length=25, required=True)), ('downloadable_file', wagtail.documents.blocks.DocumentChooserBlock(help='Document to download', required=True))])), ('quote', wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock(label='Quote Text', required=True, rows=4)), ('author', wagtail.blocks.CharBlock(label='Author', max_length=255, required=False))])), ('table', wagtail.blocks.StructBlock([('table', wagtail.contrib.table_block.blocks.TableBlock())])), ('code', wagtail.blocks.StructBlock([('language', wagtail.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('diff', 'diff'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')], help_text='Coding language', identifier='language', label='Language')), ('code', wagtail.blocks.TextBlock(identifier='code', label='Code'))]))], blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('lead_text', models.CharField(help_text='Text to appear in top banner', max_length=50)),
                ('body', wagtail.fields.RichTextField(blank=True, help_text='Centered text to appear below banner above links ')),
                ('avatar_image', models.ForeignKey(help_text='Avatar to go in home page banner', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
