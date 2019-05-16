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


class ModelsResult(Model):
    """Result of query operation to fetch multiple models.

    :param models_property: Collection of models.
    :type models_property:
     list[~azure.cognitiveservices.formrecognizer.models.ModelResult]
    """

    _attribute_map = {
        'models_property': {'key': 'models', 'type': '[ModelResult]'},
    }

    def __init__(self, *, models_property=None, **kwargs) -> None:
        super(ModelsResult, self).__init__(**kwargs)
        self.models_property = models_property