#!/usr/bin/env python

"""
@package  ion.services.sa.instrument.platform_agent_instance_impl
@author   Ian Katz
"""

#from pyon.core.exception import BadRequest, NotFound
from pyon.public import RT

from ion.services.sa.instrument.ims_simple import IMSsimple

class PlatformAgentInstanceImpl(IMSsimple):
    """
    @brief resource management for PlatformAgentInstance resources
    """

    def _primary_object_name(self):
        return RT.PlatformAgentInstance

    def _primary_object_label(self):
        return "platform_agent_instance"
