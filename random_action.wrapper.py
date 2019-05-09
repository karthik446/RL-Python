import gym
import random

# Say we want to intercept the actions by epsilon % i.e. 10 %
# Similar to C# extensions while creating a class we pass in ActionWrapper method


class RandomActionWrapper(gym.ActionWrapper):
    def __init__(self, env, epsilon=0.1):
        super(RandomActionWrapper, self).__init__(env)
        self.epsilon = epsilon

    def action(self, action):
        if random.random() < self.epsilon:
            print('Executing Random Action')
            return self.env.action_space.sample()
        return action


if __name__ == "__main__":
    env = RandomActionWrapper(gym.make("CartPole-v0"))
    env = gym.wrappers.Monitor(env, "recording", force=True)
    obs = env.reset()
    total_reward = 0.0
    while True:
        obs, reward, done, _ = env.step(0)
        total_reward += reward
        if done:
            break
    print('Reward obtained: %.2f' % total_reward)
