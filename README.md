# FinancialStochasticProcesses Documentation
## Installation

You can install the package via `pip`:

```bash
pip install financial_stochastic_processes
```
## StochasticAssetPriceSimulator
The **StochasticAssetPriceSimulator** is a Python class designed to simulate various financial stochastic processes, such as The `FinancialStochasticProcesses` class simulates various financial stochastic processes, such as Geometric Brownian Motion (GBM), Jump Diffusion, Heston Stochastic Volatility model, and Regime-Switching models. This class can be used to model and simulate asset price dynamics with optional control over randomness using a seed for reproducibility.

### Features

- **Geometric Brownian Motion (GBM)**: Simulates asset price movements under the GBM assumption.
- **Jump Diffusion Model**: Simulates asset price movements with both continuous price changes and discrete jumps, where jumps can be either upward or downward.
- **Seed Control**: Optionally set a random seed to generate reproducible simulations.



#### 1. Initialize the Simulator

You can initialize the simulator by providing the required parameters, including the initial stock price, time horizon, and time step size.

```python
simulator = StochasticAssetPriceSimulator(S0=100, T=1, dt=0.01, seed=42)
```

#### 2. Simulate Geometric Brownian Motion (GBM)

Use the `simulate_GBM` method to generate asset prices under a GBM process.

```python
gbm_simulation = simulator.simulate_GBM()
```

#### 3. Simulate Jump Diffusion

Use the `simulate_jump_diffusion` method to generate asset prices under a Jump Diffusion process.

```python
jump_diffusion_simulation = simulator.simulate_jump_diffusion()
```

#### Example Code:

```python
import matplotlib.pyplot as plt

# Initialize the simulator
simulator = StochasticAssetPriceSimulator(S0=100, T=1, dt=0.01, seed=42)

# Simulate GBM
gbm_prices = simulator.simulate_GBM()

# Simulate Jump Diffusion
jump_diffusion_prices = simulator.simulate_jump_diffusion()

# Plot the results
plt.plot(gbm_prices, label="GBM")
plt.plot(jump_diffusion_prices, label="Jump Diffusion")
plt.xlabel("Time")
plt.ylabel("Asset Price")
plt.legend()
plt.title("Stochastic Asset Price Simulation")
plt.show()
```

### Parameters

The following parameters are available when creating a `StochasticAssetPriceSimulator` instance:

| Parameter | Description | Default Value |
| --------- | ----------- | ------------- |
| `S0`      | Initial stock price | Required |
| `T`       | Time horizon | Required |
| `dt`      | Time step size | Required |
| `mu`      | Drift (expected return) | `0.05` |
| `sigma`   | Volatility | `0.2` |
| `lamb`    | Jump intensity (average number of jumps) | `0.75` |
| `p`       | Probability of upward jumps | `0.5` |
| `lambda1` | Intensity of upward jumps | `1.0` |
| `lambda2` | Intensity of downward jumps | `1.0` |
| `kappa`   | Mean reversion rate (Heston model) | `0.15` |
| `theta`   | Long-run variance (Heston model) | `0.05` |
| `xi`      | Volatility of variance (Heston model) | `0.2` |
| `regimes` | Parameters for Regime Switching Model | `None` |
| `P`       | Transition matrix for Regime Switching | `None` |
| `seed`    | Seed for reproducibility | `None` |

## Requirements

- Python 3.6 or higher
- `numpy`

Install dependencies with:

```bash
pip install numpy
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.

---

Happy simulating!
