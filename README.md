
# Financial Stochastic Processes

A Python package for simulating various financial stochastic processes such as Geometric Brownian Motion (GBM), Jump Diffusion, Heston Stochastic Volatility model, and Regime-Switching models.

## Features

- **Geometric Brownian Motion (GBM)**: Simulate asset prices using the classic GBM model.
- **Jump Diffusion**: Incorporate jumps into the asset price paths, simulating sudden price changes.
- **Heston Model**: Simulate asset prices with stochastic volatility, capturing more realistic financial dynamics.
- **Regime-Switching Model**: Simulate asset prices under different market regimes with transition probabilities between regimes.

## Installation

You can install the package via `pip`:

```bash
pip install financial_stochastic_processes
```

## Usage

### Import the Package

```python
from financial_stochastic_processes import FinancialStochasticProcesses
```

### Simulate Geometric Brownian Motion (GBM)

```python
S0 = 100  # Initial stock price
T = 1     # Time horizon (1 year)
dt = 0.01 # Time step size

# Create an instance of the class
process = FinancialStochasticProcesses(S0, T, dt)

# Simulate GBM
gbm_path = process.simulate_GBM()
```

### Simulate Jump Diffusion

```python
jump_diffusion_path = process.simulate_jump_diffusion()
```

### Simulate Heston Stochastic Volatility Model

```python
heston_path = process.simulate_heston()
```

### Simulate Regime-Switching Model

```python
regimes = [(0.02, 0.1), (0.05, 0.2)]  # Two regimes with different drifts and volatilities
P = np.array([[0.95, 0.05], [0.1, 0.9]])  # Transition matrix

process = FinancialStochasticProcesses(S0, T, dt, regimes=regimes, P=P)
regime_switching_path = process.simulate_regime_switching()
```

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
