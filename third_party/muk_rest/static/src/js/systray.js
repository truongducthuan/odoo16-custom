/**********************************************************************************
*
*    Copyright (c) 2017-today MuK IT GmbH.
*
*    This file is part of MuK REST API for Odoo
*    (see https://mukit.at).
*
*    MuK Proprietary License v1.0
*
*    This software and associated files (the "Software") may only be used
*    (executed, modified, executed after modifications) if you have
*    purchased a valid license from MuK IT GmbH.
*
*    The above permissions are granted for a single database per purchased
*    license. Furthermore, with a valid license it is permitted to use the
*    software on other databases as long as the usage is limited to a testing
*    or development environment.
*
*    You may develop modules based on the Software or that use the Software
*    as a library (typically by depending on it, importing it and using its
*    resources), but without copying any source code or material from the
*    Software. You may distribute those modules under the license of your
*    choice, provided that this license is compatible with the terms of the
*    MuK Proprietary License (For example: LGPL, MIT, or proprietary licenses
*    similar to this one).
*
*    It is forbidden to publish, distribute, sublicense, or sell copies of
*    the Software or modified copies of the Software.
*
*    The above copyright notice and this permission notice must be included
*    in all copies or substantial portions of the Software.
*
*    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
*    OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
*    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
*    THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
*    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
*    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
*    DEALINGS IN THE SOFTWARE.
*
**********************************************************************************/

odoo.define('muk_rest/static/src/js/systray.js', function (require) {
'use strict';

var core = require('web.core');
var session = require('web.session');
var config = require('web.config');

var SystrayMenu = require('web.SystrayMenu');
var Widget = require('web.Widget');

var QWeb = core.qweb;

var DocsMenu = Widget.extend({
    name: 'muk_rest_docs_menu',
    template:'muk_rest.DocsMenu',
    events: {
    	'click .mk_rest_systray_icon': '_onClickIcon',
    },
    willStart() {
        const acl = this._rpc({
        	route: '/rest/docs/check'
        }).then(docsVisible => {
        	this.isVisible = docsVisible;
        });
        return Promise.all([this._super(...arguments), acl]);
    },
    _onClickIcon(ev) {
        if(this.el.classList.contains('show')) {
        	this.el.classList.remove('show');
        } else {
        	this.el.classList.add('show'); 	
        }
        ev.preventDefault();
    },
});

if (config.isDebug() && !config.device.isMobile) {
	SystrayMenu.Items.push(DocsMenu);
}

return DocsMenu;

});
