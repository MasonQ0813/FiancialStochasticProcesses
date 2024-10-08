
import numpy as np

class FinancialStochasticProcesses:
    def __init__(self, S0, T, dt, mu=0.05, sigma=0.2, lamb=0.75, kappa=0.15, theta=0.05, xi=0.2, regimes=None, P=None):
        self.S0 = S0    # Initial stock price
        self.T = T      # Time horizon
        self.dt = dt    # Time step size
        self.mu = mu    # Drift
        self.sigma = sigma  # Volatility (for GBM, Jump Diffusion, Heston)
        self.lamb = lamb    # Jump intensity (Jump Diffusion)
        self.kappa = kappa  # Mean reversion rate (Heston)
        self.theta = theta  # Long-run variance (Heston)
        self.xi = xi        # Volatility of variance (Heston)
        self.regimes = regimes  # Parameters for Regime Switching Model
        self.P = P            # Transition matrix for Regime Switching

    def simulate_GBM(self):
        N = int(self.T / self.dt)
        t = np.linspace(0, self.T, N)
        W = np.random.normal(0, 1, N)
        W = np.cumsum(W) * np.sqrt(self.dt)
        S = self.S0 * np.exp((self.mu - 0.5 * self.sigma ** 2) * t + self.sigma * W)
        return S

    def simulate_jump_diffusion(self):
        N = int(self.T / self.dt)
        t = np.linspace(0, self.T, N)
        W = np.random.normal(0, 1, N)
        W = np.cumsum(W) * np.sqrt(self.dt)
        S = np.zeros(N)
        S[0] = self.S0
        for i in range(1, N):
            S[i] = S[i-1] * np.exp((self.mu - 0.5 * self.sigma ** 2) * self.dt + self.sigma * W[i])
            if np.random.rand() < self.lamb * self.dt:
                S[i] *= np.random.normal(1, 0.1)  # Jump diffusion factor
        return S

    def simulate_heston(self):
        N = int(self.T / self.dt)
        t = np.linspace(0, self.T, N)
        W1 = np.random.normal(0, 1, N)
        W2 = np.random.normal(0, 1, N)
        W1 = np.cumsum(W1) * np.sqrt(self.dt)
        W2 = np.cumsum(W2) * np.sqrt(self.dt)
        S = np.zeros(N)
        v = np.zeros(N)
        S[0] = self.S0
        v[0] = self.theta  # Initial variance
        rho = -0.7  # Correlation between price and variance
        for i in range(1, N):
            v[i] = np.abs(v[i-1] + self.kappa * (self.theta - v[i-1]) * self.dt + self.xi * np.sqrt(v[i-1]) * W2[i])
            S[i] = S[i-1] * np.exp((self.mu - 0.5 * v[i-1]) * self.dt + np.sqrt(v[i-1]) * (rho * W1[i] + np.sqrt(1 - rho**2) * W2[i]))
        return S

    def simulate_regime_switching(self):
        N = int(self.T / self.dt)
        t = np.linspace(0, self.T, N)
        W = np.random.normal(0, 1, N)
        W = np.cumsum(W) * np.sqrt(self.dt)
        S = np.zeros(N)
        S[0] = self.S0
        regime = 0
        for i in range(1, N):
            S[i] = S[i-1] * np.exp((self.regimes[regime][0] - 0.5 * self.regimes[regime][1] ** 2) * self.dt + self.regimes[regime][1] * W[i])
            # Regime switching based on transition probabilities
            if np.random.rand() < self.P[regime, 1-regime] * self.dt:
                regime = 1 - regime
        return S
