import holoviews as hv
import janitor
import pandas as pd
from bokeh.embed import components
from jinja2 import Environment, Template
from pathlib import Path

hv.extension("bokeh")


def load_finches(data_dir):
    df_old = (
        pd.read_csv(data_dir / "finch_beaks_1975.csv")
        .rename_column("Beak length, mm", "beak_length")
        .rename_column("Beak depth, mm", "beak_depth")
    )
    df_old["year"] = 1975

    df_new = (
        pd.read_csv(data_dir / "finch_beaks_2012.csv")
        .rename_column("blength", "beak_length")
        .rename_column("bdepth", "beak_depth")
    )
    df_new["year"] = 2012

    df = (
        pd.concat([df_old, df_new])
        .encode_categorical("species")
        .encode_categorical("year")
    )

    return df


def scatter_finches(df):
    ds = hv.Dataset(df, vdims=["beak_length", "beak_depth"], kdims=["species", "year"])
    opts = {
        "Scatter": {
            "width": 200,
            "height": 200,
            "size": 10,
            "alpha": 0.3,
            "tools": ["pan", "hover"],
        }
    }
    scatter_facet = (
        ds.to(hv.Scatter, "beak_length", "beak_depth")
        .grid(["species", "year"])
        .options(opts)
    )

    return scatter_facet


def finch_components(scatter_facet):
    renderer = hv.renderer("bokeh")
    plot = renderer.get_plot(scatter_facet).state
    script, div = components(plot)
    return script, div


def write_components(elements: dict):
    with open("./slides.html", "r+") as f:
        template = Template(f.read())

    with open("./docs/index.html", "w+") as f:
        f.write(template.render(elements=elements))


def load_hockey_traces(data_dir: Path, pooled: bool):
    if pooled:
        df = pd.read_csv(data_dir / "goalie_pool_posterior.csv")
    else:
        df = pd.read_csv(data_dir / "goalie_nopool_posterior.csv")

    df = df.filter_on(df["iter"] % 10 == 0)
    return df


def make_posterior_trace(df):
    players = ["Dylan Ferguson", "Scott Foster", "Jake Allen"]

    opts = {"BoxWhisker": {"width": 400, "height": 400, "tools": ["pan", "hover"]}}

    ds = hv.Dataset(df, kdims=["Player"], vdims=["p"])
    curve = (
        ds.select(Player=players)
        .to(hv.BoxWhisker, kdims=["Player"], vdims=["p"])
        .options(opts)
    )
    return curve


def render_posterior_trace(curve):
    renderer = hv.renderer("bokeh")
    plot = renderer.get_plot(curve).state
    script, div = components(plot)
    return script, div
