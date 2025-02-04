###################################################################################
#
#    Copyright (c) 2017-today MuK IT GmbH.
#
#    This file is part of MuK REST API for Odoo
#    (see https://mukit.at).
#
#    MuK Proprietary License v1.0
#
#    This software and associated files (the "Software") may only be used
#    (executed, modified, executed after modifications) if you have
#    purchased a valid license from MuK IT GmbH.
#
#    The above permissions are granted for a single database per purchased
#    license. Furthermore, with a valid license it is permitted to use the
#    software on other databases as long as the usage is limited to a testing
#    or development environment.
#
#    You may develop modules based on the Software or that use the Software
#    as a library (typically by depending on it, importing it and using its
#    resources), but without copying any source code or material from the
#    Software. You may distribute those modules under the license of your
#    choice, provided that this license is compatible with the terms of the
#    MuK Proprietary License (For example: LGPL, MIT, or proprietary licenses
#    similar to this one).
#
#    It is forbidden to publish, distribute, sublicense, or sell copies of
#    the Software or modified copies of the Software.
#
#    The above copyright notice and this permission notice must be included
#    in all copies or substantial portions of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#    OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
#    THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#    DEALINGS IN THE SOFTWARE.
#
###################################################################################


import os
import json
import urllib
import shutil
import logging
import requests
import unittest
import tempfile

import requests

from odoo import _, SUPERUSER_ID
from odoo.tests import common

from odoo.addons.muk_rest.tests.common import RestfulCase, skip_check_authentication

_path = os.path.dirname(os.path.dirname(__file__))
_logger = logging.getLogger(__name__)


class CommonTestCase(RestfulCase):
    
    @skip_check_authentication()
    def test_modules(self):
        client = self.authenticate()
        self.assertTrue(client.get(self.modules_url))
    
    @skip_check_authentication()
    def test_xmlid(self):
        client = self.authenticate()
        tester = self.env.ref('base.group_user')
        response = client.get(self.xmlid_url, data={'xmlid': 'base.group_user'})
        self.assertTrue(response)
    
    @skip_check_authentication()
    def test_user(self):
        client = self.authenticate()
        response = client.get(self.user_url)
        self.assertTrue(response)
        self.assertTrue(response.json().get('uid'))
    
    @skip_check_authentication()
    def test_userinfo(self):
        client = self.authenticate()
        response = client.get(self.userinfo_url)
        self.assertTrue(response)
        self.assertTrue(response.json().get('name'))
    
    @skip_check_authentication()
    def test_session(self):
        client = self.authenticate()
        response = client.get(self.session_url)
        self.assertTrue(response)
        self.assertTrue(response.json().get('name'))
