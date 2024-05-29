# Generated by Django 3.2.11 on 2022-01-18 20:08

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('wagtailimages', '0023_add_choose_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('to_address', models.CharField(blank=True, help_text='Optional - form submissions will be emailed to these addresses. Separate multiple addresses by comma.', max_length=255, verbose_name='to address')),
                ('subject', models.CharField(blank=True, max_length=255, verbose_name='subject')),
                ('intro', wagtail.fields.RichTextField(blank=True, help_text='Text that will appear directly under the page title.')),
                ('thank_you_text', wagtail.fields.RichTextField(blank=True, help_text='Message to user on submission of form.')),
                ('from_address', models.EmailField(default='stevestanleyweb@gmail.com', help_text='Email address to use to send email from.', max_length=254)),
                ('contact_page_image', models.ForeignKey(help_text='Image will fill the left column and be cropped to 580px by 355px', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('clean_name', models.CharField(blank=True, default='', help_text='Safe name of the form field, the label converted to ascii_snake_case', max_length=255, verbose_name='name')),
                ('label', models.CharField(help_text='The label of the form field', max_length=255, verbose_name='label')),
                ('required', models.BooleanField(default=True, verbose_name='required')),
                ('choices', models.TextField(blank=True, help_text='Comma separated list of choices. Only applicable in checkboxes, radio and dropdown.', verbose_name='choices')),
                ('default_value', models.CharField(blank=True, help_text='Default value. Comma separated values supported for checkboxes.', max_length=255, verbose_name='default value')),
                ('help_text', models.CharField(blank=True, max_length=255, verbose_name='help text')),
                ('field_type', models.CharField(choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('url', 'URL'), ('radio', 'Radio buttons')], max_length=16, verbose_name='Field Type')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_fields', to='contact.contactpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
