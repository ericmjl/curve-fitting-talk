import click
import pyqrcode as pq
from pyqrcode.qrspecial import QrMeCard


@click.group()
def main():
    pass


@main.command()
def slidesqr():
    url = 'https://ericmjl.github.io/curve-fitting-talk/'
    pq.create(url).png('images/talk.png', scale=10)


@main.command()
def contactqr():
    name = 'Eric J. Ma'
    url = 'https://ericmjl.github.io'
    note = 'DIGILITY 2018, speaker, Bayesian.'

    mecard = QrMeCard(name=name, url=url, memo=note)
    pq.create(str(mecard)).png('images/ericmjl.png', scale=10)


if __name__ == '__main__':
    main()
