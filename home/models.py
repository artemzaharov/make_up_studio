from django.db import models
from wagtail.core.models import Page, TranslatableMixin
from wagtail.models import Page
from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import StreamField
from streams import blocks


@register_snippet
class Menu(TranslatableMixin):
    ''' Alows to translate menus '''
    menu = StreamField([
        ('menus', blocks.MenuBlock())
    ])


class HomePage(Page):
    menu = models.ForeignKey(
        Menu, on_delete=models.SET_NULL, null=True, related_name="menus"
    )

    content_panels = Page.content_panels + [
        FieldPanel("menu"),
    ]