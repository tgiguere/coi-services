#!/usr/bin/env python

"""
@package  ion.services.sa.instrument.sensor_model_impl
@author   Ian Katz
"""

#from pyon.core.exception import BadRequest, NotFound
from pyon.public import RT

from ion.services.sa.instrument.ims_simple import IMSsimple

class SensorModelImpl(IMSsimple):
    """
    @brief resource management for SensorModel resources
    """

    def _primary_object_name(self):
        return RT.SensorModel

    def _primary_object_label(self):
        return "sensor_model"
