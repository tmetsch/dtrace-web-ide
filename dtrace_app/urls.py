'''
URL mapping configuration!
'''

from dtrace_app import settings
from django.conf.urls import patterns

from editor.form import ScriptForm, SelectForm
from editor.views import DTraceWizard

urlpatterns = patterns('',
    (r'^$', DTraceWizard.as_view([ScriptForm, SelectForm])),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
     {
      'document_root': settings.STATIC_ROOT
    }),
)
