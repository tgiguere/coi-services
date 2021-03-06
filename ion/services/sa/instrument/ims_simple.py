#!/usr/bin/env python

"""
@package  ion.services.sa.instrument.ims_simple
@author   Ian Katz
"""

#from pyon.core.exception import BadRequest, NotFound
#from pyon.core.bootstrap import IonObject
from pyon.public import LCE

from ion.services.sa.resource_impl import ResourceImpl


class IMSsimple(ResourceImpl):
    """
    @brief A base class for management of ION resources in IMS that have a simple LCS
    """
    
    def on_post_create(self, obj_id, obj):
        """
        this is for simple resources ...
        they go into active lifecycle state immediately upon creation
        @param obj_id an object id
        @param obj the object itself (not needed in this case)
        """
        self.advance_lcs(obj_id, LCE.register)

        return

    def lcs_precondition_register(self, resource_id):
        """
        preconditions for going registered (none)
        @param resource_id the id of the resource in question
        """
        return True
