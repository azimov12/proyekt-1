from modeltranslation.translator import TranslationOptions, translator
from polls.models import NewsModel

class NewsModelTranslationOptions(TranslationOptions):
    fields = ('tittle', 'body')  


translator.register(NewsModel, NewsModelTranslationOptions)