# $Id: install.py 1651 2017-01-16 18:10:37Z mwall $
# installer for cmon
# Copyright 2014 Matthew Wall

from setup import ExtensionInstaller

def loader():
    return ComputerMonitorInstaller()

class ComputerMonitorInstaller(ExtensionInstaller):
    def __init__(self):
        super(ComputerMonitorInstaller, self).__init__(
            version="0.16",
            name='cmon',
            description='Collect and display computer health indicators.',
            author="Matthew Wall",
            author_email="mwall@users.sourceforge.net",
            process_services='user.cmon.ComputerMonitor',
            config={
                'ComputerMonitor': {
                    'data_binding': 'cmon_binding'},
                'DataBindings': {
                    'cmon_binding': {
                        'database': 'cmon_sqlite',
                        'table_name': 'archive',
                        'manager': 'weewx.manager.DaySummaryManager',
                        'schema': 'user.cmon.schema'}},
                'Databases': {
                    'cmon_sqlite': {
                        'database_name': 'cmon.sdb',
                        'driver': 'weedb.sqlite'}},
                'StdReport': {
                    'cmon': {
                        'skin': 'cmon',
                        'HTML_ROOT': 'cmon'}}},
            files=[('bin/user',
                    ['bin/user/cmon.py']),
                   ('skins/cmon',
                    ['skins/cmon/skin.conf',
                     'skins/cmon/index.html.tmpl']),
                   ]
            )
