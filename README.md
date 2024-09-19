# FinancialStochasticProcesses Class Documentation

The `FinancialStochasticProcesses` class simulates various financial stochastic processes, such as Geometric Brownian Motion (GBM), Jump Diffusion, Heston Stochastic Volatility model, and Regime-Switching models.

## Constructor

### `__init__(self, S0, T, dt, mu=0.05, sigma=0.2, lamb=0.75, kappa=0.15, theta=0.05, xi=0.2, regimes=None, P=None)`

#### Parameters:
- `S0` *(float)*: The initial stock price.
- `T` *(float)*: The time horizon for the simulation.
- `dt` *(float)*: The time step size for the simulation.
- `mu` *(float, optional)*: The drift rate for GBM, Jump Diffusion, and Heston models. Default is `0.05`.
- `sigma` *(float, optional)*: The volatility for GBM, Jump Diffusion, and Heston models. Default is `0.2`.
- `lamb` *(float, optional)*: The jump intensity for the Jump Diffusion model. Default is `0.75`.
- `kappa` *(float, optional)*: The mean reversion rate for the Heston model. Default is `0.15`.
- `theta` *(float, optional)*: The long-run variance for the Heston model. Default is `0.05`.
- `xi` *(float, optional)*: The volatility of variance for the Heston model. Default is `0.2`.
- `regimes` *(list of tuples, optional)*: A list of tuples, where each tuple represents a different regime with its own drift and volatility. Used in the Regime-Switching model. Default is `None`.
- `P` *(2D numpy array, optional)*: The transition probability matrix for the Regime-Switching model. Default is `None`.

#### Example:
```python
process = FinancialStochasticProcesses(S0=100, T=1, dt=0.01, mu=0.05, sigma=0.2, lamb=0.75)

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
### Adjust Model Parameters

```python
process=FinancialStochasticProcesses(S0, T, dt, mu=0.05, sigma=0.2, lamb=0.75, kappa=0.15, theta=0.05, xi=0.2, regimes=None, P=None)

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
