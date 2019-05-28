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

from msrest.serialization import Model


class ImageInsightsImageCaption(Model):
    """Defines an image's caption.

    All required parameters must be populated in order to send to Azure.

    :param caption: Required. A caption about the image.
    :type caption: str
    :param data_source_url: Required. The URL to the website where the caption
     was found. You must attribute the caption to the source. For example, by
     displaying the domain name from the URL next to the caption and using the
     URL to link to the source website.
    :type data_source_url: str
    :param related_searches: Required. A list of entities found in the
     caption. Use the contents of the Query object to find the entity in the
     caption and create a link. The link takes the user to images of the
     entity.
    :type related_searches:
     list[~azure.cognitiveservices.search.imagesearch.models.Query]
    """

    _validation = {
        'caption': {'required': True},
        'data_source_url': {'required': True},
        'related_searches': {'required': True},
    }

    _attribute_map = {
        'caption': {'key': 'caption', 'type': 'str'},
        'data_source_url': {'key': 'dataSourceUrl', 'type': 'str'},
        'related_searches': {'key': 'relatedSearches', 'type': '[Query]'},
    }

    def __init__(self, **kwargs):
        super(ImageInsightsImageCaption, self).__init__(**kwargs)
        self.caption = kwargs.get('caption', None)
        self.data_source_url = kwargs.get('data_source_url', None)
        self.related_searches = kwargs.get('related_searches', None)