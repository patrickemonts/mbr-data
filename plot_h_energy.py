# Plot energy over field
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

    "data/J_1/mbr/deg_04/L_04x04/data_L_04-04_J_1.00_hmin_0.00_hmax_5.00_nsteps_051_type_mbr_chi_004.csv",

    "data/J_1/mbr/deg_05/L_04x04/data_L_04-04_J_1.00_hmin_0.00_hmax_5.00_nsteps_051_type_mbr_chi_005.csv",
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

nx = 4

f,ax = plt.subplots(1,1,figsize=style.figsize)
# Plot ED
df_ed = df[(df["type"] == "ed") & (df["nx"] == nx)]
ax.plot(df_ed["h"], df_ed["energy_per_site"], '-', label="ED")

# Plot MPS
# df_mps = df[(df["type"] == "mps") & (df["nx"] == nx)]
# ax.plot(df_mps["h"], df_mps["energy"], "o", label="ED", **style.create_markers("C1"))

# Plot MBR
df_mbr = df[(df["type"] == "mbr") & (df["nx"] == nx)]
ax.plot(
    df_mbr[df_mbr["degree"] == 1]["h"],
    df_mbr[df_mbr["degree"] == 1]["energy_per_site"],
    'P',
    label="MBR - 1",
    **style.create_markers("C2"),
)
ax.plot(
    df_mbr[df_mbr["degree"] == 2]["h"],
    df_mbr[df_mbr["degree"] == 2]["energy_per_site"],
    'P',
    label="MBR - 2",
    **style.create_markers("C3"),
)
ax.plot(
    df_mbr[df_mbr["degree"] == 3]["h"],
    df_mbr[df_mbr["degree"] == 3]["energy_per_site"],
    'P',
    label="MBR - 3",
    **style.create_markers("C4"),
)
ax.plot(
    df_mbr[df_mbr["degree"] == 4]["h"],
    df_mbr[df_mbr["degree"] == 4]["energy_per_site"],
    'P',
    label="MBR - 4",
    **style.create_markers("C5"),
)
ax.plot(
    df_mbr[df_mbr["degree"] == 5]["h"],
    df_mbr[df_mbr["degree"] == 5]["energy_per_site"],
    'P',
    label="MBR - 5",
    **style.create_markers("C6"),
)

ax.legend(**style.fontstyle_legend)
ax.set_xlabel("$h$")
ax.set_ylabel("$E/N$")

# inset order: left, bottom, width, height
ax_inset = ax.inset_axes([0.12, 0.17, 0.40, 0.40])

ax_inset.axhline(0,color="C0")
ax_inset.plot(
    df_mbr[df_mbr["degree"] == 1]["h"],
    df_mbr[df_mbr["degree"] == 1]["energy_per_site"]-df_ed["energy_per_site"],
    'P',
    label="MBR - 1",
    **style.create_markers("C2"),
)
ax_inset.plot(
    df_mbr[df_mbr["degree"] == 2]["h"],
    df_mbr[df_mbr["degree"] == 2]["energy_per_site"]-df_ed["energy_per_site"],
    'P',
    label="MBR - 2",
    **style.create_markers("C3"),
)
ax_inset.plot(
    df_mbr[df_mbr["degree"] == 3]["h"],
    df_mbr[df_mbr["degree"] == 3]["energy_per_site"]-df_ed["energy_per_site"],
    'P',
    label="MBR - 3",
    **style.create_markers("C4"),
)
ax_inset.plot(
    df_mbr[df_mbr["degree"] == 4]["h"],
    df_mbr[df_mbr["degree"] == 4]["energy_per_site"]-df_ed["energy_per_site"],
    'P',
    label="MBR - 4",
    **style.create_markers("C5"),
)
ax_inset.plot(
    df_mbr[df_mbr["degree"] == 5]["h"],
    df_mbr[df_mbr["degree"] == 5]["energy_per_site"]-df_ed["energy_per_site"],
    'P',
    label="MBR - 5",
    **style.create_markers("C6"),
)


ax_inset.set_xlim(1, 3)
ax_inset.tick_params(axis="x", labelsize=style.fontstyle_legend["fontsize"])
ax_inset.tick_params(axis="y", labelsize=style.fontstyle_legend["fontsize"])

ax_inset.set_xlabel(r"$h$", labelpad=0, **style.fontstyle_legend)
ax_inset.set_ylabel(
    r"$(E_{\mathrm{MBR}}-E_{\mathrm{ED}})/N$", labelpad=0, **style.fontstyle_legend
)

f.tight_layout()
f.savefig("h_energy.pdf",bbox_inches="tight")
