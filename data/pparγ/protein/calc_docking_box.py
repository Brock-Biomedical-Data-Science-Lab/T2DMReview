from pymol import cmd
import os

# ===============================
# Parameters
# ===============================
TARGET_RESN = "GD4"        # co-crystal ligand residue name
BUFFER = 15.0              # buffer added to each dimension (Å)
EXHAUSTIVENESS = 96        # vina exhaustiveness
CONFIG_NAME = "config.txt"

# ===============================
# 0. Load protein structure
# ===============================
cwd = os.getcwd()

protein_path = os.path.normpath(
    os.path.join(cwd, "pdb_files", "6dgo_raw.pdb")
)

if not os.path.exists(protein_path):
    raise FileNotFoundError(f"[ERROR] Protein not found: {protein_path}")

cmd.load(protein_path, "protein_raw")

# ===============================
# 1. Select GD4 (auto-detect chain)
# ===============================
sel = f"(resn {TARGET_RESN})"
cmd.select("ligand_auto", sel)

if cmd.count_atoms("ligand_auto") == 0:
    raise SystemExit(f"[ERROR] No {TARGET_RESN} found in structure")

# ===============================
# 2. Calculate bounding box
# ===============================
mn, mx = cmd.get_extent("ligand_auto")

center = (
    (mn[0] + mx[0]) / 2.0,
    (mn[1] + mx[1]) / 2.0,
    (mn[2] + mx[2]) / 2.0
)

size = (
    (mx[0] - mn[0]) + BUFFER,
    (mx[1] - mn[1]) + BUFFER,
    (mx[2] - mn[2]) + BUFFER
)

# ===============================
# 3. Write Vina config file
# ===============================
config_path = os.path.join(cwd, CONFIG_NAME)
with open(config_path, "w") as f:
    f.write(f"center_x = {center[0]:.3f}\n")
    f.write(f"center_y = {center[1]:.3f}\n")
    f.write(f"center_z = {center[2]:.3f}\n\n")
    f.write(f"size_x = {size[0]:.1f}\n")
    f.write(f"size_y = {size[1]:.1f}\n")
    f.write(f"size_z = {size[2]:.1f}\n\n")
    f.write(f"exhaustiveness = {EXHAUSTIVENESS}\n")
    f.write(f"# buffer_added_per_dimension = {BUFFER:.1f} Å\n")

# ===============================
# 4. Print essential info only
# ===============================
print(f"center (x y z): {center[0]:.3f} {center[1]:.3f} {center[2]:.3f}")
print(f"buffer added per dimension (Å): {BUFFER:.1f}")
print(f"box size (x y z): {size[0]:.1f} {size[1]:.1f} {size[2]:.1f}")
