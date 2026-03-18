import numpy as np

# --- 2026 SUBSTRATE CONSTANTS (ITERATED) ---
ALPHA = 1 / 137.035999139
KAPPA = 100.5940211247  # Topological Coupling
GAMMA = 0.00024571403   # Lattice Fineness constant

def calculate_iterated_anomaly(nodes, crossings):
    # Order 1: Schwinger Term
    order_1 = ALPHA / (2 * np.pi)
    
    # Order 2: Topological Correction with Fineness Bias
    topo_term = KAPPA * (crossings / nodes)**2 * (ALPHA / np.pi)**2
    fineness_bias = GAMMA / nodes
    
    return order_1 + topo_term - fineness_bias

# --- THE REVEAL ---
print(f"Muon Accuracy (34, 5): {calculate_iterated_anomaly(34, 5):.11f}")
print(f"Electron Accuracy (24, 3): {calculate_iterated_anomaly(24, 3):.11f}")
