# Plot finite size effects
import matplotlib.pyplot as plt
import pandas as pd
import sys, os
import style
import itertools as it

from matplotlib import rc
rc('font',**style.fontstyle)
rc('text', usetex=True)

fnamevec_ed = ["data/J_1/ed/L_04x04/data_L_04-04_J_1.00_hmin_0.00_hmax_5.00_nsteps_051_type_ed.csv",
    "data/J_1/ed/L_05x05/data_L_05-05_J_1.00_hmin_0.00_hmax_5.00_nsteps_051_type_ed.csv",
]
fnamevec_mps=[
    "data/J_1/mps/L_04x04/data_L_04-04_J_1.00_hmin_0.00_hmax_5.00_nsteps_051_type_mps_chi_500.csv",
    "data/J_1/mps/L_05x05/data_L_05-05_J_1.00_hmin_0.00_hmax_5.00_nsteps_051_type_mps_chi_500.csv",
    "data/J_1/mps/L_06x06/data_L_06-06_J_1.00_hmin_0.00_hmax_5.00_nsteps_051_type_mps_chi_500.csv",
    "data/J_1/mps/L_07x07/data_L_07-07_J_1.00_hmin_0.00_hmax_5.00_nsteps_051_type_mps_chi_500.csv",
    "data/J_1/mps/L_08x08/data_L_08-08_J_1.00_hmin_0.00_hmax_5.00_nsteps_051_type_mps_chi_500.csv"
]

fnamevec_mbr = [ 
    "data/J_1/mbr/deg_01/L_04x04/data_L_04-04_J_1.00_hmin_0.00_hmax_5.00_nsteps_051_type_mbr_chi_001.csv",
    "data/J_1/mbr/deg_01/L_05x05/data_L_05-05_J_1.00_hmin_0.00_hmax_5.00_nsteps_051_type_mbr_chi_001.csv",
    "data/J_1/mbr/deg_01/L_06x06/data_L_06-06_J_1.00_hmin_0.00_hmax_5.00_nsteps_051_type_mbr_chi_001.csv",
    "data/J_1/mbr/deg_01/L_07x07/data_L_07-07_J_1.00_hmin_0.00_hmax_5.00_nsteps_051_type_mbr_chi_001.csv",
    "data/J_1/mbr/deg_01/L_08x08/data_L_08-08_J_1.00_hmin_0.00_hmax_5.00_nsteps_051_type_mbr_chi_001.csv",

    "data/J_1/mbr/deg_02/L_04x04/data_L_04-04_J_1.00_hmin_0.00_hmax_5.00_nsteps_051_type_mbr_chi_002.csv",
    "data/J_1/mbr/deg_02/L_05x05/data_L_05-05_J_1.00_hmin_0.00_hmax_5.00_nsteps_051_type_mbr_chi_002.csv",
    "data/J_1/mbr/deg_02/L_06x06/data_L_06-06_J_1.00_hmin_0.00_hmax_5.00_nsteps_051_type_mbr_chi_002.csv",
    "data/J_1/mbr/deg_02/L_07x07/data_L_07-07_J_1.00_hmin_0.00_hmax_5.00_nsteps_051_type_mbr_chi_002.csv",
    "data/J_1/mbr/deg_02/L_08x08/data_L_08-08_J_1.00_hmin_0.00_hmax_5.00_nsteps_051_type_mbr_chi_002.csv",

    "data/J_1/mbr/deg_03/L_04x04/data_L_04-04_J_1.00_hmin_0.00_hmax_5.00_nsteps_051_type_mbr_chi_003.csv",
    "data/J_1/mbr/deg_03/L_05x05/data_L_05-05_J_1.00_hmin_0.00_hmax_5.00_nsteps_051_type_mbr_chi_003.csv",
    "data/J_1/mbr/deg_03/L_06x06/data_L_06-06_J_1.00_hmin_0.00_hmax_5.00_nsteps_051_type_mbr_chi_003.csv",
    # "data/J_1/mbr/deg_03/L_07x07/data_L_07-07_J_1.00_hmin_0.00_hmax_5.00_nsteps_051_type_mbr_chi_003.csv",
    # "data/J_1/mbr/deg_03/L_08x08/data_L_08-08_J_1.00_hmin_0.00_hmax_5.00_nsteps_051_type_mbr_chi_003.csv",
]

fnamevec = it.chain(fnamevec_ed,fnamevec_mps,fnamevec_mbr)

dfvec = []
for fname in fnamevec:
    if os.path.exists(fname):
        dfvec.append(pd.read_csv(fname, index_col=0))
    else:
        print(f"File {fname} does not exist. Skipping. ",file=sys.stderr)
        sys.exit(1)

df = pd.concat(dfvec)
df["degree"] = df["degree"].fillna(-1)
df["degree"] = df["degree"].astype(int)
df["degree_str"] = df["degree"].apply(lambda x: f" - {x:d}" if x >0 else "")
df["type_plot"] = df["type"] + df["degree_str"]

f, ax = plt.subplots(1, 1, figsize=style.figsize)

# Plot MPS
df_mps = df[(df["type"] == "mps") & (df["nx"] == 8)]
if len(df_mps) > 0:
    ax.plot(
        df_mps["h"],
        df_mps["energy_per_site"],
        "^",
        label="MPS, L = 8",
        **style.create_markers("C1"),
    )

# Plot MBR
# colorvec = ["5d169cff","6b28a7ff","9747deff","ac60efff","b38ad9ff"]
colorvec = ["b38ad9ff","ac60efff","9747deff","6b28a7ff","5d169cff"]

for i,l in enumerate(range(4,9)):
    df_mbr = df[(df["type"] == "mbr") & (df["nx"] == l)]
    if len(df_mbr) > 0:
        ax.plot(
            df_mbr[df_mbr["degree"] == 3]["h"],
            df_mbr[df_mbr["degree"] == 3]["energy_per_site"],
            'P',
            label=f"MBR - 3, L = {l} ",
            **style.create_markers(f"#{colorvec[i]}"),
        )

ax.set_ylabel("$E/N$")
ax.set_xlabel("$h$")
ax.legend(**style.fontstyle_legend)

f.tight_layout()
f.savefig("finite_size_scaled.pdf",bbox_inches="tight")