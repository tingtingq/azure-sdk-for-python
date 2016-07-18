# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ExpressRouteCircuitsRoutesTableSummaryListResult(Model):
    """Response for ListRoutesTable associated with the Express Route Circuits
    Api.

    :param value: Gets List of RoutesTable
    :type value: list of :class:`ExpressRouteCircuitRoutesTableSummary
     <azure.mgmt.network.models.ExpressRouteCircuitRoutesTableSummary>`
    :param next_link: Gets the URL to get the next set of results.
    :type next_link: str
    """ 

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ExpressRouteCircuitRoutesTableSummary]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, value=None, next_link=None):
        self.value = value
        self.next_link = next_link
