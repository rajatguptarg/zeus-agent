#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Author: Rajat Gupta
Description:
"""

import json
import logging
from slack import WebClient

from samantha import config


__all__ = ['SlackWebClient']

logger = logging.getLogger(__name__)


class SlackWebClient(object):
    """
    Web client for uploading data to slack
    """
    def __init__(self):
        opts = config.get_slack_config()
        self._token = opts.bot_token
        self._client = WebClient(token=self._token, run_async=True)

    def send_text(self, text: str, channel: str):
        """
        Send messsage as text in channel
        """
        response = self._client.chat_postMessage(
                channel=channel, text=text)
        logger.info("Sent message: %s to slack with response %s" % (text, str(response)))
        return response

    def send_blocks(self, block: dict, channel: str):
        """
        Send blocks to the channel
        """
        response = self._client.chat_postMessage(
                blocks=json.dumps(block), channel=channel)
        return response

    def send_file(self, file_path: str, channel: str, filename: str, filetype: str,
            title: str):
        """
        Send file in the channel
        """
        response = self._client.files_upload(
                channels=channel, file=file_path, filename=filename,
                filetype=filetype, title=title)
        return response

    def send_text_as_file(self, content: str, channel: str, filename: str, filetype: str,
            title: str):
        """
        Send text as a file in the channel
        """
        response = self._client.files_upload(
                channels=channel, content=content, filename=filename,
                filetype=filetype, title=title)
        return response
