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


class BgpSettings(Model):
    """BgpSettings.

    :param asn: Gets or sets this BGP speaker's ASN
    :type asn: long
    :param bgp_peering_address: Gets or sets the BGP peering address and BGP
     identifier of this BGP speaker
    :type bgp_peering_address: str
    :param peer_weight: Gets or sets the weight added to routes learned from
     this BGP speaker
    :type peer_weight: int
    """ 

    _attribute_map = {
        'asn': {'key': 'asn', 'type': 'long'},
        'bgp_peering_address': {'key': 'bgpPeeringAddress', 'type': 'str'},
        'peer_weight': {'key': 'peerWeight', 'type': 'int'},
    }

    def __init__(self, asn=None, bgp_peering_address=None, peer_weight=None):
        self.asn = asn
        self.bgp_peering_address = bgp_peering_address
        self.peer_weight = peer_weight
