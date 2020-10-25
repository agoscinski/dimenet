import ase.io
import numpy as np

figshare_qm9 = ase.io.read('/home/alexgo/lib/feature-space-measures/data/qm9.db', ':')
structures_id = np.arange(len(figshare_qm9), dtype=np.dtype('int64'))
number_of_atoms_in_structures = np.array([structure.get_global_number_of_atoms() for structure in figshare_qm9], dtype=np.dtype('int64'))
structures_species = np.concatenate([structure.numbers for structure in figshare_qm9])
structures_positions = np.concatenate([structure.positions for structure in figshare_qm9])
dimenet = np.savez('data/qm9_eV.npz', id=structures_id, N=number_of_atoms_in_structures, Z=structures_species, R=structures_positions)
