#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

regex_sentences = {
    'numbres_and_letters': '^[a-zA-Z0-9_áéíóúñ\s]*$',
}

custom_error_messages = {
    'blank': _('This field can not be blank'),
    'unique': _("There is a %(model_name)s with this %(field_label)s already registred"),
    'inevent': _('101'),
    'shevent': _('102'),
    'mismatch': _('103'),
    'invalid_login': _('104'),
    'inactive_account': _('This account is inactive'),
    'incorrect_password': _('The password is incorrect'),
}

media_messages = {
    'invalid_archive': _('201'),
    'invalid_audio': _('202'),
    'invalid_image': _('203'),
}
