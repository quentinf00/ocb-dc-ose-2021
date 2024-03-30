import aprl.module
import aprl.utils
import copernicusmarine
import hydra_zen
import pandas as pd

aprl.utils.register_resolvers()


def month_regex_from_date(min_time="2017-01-01", max_time="2017-12-31"):
    dates = list(set(pd.date_range(min_time, max_time).strftime("%Y%m")))
    return "(" + "|".join(dates) + ")"


def duacs_l3(sat="c2"):
    return f"cmems_obs-sl_glo_phy-ssh_my_{sat}-l3-duacs_PT1S"


b = hydra_zen.make_custom_builds_fn(populate_full_signature=True)

cmems_get_endpoint, cmems_get_cfg = aprl.module.register(
    copernicusmarine.get,
    base_args=dict(
        dataset_id=b(duacs_l3),
        regex=b(month_regex_from_date),
        output_directory="${aprl-mkp:data/downloads/ref}",
        force_download=True,
        overwrite_output_data=True,
    ),
    builds_kwargs=dict(populate_full_signature=False),
    zen_kwargs=dict(exclude="download_file_list"),
)

if __name__ == "__main__":
    cmems_get_endpoint()
