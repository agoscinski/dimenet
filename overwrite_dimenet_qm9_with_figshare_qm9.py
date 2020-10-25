import ase.io
import numpy as np
from schnetpack.datasets import QM9

qm9data = QM9('/home/alexgo/lib/feature-space-measures/data/qm9.db', download=True, remove_uncharacterized=True)
properties_key = ["rotational_constant_A", "rotational_constant_B", "rotational_constant_C", "dipole_moment", "isotropic_polarizability", "homo", "lumo", "gap", "electronic_spatial_extent", "zpve", "energy_U0", "energy_U", "enthalpy_H", "free_energy", "heat_capacity"]
properties = {key: np.zeros(len(qm9data)) for key in properties_key}
for i in range(len(qm9data)):
    _, struc_property = qm9data.get_properties(idx=i)
    for key in properties_key:
        properties[key][i] = float(struc_property[key][0])

for key in properties_key:
    np.save("qm9_"+key+".npy", properties[key])

dimenet_qm9 = np.load('data/qm9_eV.npz', allow_pickle=True)

figshare_qm9 = ase.io.read('/home/alexgo/lib/feature-space-measures/data/qm9.db', ':')
structures_id = np.arange(len(figshare_qm9), dtype=np.dtype('int64'))
number_of_atoms_in_structures = np.array([structure.get_global_number_of_atoms() for structure in figshare_qm9], dtype=np.dtype('int64'))
structures_species = np.concatenate([structure.numbers for structure in figshare_qm9])
structures_positions = np.concatenate([structure.positions for structure in figshare_qm9])
meta = dimenet_qm9['meta']
dimenet = np.savez('data/qm9_eV.npz', 
        id=structures_id,
        N=number_of_atoms_in_structures,
        Z=structures_species,
        R=structures_positions,
        A = properties["rotational_constant_A"],
        B = properties["rotational_constant_B"],
        C = properties["rotational_constant_C"],
        mu = properties["dipole_moment"],
        alpha = properties["isotropic_polarizability"],
        homo = properties["homo"],
        lumo = properties["lumo"],
        gap = properties["gap"],
        r2 = properties["electronic_spatial_extent"],
        zpve = properties["zpve"],
        U0 = properties["energy_U0"],
        U = properties["energy_U"],
        H = properties["enthalpy_H"],
        G = properties["free_energy"],
        Cv = properties["heat_capacity"],
        meta=meta)
