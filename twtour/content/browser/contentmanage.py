# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
import logging
from plone import api
from Products.CMFPlone.utils import safe_unicode
#from datetime import date, datetime
from DateTime import DateTime
from plone.multilingual.interfaces import ILanguage

logger = logging.getLogger("contentmanage.py")


class ContentManage(BrowserView):

    template = ViewPageTemplateFile('template/contentmanage.pt')

    def __call__(self):
        portal = api.portal.get()
        request = self.request
        catalog = api.portal.get_tool(name='portal_catalog')
        period = int(request['p'])
        now = DateTime()
        startDate = now - period
        self.brain = catalog({'pubDate':{'query':startDate,'range':'min'},
                        	      'Type':['TourEvent', 'TourNews'],
                              'Language':['zh-tw', 'zh-cn', 'en-us'],
                              'review_state':'pending',
                             }, sort_on='pubDate', sort_order='reverse',)

        return self.template()
