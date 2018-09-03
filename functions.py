from jinja2 import Environment, Template


import pandas as pd
import janitor
import holoviews as hv
from bokeh.embed import components

hv.extension("bokeh")


def load_data(data_dir):
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


def hv_scatter(df):
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


def hv_render(scatter_facet):
    renderer = hv.renderer("bokeh")
    plot = renderer.get_plot(scatter_facet).state
    script, div = components(plot)
    with open("./docs/slides.html", "r+") as f:
        template = Template(f.read())

    with open("./docs/index.html", "w+") as f:
        f.write(template.render(scatter_script=script, scatter_div=div))
