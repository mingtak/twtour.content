# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
import logging
from plone import api
from bs4 import BeautifulSoup
import urllib2
from Products.CMFPlone.utils import safe_unicode
from datetime import date, datetime
from plone.app.textfield.value import RichTextValue
from plone.multilingual.interfaces import ILanguage
from htmllaundry import strip_markup

logger = logging.getLogger("getdata.py")

registryPrefix = "twtour.content.configlets.getdatasetup.IGetDataSetup"


class GetNews(BrowserView):

    def __call__(self):
        portal = api.portal.get()
        request = self.request
        catalog = api.portal.get_tool(name='portal_catalog')
        lang = request['lang']
        suffix = request['suffix']
        url = api.portal.get_registry_record('%s.%s' % (registryPrefix, suffix))
        response = urllib2.urlopen(url)
        doc = response.read()
        xmlSoup = BeautifulSoup(doc, 'xml')
        items = xmlSoup.find_all('item')
        for item in items:
            try:
                title = unicode(safe_unicode(item.find('title').string))
                pubDateString = unicode(safe_unicode(item.find('pubDate').string))
                pubDate = datetime.strptime(pubDateString, '%a, %d %b %Y %X %Z')
                brain = catalog({'Language':lang, 'pubDate':pubDate})
                if len(brain) > 0:
                    continue
                description = unicode(safe_unicode(item.find('description').string))
                description = strip_markup(description)
                sourcePageUrl = unicode(safe_unicode(item.find('link').string))

                object = api.content.create(
                    container=portal[lang]['news'],
                    type='twtour.content.tournews',
                    title=title,
                    description=description,
                    sourcePageUrl=sourcePageUrl,
                    pubDate=pubDate,
                    detail=RichTextValue(u'<p>%s</p>' % description, 'text/html', 'text/html'),
                )
#                ILanguage(object).set_language(lang)
#                object.reindexObject()
            except:
                pass

        return


class GetEvent(BrowserView):

    def __call__(self):
        portal = api.portal.get()
        request = self.request
        catalog = api.portal.get_tool(name='portal_catalog')
        suffix = request['suffix']
        url = api.portal.get_registry_record('%s.%s' % (registryPrefix, suffix))
        response = urllib2.urlopen(url)
        doc = response.read()
        xmlSoup = BeautifulSoup(doc, 'xml')
        items = xmlSoup.find_all('item')
        for item in items:
            try:
                title = unicode(safe_unicode(item.find('title').string))
                pubDateString = unicode(safe_unicode(item.find('pubDate').string))
                pubDate = datetime.strptime(pubDateString, '%a, %d %b %Y %X %Z')
                brain = catalog({'Language':request['lang'], 'pubDate':pubDate})
                if len(brain) > 0:
                    continue
                description = unicode(safe_unicode(item.find('description').string))
                sourcePageUrl = unicode(safe_unicode(item.find('link').string))
                organizer = unicode(safe_unicode(item.find('mw_c1').string))
                eventWebSite = unicode(safe_unicode(item.find('mw_c3').string))
                year, month, day = item.find('mw_date1').string.split('-')
                startDate = date(int(year),int(month),int(day))
                year, month, day = item.find('mw_date2').string.split('-')
                endDate = date(int(year),int(month),int(day))
                mapPoint = unicode(safe_unicode(item.find('map').string))
                latitude = 0 if item.find('lat').string is None else float(str(item.find('lat').string))
                longitude = 0 if item.find('long').string is None else float(str(item.find('long').string))

                api.content.create(
                    container=portal[request['lang']]['event'],
                    type='twtour.content.tourevent',
                    title=title,
                    description=description,
                    sourcePageUrl=sourcePageUrl,
                    pubDate=pubDate,
                    organizer=organizer,
                    eventWebSite=eventWebSite,
                    startDate=startDate,
                    endDate=endDate,
                    detail=RichTextValue(u'<p>%s</p>' % description, 'text/html', 'text/html'),
                    mapPoint=mapPoint,
                    latitude=latitude,
                    longitude=longitude,
                )
            except:
                pass

        return
