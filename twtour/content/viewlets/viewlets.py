#-*- coding:utf-8 -*-
from zope.interface import Interface
from five import grok
from plone.app.layout.viewlets.interfaces import IContentViews, IPortalHeader, IAboveContent, IBelowContentBody
#from reporter.content.eventinfo import IEventInfo
#from reporter.content.article import IArticle
#from reporter.content.contentlist import IContentList
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile



"""
# viewlet nameing format: ContentType_Position_ViewletFunction
class EventInfo_IAboveContent_ResponsiveAd(grok.Viewlet):
    grok.viewletmanager(IAboveContent)
    grok.context(IEventInfo)
    template = ViewPageTemplateFile('template/responsivead.pt')

    def render(self):
        return self.template()


class All_IBelowContentBody_TopBanner(grok.Viewlet):
    grok.viewletmanager(IBelowContentBody)
    grok.context(Interface)
    template = ViewPageTemplateFile('template/topbanner.pt')

    def render(self):
        return self.template()


class All_IBelowContentBody_Sidebar(grok.Viewlet):
    grok.viewletmanager(IBelowContentBody)
    grok.context(Interface)
    template = ViewPageTemplateFile('template/sidebar.pt')

    def render(self):
        return self.template()


class All_IBelowContentBody_WebHeaderTop(grok.Viewlet):
    grok.viewletmanager(IBelowContentBody)
    grok.context(Interface)
    template = ViewPageTemplateFile('template/webheadertop.pt')

    def render(self):
        return self.template()
"""
