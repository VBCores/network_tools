import click

from .controller import srv_port_from_name, msg_port_from_name, id_from_name

try:
    from _utils import title, info, err
except ImportError:
    title = info = err = lambda v: v


def print_table(rows):
    max_first_len = max((len(row[0]) for row in rows))
    for first, *other in rows:
        print(first.ljust(max_first_len), end=": ")
        print(*other)


@click.group()
def cli():
    pass


@cli.command("all")
@click.argument("name", required=True)
def generate_all(name):
    print(title(f'Порты и id для строки "{name}"'))
    print_table(
        [
            (info("Service port"), srv_port_from_name(name)),
            (info("Message port"), msg_port_from_name(name)),
            (info("Node ID"), id_from_name(name)),
        ]
    )


@cli.command("srv")
@click.argument("name", required=True)
def service(name):
    print(srv_port_from_name(name))


@cli.command("msg")
@click.argument("name", required=True)
def message(name):
    print(msg_port_from_name(name))


@cli.command("id")
@click.argument("name", required=True)
def node_id(name):
    print(id_from_name(name))


if __name__ == "__main__":
    cli()
