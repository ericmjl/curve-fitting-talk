import click
import pyqrcode as pq
from pyqrcode.qrspecial import QrMeCard
from pathlib import Path
from functions import load_hockey_traces, make_posterior_trace, render_posterior_trace, write_components

img_dir = Path("assets/images")
data_dir = Path("notebooks/data")


@click.group()
def main():
    pass


@main.command()
def slidesqr():
    url = "https://ericmjl.github.io/curve-fitting-talk/"
    pq.create(url).png(img_dir / "talk.png", scale=10)

    url = "https://en.wikipedia.org/wiki/Darwin%27s_finches"
    pq.create(url).png(img_dir / "finches.png", scale=10)

    url = "https://www.youtube.com/watch?v=s0S6HFdPtlA"
    pq.create(url).png(img_dir / "pydata.png", scale=10)


@main.command()
def contactqr():
    name = "Eric J. Ma"
    url = "https://ericmjl.github.io"

    mecard = QrMeCard(name=name, url=url)
    pq.create(str(mecard)).png(img_dir / "ericmjl.png", scale=10)


@main.command()
def render():
    elements = dict()

    df = load_hockey_traces(data_dir, pooled=False)
    curve = make_posterior_trace(df)
    script, div = render_posterior_trace(curve)
    elements['hockey_unpooled_script'] = script
    elements['hockey_unpooled_div'] = div

    df = load_hockey_traces(data_dir, pooled=True)
    curve = make_posterior_trace(df)
    script, div = render_posterior_trace(curve)
    elements['hockey_pooled_script'] = script
    elements['hockey_pooled_div'] = div

    write_components(elements)



if __name__ == "__main__":
    main()
