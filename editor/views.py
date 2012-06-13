'''
A django view which will basically be an implementation of an wizard.

Created on Jun 12, 2012

@author: tmetsch
'''


from django import shortcuts
from django.contrib.formtools.wizard import views
from editor import charts
import dtrace


class DTraceWizard(views.SessionWizardView):
    '''
    A DTrace wizard which will allow the user to edit, run and see the results
    of an DTrace script.
    '''

    def __init__(self, **kwargs):
        views.SessionWizardView.__init__(self, **kwargs)
        self.agg_data = {}
        self.out_data = ''
        self.chart_type = 'N/A'

    def my_out(self, value):
        '''
        Catches the output from DTrace scripts which are not stored in an
        aggregate.

        value -- some text value.
        '''
        self.out_data += str(value) + '\n'

    def my_walk(self, action, identifier, keys, values):
        '''
        A walker for the DTrace aggregate.

        action -- The DTrace aggregate function.
        identifier -- cpu #.
        keys -- The keys in the aggregate.
        values -- The actual data.
        '''
        if action in [1793, 1794, 1795, 1796, 1797]:
            self.chart_type = 'pie'
            if repr(keys) in self.agg_data:
                self.agg_data[repr(keys)] += values
            else:
                self.agg_data[repr(keys)] = values
        elif action == 1799:
            # quantize
            self.chart_type = 'histogram_quantize'
            res = []
            for item in values:
                # FIXME: 64 because matplotlib has no way of formatting
                # the xaxis in power two scale :-(
                if item[0][0] > 0 and item[0][0] <= item[0][1] and \
                   item[0][0] <= 64:
                    res.append(item)
            self.agg_data[repr(keys)] = res
        elif action == 1800:
            # lquantize
            self.chart_type = 'histogram_lquantize'
            res = []
            for item in values:
                if item[0][0] >= 0:
                    res.append(item)
            self.agg_data[repr(keys)] = res
        else:
            raise AttributeError('This should never happen - Unknown action!')

    def run_dtrace(self, time, script):
        '''
        Will actually run DTrace.

        time -- how long DTrace should run.
        script -- The DTrace script.
        '''
        consumer = dtrace.DTraceConsumer(walk_func=self.my_walk,
                                         out_func=self.my_out)
        consumer.run_script(script, runtime=int(time))
        del(consumer)

    def done(self, form_list, **kwargs):
        data = {}

        # gather data from all forms!
        for form in form_list:
            data.update(form.cleaned_data)

        runtime = data['runtime']
        script = data['script']

        # reset & run dtrace
        self.agg_data = {}
        self.chart_type = ''
        self.run_dtrace(runtime, script)

        # based on chart_type type create chart
        if self.chart_type == 'pie':
            chart = charts.create_pie_chart(self.agg_data)
        elif self.chart_type == 'histogram_quantize':
            # 7 - because 0 - 64...
            xticks = [pow(2, x) for x in range(0, 7)]
            chart = charts.create_quan_chart(self.agg_data, xticks)
        elif self.chart_type == 'histogram_lquantize':
            mini = self.agg_data.values()[0][0][0][0]
            maxi = self.agg_data.values()[0][-1][0][0]
            step = self.agg_data.values()[0][1][0][1] - \
                   self.agg_data.values()[0][1][0][0] + 1

            xticks = range(mini, maxi + step, step)
            chart = charts.create_quan_chart(self.agg_data, xticks)
        else:
            chart = ''

        # render it back to client!
        return shortcuts.render_to_response('output.html', {
            'form_data': self.agg_data,
            'out_data': self.out_data,
            'img_src': chart,
            'script': script
        })
