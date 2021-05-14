from jericho import *
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
print(initial_observation)
while not done:
    # Take an action in the environment using the step fuction.
    # The resulting text-observation, reward, and game-over indicator is returned.
    action = input()
    observation, reward, done, info = env.step(action)
    print(observation)
    # Total score and move-count are returned in the info dictionary
    print('Total Score', info['score'], 'Moves', info['moves'])
print('Scored', info['score'], 'out of', env.get_max_score())