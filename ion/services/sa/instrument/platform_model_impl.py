#!/usr/bin/env python

"""
@package  ion.services.sa.instrument.platform_model_impl
@author   Ian Katz
"""

#from pyon.core.exception import BadRequest, NotFound
from pyon.public import RT

from ion.services.sa.instrument.ims_simple import IMSsimple

class PlatformModelImpl(IMSsimple):
    """
    @brief resource management for PlatformModel resources
    """

    def _primary_object_name(self):
        return RT.PlatformModel

    def _primary_object_label(self):
        return "platform_model"
