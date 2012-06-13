'''
This module will allow the creation of charts.

Created on Jun 12, 2012

@author: tmetsch
'''
from mpl_toolkits.mplot3d import axes3d
import pylab
import random


def create_pie_chart(data):
    '''
    Create a pie chart and return filename.

    wants data in key, value format stored in a dict [('foo', value), ...].

    data -- the data.
    '''
    pylab.figure(1, figsize=(6, 6))
    labels = data.keys()
    fracs = data.values()

    pylab.pie(fracs, labels=labels, autopct='%.2f%%', shadow=False)

    name = 'static/' + str(random.randint(0, 9999999)) + '.png'
    pylab.savefig(name)
    pylab.close()
    return name


def create_quan_chart(data, xticks):
    '''
    Create a 3D histogram and return filename of the image.

    needs data in form of an dict with keys and values in it:
    [((begin, end), valu),...].

    data -- the data.
    xticks -- the x-axis ticks (e.g. [0,2,4,6,8...].
    '''
    fig = pylab.figure(1, figsize=(10, 6))

    xaxis = axes3d.Axes3D(fig)

    posval = []
    for i in range(0, len(data.keys())):
        posval.append(i)

    for key, zval in zip(data.keys(), posval):
        yaxes = []
        for item in data[key]:
            if item[0][0] < 0:
                continue
            else:
                yaxes.append(int(item[1]))
        xaxis.bar(xticks, yaxes, zs=zval, zdir='y', alpha=0.8, label="foo")

    group_labels = data.keys()

    xaxis.set_yticklabels(group_labels)

    xaxis.set_xlabel('Value')
    xaxis.set_zlabel('Count')

    name = 'static/' + str(random.randint(0, 9999999)) + '.png'
    pylab.savefig(name)
    pylab.close()
    return name
