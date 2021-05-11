import click
from src.cli import pass_context
from src.cli import getDisclaimer

short_help='Runs DAGs from cli'
long_help='This command allows ... TBD.\n\n' \
'<action> - specify one of the following values [list, ...]'


@click.command('taskrunner', short_help=click.style(short_help, fg='green'), epilog=getDisclaimer(), help=click.style(long_help, fg='green'))
@click.argument('action', required=True, metavar='<action>')
@pass_context
def cli(ctx, action):

    if action == 'list':
        ret = True
        if ret is not None:
            ctx.log(ret)

    elif action == '...':
        ctx.log('testing ...')

    else:
        ctx.logerror('Unknown action parameter of ' + action)
