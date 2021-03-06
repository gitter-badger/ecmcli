"""
Reboot connected router(s).
"""

from . import base


class Reboot(base.ECMCommand):
    """ Reboot connected router(s). """

    name = 'reboot'

    def setup_args(self, parser):
        self.add_argument('idents', metavar='ROUTER_ID_OR_NAME', nargs='*',
                          complete=self.make_completer('routers', 'name'))
        self.add_argument('-f', '--force', action='store_true')

    def run(self, args):
        if args.idents:
            routers = [self.api.get_by_id_or_name('routers', r)
                       for r in args.idents]
        else:
            routers = self.api.get_pager('routers')
        for x in routers:
            if not args.force and \
               not base.confirm("Reboot %s (%s)" % (x['name'], x['id']),
                                exit=False):
                continue
            print("Rebooting: %s (%s)" % (x['name'], x['id']))
            self.api.put('remote', '/control/system/reboot', 1, timeout=0,
                         id=x['id'])

command_classes = [Reboot]
