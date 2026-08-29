# T2DMReview
This repository contains the processed files and selected analysis scripts for the paper:

“Cheminformatics of Diabetic Protein Targets and Therapeutics.” (Zhao et al.)

## Directory Structure
```text
data/
├── Boltz-2 inputs/
│   └── ...                    # Input files used for Boltz-2 predictions
│
├── abcc8/
│   └── <drug>/
│       ├── <drug>.smi         # SMILES input for the ligand
│       ├── <drug>.pdb         # Prepared 3D ligand structure
│       ├── <drug>.pdbqt       # Ligand input for AutoDock Vina docking
│       ├── <drug>_out.pdbqt   # AutoDock Vina docking output
│       ├── complex/            # Protein–ligand complexes generated from individual Vina docking poses
│       └── closest/            # PLIP results for the representative pose selected in the manuscript
│
├── dpp4/
│   └── <drug>/
│       └── ...
│
├── pparγ/
│   └── <drug>/
│       └── ...
│
└── sglt2/
    └── <drug>/
        └── ...
```
## Citing This Work
```bibtex
@Article{Zhao2026,
author={Zhao, Jiani and Yan, Hongbin and Li, Yifeng},
title={Cheminformatics of Diabetic Protein Targets and Therapeutics.},
journal={},
year={2026},
month={},
day={},
volume={},
number={},
pages={},
doi={},
url={}
}
```
