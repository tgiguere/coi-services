#!/usr/bin/env python

__author__ = 'Ian Katz'
__license__ = 'Apache 2.0'

from ion.services.sa.direct_access.direct_access import DirectAccess


class PlatformDirectAccess(DirectAccess):
    """
    Class for direct access at the platform level
    """

    def request(self, request_params={}):
        pass

    def stop(self, stop_params={}):
        pass

