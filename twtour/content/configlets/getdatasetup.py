from zope import schema
from plone.directives import dexterity, form
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

from plone.z3cform import layout
from z3c.form import form as z3cform

from twtour.content import MessageFactory as _


class IGetDataSetup(form.Schema):
    """
    Get data setup for taiwan-tour.tw
    """
    # Get twtourEvent, zh-TW,
    twtourEventUrl_tw_1 = schema.URI(
        title=_(u'URL'),
        description=_(u'twtourEvent URL, zh-TWTaiwan'),
        required=False,
    )

    # Get twtourEvent, en-US,
    twtourEventUrl_us_1 = schema.URI(
        title=_(u'URL'),
        description=_(u'twtourEvent URL, en-US'),
        required=False,
    )

    # Get tourNews, en-us
    tourNewsUrl_us_1 = schema.URI(
        title=_(u'URL'),
        description=_(u'tourNews URL, en-us'),
        required=False,
    )


class GetDataSetupControlPanelForm(RegistryEditForm):
    z3cform.extends(RegistryEditForm)
    schema = IGetDataSetup

GetDataSetupControlPanelView = layout.wrap_form(GetDataSetupControlPanelForm, ControlPanelFormWrapper)
GetDataSetupControlPanelView.label = _(u"Get data setup")
