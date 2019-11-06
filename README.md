## Reinforcement learning

Reinforcement learning is briefly a paradigm of Learning process in which a agent learns, overtime, to behave optimally in a certain environment by interacting continuously in the environment. The agent during its course of learning experience varies different situations in the environment it is in. These are called states. The agent while being in that state may choose from a set of allowable actions which may fetch different rewards(or penalties). The learning agent overtime learns to maximmize these rewards so as to behave optimally at any given state it is in.

### Q-Learning

Q-Learning is a basic form of reinforcement learning which uses Q-values ( also called action values ) to iteratively improve the behaviour of the learning agent.

1. <strong>Q-values or Action-values : </strong> Q-values are defined for states and actions. Q(S,A) is an estimation of how good is it to take the action A at the state S. This estimation of Q(S,A) will be iteratively computed using the <strong>TD-Update rule</strong> which we will see in further sections.

2. <strong>Rewards and Episodes : </strong>An agent over the course of its lifetime starts from a start state, makes a number of transitions from its current state to a next state based on its choice of action and also the environment the agent is interacting in. At every step of transition, the agent from a state takes an action, observes a reward from the environment, and then transits to another state. If any point of time the agent ends up in one of the terminating states that means there are no further transition possible. This is said to be the completion of an episode.

3. <strong>Temporal Difference or TD-Update : </strong> The Temporal Difference or TD-Update rule can be represented as follows:
> Q(S,A) <-- Q(S,A) + a( R + yQ(S',A') - Q(S,A))
This update rule to estimate the value of Q is applied at every time step of the agents interaction with the environment. The terms used are explained as:
* <strong>S</strong>: Current state of the agent.
* <strong>A</strong>: Current Action Picked according to some policy.
* <strong>S'</strong>: Next State where the agent ends up.
* <strong>A'</strong>: Next best action to be picked using current Q-value estimation, i.e. pick the action with the maximum Q-value in the next state.
* <strong>R</strong>: Current Reward observed from the environment in Response of current action.
* <strong>y( >0 and <=1 )</strong>: Discounting Factor for Future Rewards. Future rewards are less valuable than current rewards so they must be discounted. Since Q-value is an estimation of expected rewards from a state, discounting rule applies here as well.
* <strong>a</strong>: Step length taken to update the estimation of Q(S,A).

4. <strong>Choosing the Action to take using e-greedy policy.</strong>:
e-greedy policy is a very simple policy of choosing actions using the current Q-Value estimations. It goes on as follows:
* With probability (1-e) choose the action which has the highest Q-value.
* With probability (e) choose any action at random.