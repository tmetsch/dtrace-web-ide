'''
A set of forms. Those will be embedded in the wizard.

Created on Jun 12, 2012

@author: tmetsch
'''

from django import forms
from editor import fields


class ScriptForm(forms.Form):
    '''
    A simple form for the DTrace script editor.
    '''
    script = fields.ScriptField(widget=forms.Textarea(attrs={'cols': 80,
                                                             'rows': 20}),
                                initial='/*\n * Syscall count by syscall\
                                         \n */\nsyscall:::entry { \
                                         \n\t@num[probefunc] = count();\n}')
    script.help_text = 'Please provide you DTrace script here.'
#                                initial='syscall::read:entry {\
#                                        \n\t@dist[execname] = quantize(arg0);\
#                                        \n}')


class SelectForm(forms.Form):
    '''
    A form where runtime options for DTrace can be selected.
    '''
    runtime = fields.TimeField(initial='2')
    runtime.help_text = 'This is the time that the Python based DTrace' \
                        ' Consumer will aggregate data (> 0!).'
