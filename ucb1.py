import numpy as np
import matplotlib.pyplot as plt
from greedyEpsilon import run_experiment as run_experiment_eps


class Bandit:
    def __init__(self, m, upper_limit):
        self.m = m
        self.mean = 0
        self.N = 0

    def pullArm(self):
        return np.random.randn() + self.m

    def updateMean(self, x):
        self.N += 1
        self.mean = (1 - 1.0/self.N)*self.mean + 1/self.N * x


def ucb(mean, n, nj):
    if nj == 0:
        return float('inf')
    return mean + np.sqrt(2 * np.log(n) / nj)


def run_experiment(m1, m2, m3, N, upper_limit=10):
    bandits = [Bandit(m1, upper_limit), Bandit(
        m2, upper_limit), Bandit(m3, upper_limit)]

    data = np.empty(N)

    for i in range(N):
        j = np.argmax([ucb(b.mean, i+1, b.N) for b in bandits])
        x = bandits[j].pullArm()
        bandits[j].updateMean(x)
        data[i] = x
    avg = np.cumsum(data) / (np.arange(N) + 1)

    print('Bandit 1 number of times played', bandits[0].N)
    print('Bandit 1 mean', bandits[0].mean)
    print('Bandit2 number of times played', bandits[1].N)
    print('Bandit 2 mean', bandits[1].mean)

    print('Bandit3 number of times played', bandits[2].N)
    print('Bandit 3 mean', bandits[2].mean)

    plt.plot(avg)
    # plt.plot(np.ones(N) * m1)
    # plt.plot(np.ones(N) * m2)
    # plt.plot(np.ones(N) * m3)
    plt.xscale('log')
    plt.show()

    for b in bandits:
        print(b.mean)
    return avg


if __name__ == '__main__':
    eps = run_experiment_eps(1.0, 2.0, 3.0, 0.1, 100000)
    ucb = run_experiment(1.0, 2.0, 3.0, 100000)

    # log scale plot
    plt.plot(eps, label='eps = 0.1')
    plt.plot(ucb, label='ucb1')
    plt.legend()
    plt.xscale('log')
    plt.show()

    # linear plot
    plt.plot(eps, label='eps = 0.1')
    plt.plot(ucb, label='ucb1')
    plt.legend()
    plt.show()
