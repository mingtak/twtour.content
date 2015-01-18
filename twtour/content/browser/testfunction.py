from Products.Five.browser import BrowserView
import logging

logger = logging.getLogger("TESTFUNCTION")


class TestFunction(BrowserView):
    def __call__(self):
        import pdb; pdb.set_trace()
        return
