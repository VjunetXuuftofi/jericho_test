from jericho import FrotzEnv
import os
# Create the environment, optionally specifying a random seed
game_selected = False
env = None
while not game_selected:
    game = input("What game do you want to play (zork1)? ")
    if game == "":
        game = "zork1"
    try:
        env = FrotzEnv(os.path.join("z-machine-games-master/jericho-game-suite",f"{game}.z5"))
        game_selected = True
    except FileNotFoundError:
        print("Game not recognized!")
initial_observation, info = env.reset()
done = False
print("Number of objects: ", len(env.get_world_objects()))
print(initial_observation)

states = []
observation = ""
while not done:
    action = input()
    if action == "undo":
        state, observation = states.pop()
        print(observation)
        env.set_state(state)
    elif action == "valid":
        print("Valid actions: ", env.get_valid_actions())
    else:
        states.append((env.get_state(), observation))
        observation, reward, done, info = env.step(action)
        print(observation)
        print('Total Score', info['score'], 'Moves', info['moves'])
    if done:
        undo = input("Game over. Type undo to undo, or anything else to end: ")
        if undo == "undo":
            done = False
            state, observation = states.pop()
            print(observation)
            env.set_state(state)
print('Scored', info['score'], 'out of', env.get_max_score())