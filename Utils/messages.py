from django.utils.translation import ugettext_lazy as _

default_messages = {
    'blank': _('001'),
    'invalid': _('002'),
    'invalid_choice': _('003'),
    'invalid_image': _('004'),
    'max_length': _('005'),
    'required': _('006'),
    'unique': _('007'),
}


custom_messages = {
    'inevent': _('101'),
    'shevent': _('102'),
    'mismatch': _('103'),
    'invalid_login': _('104'),
    'inactive_account': _('105'),
    'incorrect_password': _('106'),
}

media_messages = {
    'invalid_archive': _('201'),
    'invalid_audio': _('202'),
    'invalid_image': _('203'),
}
