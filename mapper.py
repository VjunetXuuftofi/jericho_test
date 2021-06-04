from collections import defaultdict
states = defaultdict(list)
from jericho import *
import queue

env = FrotzEnv("z-machine-games-master/jericho-game-suite/905.z5")

env.reset()

states_to_explore = queue.Queue()

state_mapping = {env.get_world_state_hash(): env.get_state()}

states_to_explore.put((0, env.get_world_state_hash()))


while True:
    try:
        depth, state_hash = states_to_explore.get()
    except IndexError:
        break
    if state_hash not in states:
        state = state_mapping[state_hash]
        env.set_state(state)
        for action in env.get_valid_actions():
            observation, reward, done, info = env.step(action)
            next_state_hash = env.get_world_state_hash()
            next_state = env.get_state()
            state_mapping[next_state_hash] = next_state
            states[state_hash].append((action, next_state_hash))
            if done:
                print(f"depth: {depth}, reward: {reward}")
            elif next_state_hash not in states:
                states_to_explore.put((depth + 1, next_state_hash))
            env.set_state(state)
    print(len(states))
