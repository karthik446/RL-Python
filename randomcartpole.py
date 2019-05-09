import gym
if __name__ == '__main__':
    env = gym.make('CartPole-v0')
    total_reward = 0.0
    total_steps = 10
    obs = env.reset()
    while True:
        action = env.action_space.sample()
        obs, reward, done, _ = env.step(action)
        total_reward += reward
        total_steps += 1
        if done:
            break
    print("Episode done in %d steps, total reward obtained by the agent is %.2f" % (
        total_steps, total_reward))
