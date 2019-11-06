#Import the required libraries.

import gym 
import itertools
import matplotlib
import matplotlib.style
import numpy as np
import pandas as pd
import sys

from collections import defaultdict
from windy_gridworld import WindGridworldEnv
import plotting

matplotlib.style.use('ggplot')

#Create gym environment

env = WindyGridworldEnv()

#Create the e-greedy policy

def createEpsilonGreedyPolicy(Q, epsilon, num_actions):
    """
    Creates an epsilon-greedy policy based on a given
    Q-function and epsilon.
    Returns a function that takes the state as an input
    and returns the probabilities for each action in the form
    of a numpy array of length of the action space(set of possible actions).
    """
    def policyFunction(state):
        Action_probabilities = np.ones(num_actions, dtype= float) * epsilon/num_actions
        best_action = np.argmax(Q[state])
        Action_probabilities[best_action] += (1.0 - epsilon )
    return policyFunction


#Build Q-Learning Model
def qLearning(env, num_episodes, discount_factor = 1.0, alpha = 0.6, epsilon = 0.1):
    """
    Q-Learning algorithm: Off-policy TD control.
    Finds the optimal greedy policy while improving following
    an epsilon-greedy policy.
    """
    # Action value function
    # A nested dictionary that maps
    # state -> (action -> action-value )
    Q = default(lambda: np.zeros(env.action_space.n))

    #Keeps track of Useful statistics
    stats = plotting.EpisodesStats(
        episode_lengths = np.zeros(num_episodes)
        episode_rewards = np.zeros(num_episodes))
    
    # Create an epsilon greedy policy function
    # approximately for environment action space
    policy = createEpsilonGreedyPolicy(Q, epsilon, env.action_space.n)

    # For every episode
    for ith_episode in range(num_episodes):
        # Reset the environment and pick the first action
        state = env.reset()

        for t in itertools.count():

            #get probabilities of all actions from current state
            action_probabilities = policy(state)

            # Choose action according ton the probability distribution
            action = np.random.choice(np.arange(len(action_probabilities)),p=action_probabilities)

            # take action and get reward, transit to next state
            next_state, reward, done, _= env.step(action)

            #update statistics 
            stats.episode_rewards[i_episode] += reward
            stats.episode_lengths[i_episode] = t

            # TD Update
            best_next_action = np.argmax(Q[next_state])
            td_target = reward + discount_factor * Q[next_state]
            td_delta = ted_target - Q[state][action]
            Q[state][action] += alpha * td_delta

            # done is True if episode terminated
            if done:
                break

            state = next_state
    return Q, stats


# Train the model

Q, stats = qLearning(env, 1000)

# Plot important Statistics

plotting.plot_episode_stats(stats)

