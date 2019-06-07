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


class PowerShellCommandResult(Model):
    """Results from invoking a PowerShell command.

    :param message_type: The type of message.
    :type message_type: int
    :param foreground_color: The HTML color string representing the foreground
     color.
    :type foreground_color: str
    :param background_color: The HTML color string representing the background
     color.
    :type background_color: str
    :param value: Actual result text from the PowerShell Command.
    :type value: str
    :param prompt: The interactive prompt message.
    :type prompt: str
    :param exit_code: The exit code from a executable that was called from
     PowerShell.
    :type exit_code: int
    :param id: ID of the prompt message.
    :type id: int
    :param caption: Text that precedes the prompt.
    :type caption: str
    :param message: Text of the prompt.
    :type message: str
    :param descriptions: Collection of PromptFieldDescription objects that
     contains the user input.
    :type descriptions:
     list[~azure.mgmt.servermanager.models.PromptFieldDescription]
    """

    _attribute_map = {
        'message_type': {'key': 'messageType', 'type': 'int'},
        'foreground_color': {'key': 'foregroundColor', 'type': 'str'},
        'background_color': {'key': 'backgroundColor', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'prompt': {'key': 'prompt', 'type': 'str'},
        'exit_code': {'key': 'exitCode', 'type': 'int'},
        'id': {'key': 'id', 'type': 'int'},
        'caption': {'key': 'caption', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'descriptions': {'key': 'descriptions', 'type': '[PromptFieldDescription]'},
    }

    def __init__(self, *, message_type: int=None, foreground_color: str=None, background_color: str=None, value: str=None, prompt: str=None, exit_code: int=None, id: int=None, caption: str=None, message: str=None, descriptions=None, **kwargs) -> None:
        super(PowerShellCommandResult, self).__init__(**kwargs)
        self.message_type = message_type
        self.foreground_color = foreground_color
        self.background_color = background_color
        self.value = value
        self.prompt = prompt
        self.exit_code = exit_code
        self.id = id
        self.caption = caption
        self.message = message
        self.descriptions = descriptions