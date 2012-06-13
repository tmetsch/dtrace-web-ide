Web editor for DTrace based on Python
==============

This is a Python &amp; web based IDE for DTrace with Data Visualizations. Based
on the script the user provided this tool will create some graphs and return
some visualizations.

It basically acts like the command 'dtrace' - which is actually a consumer
itself - just web based. So maybe the better name for this project would be 
DTrace web consumer.

Prerequisites
-------------

 1. First install the python-dtrace consumer - please note that you currently
    need to fork it from [github](https://github.com/tmetsch/python-dtrace).
 1. Install numpy which is a requirement of matplotlib
 1. Install matplotlib

Running the editor
------------------

First you will need to create a simple database (sqlite). The django users
among you will know why :-)

    python manage.py syncdb

This only needs to be done once. When done you can run the editor:

    python manage.py runserver

Go to http://localhost:8000 and you will see this web based DTrace consumer.
Note that this is not the way it is supposed to run in a production system.

Notes
-----

Thanks to the folks whom created [editarea](http://www.cdolivet.com/editarea/)
which is used to get the syntax highlighting.

WARNING
=======
Use as own risk - no warranties - this is still very much work in progress -
please see: [issues](https://github.com/tmetsch/dtrace-web-ide/issues 'Issues')

(c) 2012 Thijs Metsch
