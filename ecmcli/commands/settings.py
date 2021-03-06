"""
Display and edit account and/or group settings.
"""

from . import base


class Settings(base.ECMCommand):
    """ Display and edit account and group settings. """

    name = 'settings'
    expands = ','.join([
        'setting'
    ])

    def setup_args(self, parser):
        or_group = parser.add_mutually_exclusive_group()
        or_group.add_argument('--group', metavar='GROUP_ID_OR_NAME')
        or_group.add_argument('--account', metavar='ACCOUNT_ID_OR_NAME')
        parser.add_argument('get_or_set', metavar='GET_OR_SET', nargs='?',
                            help='key or key=value')

    def run(self, args):
        if args.group:
            res = self.api.get_by_id_or_name('groups', args.group)
        elif args.account:
            res = self.api.get_by_id_or_name('account', args.account)
        else:
            res = self.api.ident['account']
        for x in self.api.get_pager(urn=res['settings_bindings'],
                                    expand=self.expands):
            print(x['setting']['name'], x['value'])

command_classes = [Settings]
