"""
Bootstrap the shell and commands and then run either one.
"""

import importlib
import pkg_resources
import sys
from . import api
from .commands import base

command_modules = [
    'accounts',
    'alerts',
    'config',
    'flashleds',
    'groups',
    'logs',
    'reboot',
    'routers',
    'settings',
    'shell',
    'users',
    'wanrate'
]


class ECMRoot(base.ECMCommand):
    """ ECM Command Line Interface

    This utility represents a collection of sub-commands to perform against
    the Cradlepoint ECM service.  You must already have a valid ECM
    username/password to use this tool.  For more info go to
    https://cradlepointecm.com/. """

    name = 'ecm'

    def setup_args(self, parser):
        distro = pkg_resources.get_distribution('ecmcli')
        self.add_argument('--api_username')
        self.add_argument('--api_password')
        self.add_argument('--api_account', help='Limit activity to this '
                          'account')
        self.add_argument('--api_site',
                          help='E.g. https://cradlepointecm.com')
        self.add_argument('--version', action='version',
                          version=distro.version)

    def prerun(self, args):
        if args.api_account:
            account = self.api.get_by_id_or_name('accounts', args.api_account)
            self.api.account = account['id']
        super().prerun(args)

    def run(self, args):
        self.shell()


def main():
    root = ECMRoot(api=api.ECMService())
    for modname in command_modules:
        module = importlib.import_module('.%s' % modname, 'ecmcli.commands')
        for Command in module.command_classes:
            root.add_subcommand(Command)
    args = root.argparser.parse_args()
    root.api.connect(args.api_site, username=args.api_username,
                     password=args.api_password)
    try:
        root(args)
    except KeyboardInterrupt:
        sys.exit(1)
