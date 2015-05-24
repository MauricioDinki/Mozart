from django.utils.translation import ugettext_lazy as _

default_messages = {
    'invalid': _('Inserte un valor valido'),
    'invalid_choice': _('Selecciona una opcion valida'),
    'invalid_image': _('Selecciona un archivo de imagen valido'),
    'max_length': _('Longitud maxima rebasada'),
    'required': _('Este campo es requerido'),
    'blank': _('El campo esta en blanco'),
    'unique': _('Este nombre ya no esta disponible'),
}

custom_messages = {
    'inevent': _('La fecha del evento es invalida'),
    'shevent': _('El evento no puede ser tan corto'),
    'mismatch': _('Los valores no coinciden'),
}

media_messages = {
    'invalid_image': _('Mozart no soporta este formato de imagen'),
    'invalid_audio': _('Mozart no soporta este formato de audio'),
    'invalid_archive': _('Mozart no soporta este formato de archivo'),
}
