#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

regex_sentences = {
    'numbres_and_letters_special': '^[a-zA-Z0-9_áéíóúñ\s]*$',
    'numbres_and_letters': '^[a-zA-Z0-9]*$',
    'email': '^[\w.@+-]+$',
    'zip_code': '^[0-9\-]*$',
}

custom_error_messages = {
    'blank': _('This field can not be blank'),
    'unique': _("There is a %(model_name)s with this %(field_label)s already registred"),
    'inevent': _('101'),
    'shevent': _('102'),
    'mismatch': _('Passwords do not match'),
    'invalid_login': _('The username or password are incorrect'),
    'inactive_account': _('This account is inactive'),
    'incorrect_password': _('The password is incorrect'),
}

media_messages = {
    'invalid_archive': _('201'),
    'invalid_audio': _('202'),
    'invalid_image': _('203'),
}

success_messages = {
    'event_create': _('Event created successfully'),
    'user_update': _('Profile updated successfully'),
    'work_create': _('Work created successfully'),
    'work_update': _('Work updated successfully'),
}

not_found_messages = {
    '404_user': _("Thers any user with this username"),
    '404_work_category': _("Thers any work with this category")
}

# CHOICES

DAYS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('13', '13'),
    ('14', '14'),
    ('15', '15'),
    ('16', '16'),
    ('17', '17'),
    ('18', '18'),
    ('19', '19'),
    ('20', '20'),
    ('21', '21'),
    ('22', '22'),
    ('23', '23'),
    ('24', '24'),
    ('25', '25'),
    ('26', '26'),
    ('27', '27'),
    ('28', '28'),
    ('29', '29'),
    ('30', '30'),
    ('31', '31'),
)

MONTHS = (
    ('january', _('January')),
    ('february', _('February')),
    ('march', _('March')),
    ('april', _('April')),
    ('may', _('May')),
    ('june', _('June')),
    ('july', _('July')),
    ('august', _('August')),
    ('september', _('September')),
    ('october', _('October')),
    ('november', _('November')),
    ('december', _('December')),
)

SEXUALITY = (
    ('male', _('Male')),
    ('female', _('Female')),
)

USER_TYPE = (
    ('artist', _('Artist')),
    ('promoter', _('Promoter')),
)
