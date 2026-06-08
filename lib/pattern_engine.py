"""Ternary strategy → TidalCycles rhythmic pattern engine"""
import json
from typing import List, Dict

TERNARY_TO_TIDAL = {
    1:  's "bd"',       # assertion → kick
    0:  's "hh"',       # sustain  → hat
    -1: 's "sn"',       # opposition → snare
}

def vector_to_pattern(ternary_vector: List[int], name: str = "agent") -> str:
    """Convert a ternary state vector into a TidalCycles pattern string."""
    tidied = []
    for v in ternary_vector:
        tidied.append(TERNARY_TO_TIDAL.get(v, 's "hh"'))
    return f'{name}: {", ".join(tidied)}'

def vector_to_euclidean(ternary_vector: List[int], steps: int = 8) -> str:
    """Convert ternary vector into Euclidean rhythm pattern for Tidal."""
    ons = [i for i, v in enumerate(ternary_vector) if v == 1]
    offs = [i for i, v in enumerate(ternary_vector) if v == -1]
    if not ons:
        return f'e({steps}, {steps})'  # silence
    pulses = len(ons)
    return f'e({pulses}, {steps})'

def vector_to_fast(ternary_vector: List[int]) -> str:
    """Generate TidalCycles fast/slow pattern based on vector density."""
    density = sum(1 for v in ternary_vector if v != 0) / len(ternary_vector) if ternary_vector else 0
    if density > 0.6:
        return 'fast 2'
    elif density > 0.3:
        return 'slow 2'
    return ''

if __name__ == '__main__':
    test_vec = [1, 0, -1, 1, 0, -1, 1, 1]
    print(vector_to_pattern(test_vec, "test-agent"))
    print(f'Euclidean: {vector_to_euclidean(test_vec)}')
    print(f'Density: {vector_to_fast(test_vec)}')
