import click
import pyqrcode as pq
from pyqrcode.qrspecial import QrMeCard
from pathlib import Path
from functions import load_data, hv_scatter, hv_render

img_dir = Path("assets/images")
data_dir = Path("notebooks/data")


@click.group()
def main():
    pass


@main.command()
def slidesqr():
    url = 'https://ericmjl.github.io/curve-fitting-talk/'
    pq.create(url).png(img_dir / 'talk.png', scale=10)


@main.command()
def contactqr():
    name = 'Eric J. Ma'
    url = ('https://ericmjl.github.io')

    mecard = QrMeCard(name=name, url=url)
    pq.create(str(mecard)).png(img_dir / 'ericmjl.png', scale=10)


@main.command()
def render():
    df = load_data(data_dir)
    plot = hv_scatter(df)
    hv_render(plot)

if __name__ == '__main__':
    main()
