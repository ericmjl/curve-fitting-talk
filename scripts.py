import click
import pyqrcode as pq
from pyqrcode.qrspecial import QrMeCard
from pathlib import Path
import pandas as pd
import holoviews as hv
from functions import (
    load_hockey_traces,
    make_posterior_trace,
    render_posterior_trace,
    write_components,
)

img_dir = Path("assets/images")
data_dir = Path("notebooks/data")

hv.extension("bokeh")


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
    data_dir = Path("./notebooks") / "data"
    data = pd.read_csv(data_dir / "hockey-goalie.csv", skiprows=1)
    df = data.groupby("Player").sum().reset_index()
    df["SV%_adj"] = df["SV%"] / data.groupby("Player").size().values
    df["Player"] = df["Player"].apply(lambda x: x.split("\\")[0])

    df1 = load_hockey_traces(data_dir, pooled=False)
    curve1 = make_posterior_trace(df1)
    script, div = render_posterior_trace(curve1)
    elements["hockey_unpooled_script"] = script
    elements["hockey_unpooled_div"] = div

    df2 = load_hockey_traces(data_dir, pooled=True)
    curve2 = make_posterior_trace(df2)
    script, div = render_posterior_trace(curve2)
    elements["hockey_pooled_script"] = script
    elements["hockey_pooled_div"] = div

    script, div = render_posterior_trace((curve1 + curve2))
    elements["hockey_combined_script"] = script
    elements["hockey_combined_div"] = div

    shrinkage = pd.DataFrame()
    shrinkage["No Pooling"] = df1.groupby("Player").mean()["p"]
    shrinkage["Partial Pooling"] = df2.groupby("Player").mean()["p"]
    shrinkage["Full Pooling"] = [df["SV%_adj"].mean()] * len(df)
    shrinkage = shrinkage.reset_index()
    shrinkage = (
        shrinkage.melt(id_vars="Player")
        .rename_column("variable", "Pooling")
        .rename_column("value", "p")
    )
    ds = hv.Dataset(shrinkage, vdims=["p"], kdims=["Pooling", "Player"])
    curve3 = ds.to(hv.Curve).overlay("Player").options({'Curve': {'width': 600}})
    script, div = render_posterior_trace(curve3)
    elements["hockey_shrinkage_script"] = script
    elements["hockey_shrinkage_div"] = div

    write_components(elements)


if __name__ == "__main__":
    main()
