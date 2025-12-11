import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
def run_dynamic_alpha_sim(max_n=100):
    # Problem Size (N): Increases from 10 to 100
    problem_sizes = list(range(10, max_n + 1, 5))
    classic_costs = []      # 1. Classic (Exponential Explosion)
    static_roa_costs = []   # 2. Static ROA (Fixed alpha=0.5)
    dynamic_roa_costs = []  # 3. Dynamic AI (Adaptive alpha)
    dynamic_alphas = []     # Record of alpha adaptation
    print("--- [Alpha-Sim 3.0] Dynamic Roughness Adaptation Started ---")
    for n in problem_sizes:
        # [1] Classic (alpha=1): Exponential Time O(10^(N/5))
        classic = 10 ** (n / 5.0)
        classic_costs.append(classic)
        # [2] Static ROA (alpha=0.5): Polynomial Time O(N^2)
        static_k = 1 / (1 - 0.5) # k=2
        static_roa = n ** static_k
        static_roa_costs.append(static_roa)
        # [3] Dynamic ROA (Adaptive alpha): Intelligent Tunneling
        # Algorithm: As N increases, lower alpha to create shortcuts
        # alpha = 0.6 / log(N)
        curr_alpha = max(0.15, 0.6 / np.log10(n))
        dynamic_alphas.append(curr_alpha)
        # Dynamic Complexity: k = 1/(1-alpha)
        dynamic_k = 1 / (1 - curr_alpha) 
        dynamic_roa = n ** dynamic_k
        dynamic_roa_costs.append(dynamic_roa)
    return problem_sizes, classic_costs, static_roa_costs, dynamic_roa_costs, dynamic_alphas
# --- Execution ---
N, y_classic, y_static, y_dynamic, alphas = run_dynamic_alpha_sim(max_n=100)
# --- Visualization ---
plt.figure(figsize=(12, 8))
plt.plot(N, y_classic, 'r-o', label='Classic (α=1.0) [Exponential Wall]', linewidth=2, alpha=0.4)
plt.plot(N, y_static, 'b--', label='Static ROA (Fixed α=0.5) [Quadratic]', linewidth=2)
plt.plot(N, y_dynamic, 'g-s', label='Dynamic AI (Adaptive α) [Evolutionary]', linewidth=4)
plt.title('[Alpha-Sim 3.0] The Evolution of Intelligence', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Problem Difficulty', fontsize=14)
plt.ylabel('Computing Cost (Log Scale)', fontsize=14)
plt.yscale('log')
plt.grid(True, which="both", ls="--", alpha=0.3)
plt.legend(fontsize=12, loc='upper left')
plt.show()
