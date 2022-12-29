from modeltranslation.translator import register, TranslationOptions

from pages.models import MainPage, TemplatePage, NewsPromotions, Contacts


@register(MainPage)
class MainPageTranslationOptions(TranslationOptions):
    fields = ('seo_text',)


@register(TemplatePage)
class TemplatePageTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(NewsPromotions)
class NewsPromotionsTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Contacts)
class ContactsTranslationOptions(TranslationOptions):
    fields = ('cinema_name', 'address')
