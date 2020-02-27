# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.paging import Paged


class GalleryPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Gallery <azure.mgmt.compute.v2019_12_01.models.Gallery>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Gallery]'}
    }

    def __init__(self, *args, **kwargs):

        super(GalleryPaged, self).__init__(*args, **kwargs)
class GalleryImagePaged(Paged):
    """
    A paging container for iterating over a list of :class:`GalleryImage <azure.mgmt.compute.v2019_12_01.models.GalleryImage>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[GalleryImage]'}
    }

    def __init__(self, *args, **kwargs):

        super(GalleryImagePaged, self).__init__(*args, **kwargs)
class GalleryImageVersionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`GalleryImageVersion <azure.mgmt.compute.v2019_12_01.models.GalleryImageVersion>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[GalleryImageVersion]'}
    }

    def __init__(self, *args, **kwargs):

        super(GalleryImageVersionPaged, self).__init__(*args, **kwargs)
class GalleryApplicationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`GalleryApplication <azure.mgmt.compute.v2019_12_01.models.GalleryApplication>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[GalleryApplication]'}
    }

    def __init__(self, *args, **kwargs):

        super(GalleryApplicationPaged, self).__init__(*args, **kwargs)
class GalleryApplicationVersionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`GalleryApplicationVersion <azure.mgmt.compute.v2019_12_01.models.GalleryApplicationVersion>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[GalleryApplicationVersion]'}
    }

    def __init__(self, *args, **kwargs):

        super(GalleryApplicationVersionPaged, self).__init__(*args, **kwargs)
