from five import grok

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Container
from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.formwidget.autocomplete import AutocompleteMultiFieldWidget, AutocompleteFieldWidget
from zope.lifecycleevent.interfaces import IObjectAddedEvent

from twtour.content.attractions import IAttractions
from twtour.content import MessageFactory as _

from plone.multilingual.interfaces import ITranslationManager, ILanguage
from random import choice
from plone.indexer import indexer

# Interface class; used to define content-type schema.

class ITourNews(form.Schema, IImageScaleTraversable):
    """
    Taiwan Tour News Item
    """

    leadImageForNews = NamedBlobImage(
        title=_(u'Lead image'),
        required=True,
    )

    detail = RichText(
        title=_(u'Event detail information'),
        required=False,
    )

    form.widget(relatedAttractions=AutocompleteMultiFieldWidget)
    relatedAttractions = RelationList(
        title=_(u"Related attractions"),
        value_type=RelationChoice(
            source=ObjPathSourceBinder(
                object_provides=IAttractions.__identifier__,
            ),
        ),
        required=True,
    )

    pubDate = schema.Datetime(
        title=_(u'Published datetime'),
        required=False,
    )

    sourcePageUrl = schema.URI(
        title=_(u'Source page URL'),
        required=False,
    )


class TourNews(Container):
    grok.implements(ITourNews)


class SampleView(grok.View):
    """ sample view class """

    grok.context(ITourNews)
    grok.require('zope2.View')
    grok.name('view')


    def getTranslated(self):
        return ITranslationManager(self.context).get_translated_languages()


    def getLanguage(self):
        return ILanguage(self.context).get_language()


    def get_translation(self, langCode):
        return ITranslationManager(self.context).get_translation(langCode)


@grok.subscribe(ITourNews, IObjectAddedEvent)
def initialItem(item, event):
    item.exclude_from_nav = True
    subject = list(item.Subject())
    subject.append(item.Title())
    subject.append(choice(['Taiwan Travel', 'Taiwan Tour', 'Formosa', 'Backpacker']))
    if item.relatedAttractions is not None:
        for relatedItem in item.relatedAttractions:
            subject.append(relatedItem.to_object.Title())
    item.setSubject(subject)
    item.reindexObject()


@indexer(ITourNews)
def pubDate_indexer(obj):
     return obj.pubDate
grok.global_adapter(pubDate_indexer, name='pubDate')
