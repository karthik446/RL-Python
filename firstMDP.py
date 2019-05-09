import random


class Environment:
    def __init__(self):
        self.steps_left = 10

    # Initial Observtion is 0
    # it will return current observation to the agent
    def get_observation(self):
        return [0.0, 0.0, 0.0]
    # it allows the agent to get the set of actions it can take

    def get_actions(self):
        return [0, 1]

    def is_done(self):
        return self.steps_left == 0

    # this is the method that handles an action
    # returns a reward - for now random.random()
    def action(self, action):
        if self.is_done():
            raise Exception("Yo game is over")
        self.steps_left -= 1
        return random.random()


class Agent:
    def __init__(self):
        self.total_reward = 0

    # the step of an agent
    # 1. looks at the current observation from the environment
    # 2. select the actions
    # 3. gets the reward
    def step(self, env):
        # current_observation = env.get_observation()
        actions = env.get_actions()
        reward = env.action(random.choice(actions))
        self.total_reward += reward


if __name__ == "__main__":
    env = Environment()
    agent = Agent()
    while not env.is_done():
        agent.step(env)
    print('Hello there ')
    print("Total reward got: %.4f" % agent.total_reward)
