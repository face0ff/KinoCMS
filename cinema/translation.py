from modeltranslation.translator import register, TranslationOptions

from cinema.models import Film, Cinema, Hall


@register(Film)
class FilmTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Cinema)
class CinemaTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'condition')


@register(Hall)
class HallTranslationOptions(TranslationOptions):
    fields = ('number', 'description')