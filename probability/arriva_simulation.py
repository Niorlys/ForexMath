import numpy as np
import matplotlib.pyplot as plt

# Parameters
lambda_ = 2.0          # rate of the Poisson process
T = 5.0                # simulate over interval [0, T]
max_events = 100       # safety cap to avoid infinite loop

# Simulate arrival times using exponential interarrival times
inter_arrivals = np.random.exponential(scale=1/lambda_, size=max_events)
arrival_times = np.cumsum(inter_arrivals)

# Keep only arrivals within [0, T]
arrival_times = arrival_times[arrival_times <= T]
n_arrivals = len(arrival_times)

# Build Poisson counting process (step function)
times = np.concatenate(([0], arrival_times, [T]))
counts = np.arange(len(times) - 1)
counts = np.append(counts, counts[-1])  # hold last value until T

# Plot the step function
plt.figure(figsize=(10, 5))
plt.step(times, counts, where='post', label='Poisson Process $N_t$', linewidth=2)
plt.vlines(arrival_times, ymin=0, ymax=counts[-1], colors='gray', linestyles='dotted', alpha=0.4)

# Overlay exponential interarrival times (optional)
for i, t in enumerate(arrival_times):
    plt.text(t, counts[i] + 0.3, f'{inter_arrivals[i]:.2f}', rotation=90, ha='center', va='bottom', fontsize=8)

# Labels and legend
plt.title(f"Sample Path of Poisson Process (λ = {lambda_})")
plt.xlabel("Time")
plt.ylabel("Number of Events $N_t$")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
