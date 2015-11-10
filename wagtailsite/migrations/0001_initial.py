# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import modelcluster.contrib.taggit
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0008_image_created_at_index'),
        ('wagtaildocs', '0003_add_verbose_names'),
        ('wagtailcore', '0019_verbose_names_cleanup'),
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, to='wagtailcore.Page', serialize=False, primary_key=True, parent_link=True)),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogIndexPageRelatedLink',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('sort_order', models.IntegerField(editable=False, null=True, blank=True)),
                ('link_external', models.URLField(verbose_name='External link', blank=True)),
                ('title', models.CharField(help_text='Link title', max_length=255)),
                ('link_document', models.ForeignKey(related_name='+', null=True, to='wagtaildocs.Document', blank=True)),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, to='wagtailcore.Page', serialize=False, primary_key=True, parent_link=True)),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('body', wagtail.wagtailcore.fields.RichTextField()),
                ('date', models.DateField(verbose_name='Post date')),
                ('feed_image', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, null=True, to='wagtailimages.Image', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogPageRelatedLink',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('sort_order', models.IntegerField(editable=False, null=True, blank=True)),
                ('link_external', models.URLField(verbose_name='External link', blank=True)),
                ('title', models.CharField(help_text='Link title', max_length=255)),
                ('link_document', models.ForeignKey(related_name='+', null=True, to='wagtaildocs.Document', blank=True)),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='BlogPageTag',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('content_object', modelcluster.fields.ParentalKey(related_name='tagged_items', to='wagtailsite.BlogPage')),
                ('tag', models.ForeignKey(related_name='wagtailsite_blogpagetag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, to='wagtailcore.Page', serialize=False, primary_key=True, parent_link=True)),
            ],
            options={
                'verbose_name': 'Homepage',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='blogpagerelatedlink',
            name='link_page',
            field=models.ForeignKey(related_name='+', null=True, to='wagtailcore.Page', blank=True),
        ),
        migrations.AddField(
            model_name='blogpagerelatedlink',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='related_links', to='wagtailsite.BlogPage'),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(to='taggit.Tag', verbose_name='Tags', blank=True, through='wagtailsite.BlogPageTag', help_text='A comma-separated list of tags.'),
        ),
        migrations.AddField(
            model_name='blogindexpagerelatedlink',
            name='link_page',
            field=models.ForeignKey(related_name='+', null=True, to='wagtailcore.Page', blank=True),
        ),
        migrations.AddField(
            model_name='blogindexpagerelatedlink',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='related_links', to='wagtailsite.BlogIndexPage'),
        ),
    ]
