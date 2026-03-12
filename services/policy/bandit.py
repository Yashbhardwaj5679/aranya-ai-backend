import random
import numpy as np


class ContextualBandit:
    """
    Simple epsilon-greedy contextual bandit.
    Actions represent cultivation strategies.
    Context can be plant/environment features.
    """

    def __init__(self, actions, epsilon=0.1):

        self.actions = actions
        self.epsilon = epsilon

        # action statistics
        self.counts = {a: 0 for a in actions}
        self.values = {a: 0.0 for a in actions}

    def select_action(self, context=None):
        """
        Choose action using epsilon-greedy policy.
        Context is unused for now but added for future extension.
        """

        # exploration
        if random.random() < self.epsilon:
            action = random.choice(self.actions)

        # exploitation
        else:
            action = max(self.values, key=self.values.get)

        return action

    def update(self, action, reward):
        """
        Update action value using incremental mean.
        """

        self.counts[action] += 1

        n = self.counts[action]
        value = self.values[action]

        new_value = ((n - 1) / n) * value + (1 / n) * reward

        self.values[action] = new_value

    def get_policy(self):
        """
        Return learned policy values.
        """
        return self.values


# ------------------------------
# Test the bandit
# ------------------------------

if __name__ == "__main__":

    actions = [
        "organic_fertilizer",
        "drip_irrigation",
        "shade_cultivation",
        "direct_soil"
    ]

    bandit = ContextualBandit(actions)

    print("\nRunning bandit simulation...\n")

    for i in range(20):

        context = {
            "plant": "tulsi",
            "soil": "loamy",
            "temperature": 32
        }

        action = bandit.select_action(context)

        # simulate reward
        reward = random.choice([0, 1])

        bandit.update(action, reward)

        print(f"Step {i+1}")
        print("Action:", action)
        print("Reward:", reward)
        print()

    print("Learned Policy:")
    print(bandit.get_policy())