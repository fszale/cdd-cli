import os
import sys
import click
from version import __version__
import datetime


CONTEXT_SETTINGS = dict(auto_envvar_prefix='COMPLEX')


def getDisclaimer():
    msg = 'Copyright (c) ' + str(datetime.datetime.now().year) + ' Your Organization. All rights reserved. Trade\n' + \
           'Secret, Confidential and Proprietary. Any dissemination outside of\n' + \
           'Your Organization is strictly prohibited.'
    return click.style(msg, fg='cyan')


def showVersion(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('cddcli ' + __version__)
    ctx.exit()


class Context(object):

    def __init__(self):
        self.verbose = False
        self.debug = False

    def log(self, msg, *args):
        """Logs a message to stderr."""
        if args:
            msg %= args
        click.echo(click.style(msg, fg='white'), file=sys.stderr)

    def logerror(self, msg, *args):
        """Logs a message to stderr."""
        if args:
            msg %= args
        click.echo(click.style(msg, fg='red'), file=sys.stderr)

    def vlog(self, msg, *args):
        """Logs a message to stderr only if verbose is enabled."""
        if self.verbose:
            self.log(click.style(msg, fg='yellow'), *args)


pass_context = click.make_pass_decorator(Context, ensure=True)
cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'cmd'))


class ComplexCLI(click.MultiCommand):

    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith('.py') and \
               filename.startswith('cmd_'):
                rv.append(filename[4:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        try:
            if sys.version_info[0] == 2:
                name = name.encode('ascii', 'replace')
            mod = __import__('src.cmd.cmd_' + name,
                                 None, None, ['cli'])
        except ImportError:
            return
        return mod.cli


@click.command(cls=ComplexCLI, context_settings=CONTEXT_SETTINGS, epilog=getDisclaimer(), help=click.style('A product of your mind.', fg='cyan'))
@click.option('-v', '--verbose', is_flag=True, help='Enables verbose mode.')
@click.option('--debug/--no-debug', default=False, help='Do we really need to explain this one?')
@click.option('-V', '--version', is_eager=True, is_flag=True, expose_value=False, help='Show version and exit.', callback=showVersion)
@pass_context
def cli(ctx, verbose, debug):
    ctx.verbose = verbose
    ctx.debug = debug


if __name__ == '__main__':
    cli()
