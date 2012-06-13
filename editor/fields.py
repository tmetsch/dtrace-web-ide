'''
A set of Django form fields which are used in the wizard.

Created on Jun 12, 2012

@author: tmetsch
'''

from django import forms
from django.core import exceptions
import dtrace


class ScriptField(forms.CharField):
    '''
    A DTrace char field.

    Will compile the script upon validation.
    '''

    def to_python(self, value):
        if not value:
            return ''
        return value

    def validate(self, value):
        super(ScriptField, self).validate(value)

        try:
            consumer = dtrace.DTraceConsumer()
            consumer.compile_script(value)
        except Exception as ex:
            raise exceptions.ValidationError(ex)


class TimeField(forms.IntegerField):
    '''
    A field which allows inputs of > 0.
    '''

    def to_python(self, value):
        if not value:
            return 2
        return value

    def validate(self, value):
        super(TimeField, self).validate(value)
        if int(value) <= 0:
            raise exceptions.ValidationError('Needs to be > 0.')
