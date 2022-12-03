from wagtail.core import blocks

class MenuBlock(blocks.StructBlock):

    title_menu = blocks.CharBlock(required=True, help_text='Add your title')
    title_url = blocks.URLBlock(required=True, help_text='Add additional text')
    
    class Meta:  # noqa
        template = 'streams/menu_block.html'
        icon = "edit"
        label = "Menus"