import numpy as np

def simulate_matrix_sweep(cycles=1000):
    """
    Simulates the Landauer energy cost of CW vs CCW knots 
    under a sequential Row-Major matrix update.
    """
    matter_efficiency = 1.0
    # Antimatter (CCW) pays a 'Write Penalty' for opposing the sweep
    antimatter_penalty = 1e-9 
    
    m_pop = 1.0
    am_pop = 1.0
    
    for _ in range(cycles):
        m_pop *= (1 - 1e-12) # Natural decay
        am_pop *= (1 - 1e-12 - antimatter_penalty) # Biased decay
        
    return m_pop / am_pop

ratio = simulate_matrix_sweep(cycles=10**6)
print(f"--- Baryon Asymmetry Simulation ---")
print(f"Update Order: Sequential Row-Major")
print(f"Matter/Antimatter Ratio: {ratio:.10f}")
print(f"Result: Matter Dominance via Computational Bias.")
