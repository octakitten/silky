# Silky
A framework for cognitive neural networks with persistent memory

**What is this?**

This is a hobby project aimed at creating a neural network (of sorts) which can learn and act in real time. I don't really have the methodology documented well, yet, but I'm working on it. Currently, the model sees a pixel greyscale image of arbitrary size and reacts to it with predefined actions. These actions allow it to play a series of games which have win and loss conditions. The model can be initialized with randomized parameters, or these parameters can be iterated on each time the model wins a game.

Currently there are only a handful of simplistic games and the most powerful model runs ridiculously slowly on a home pc. Things on the roadmap are: creating a minesweeper-like game, integrating tensorplus into the project, and creating a more optimized model.

If you'd like to playtest this weird little project, I'm including some wheel releases of the library which can be downloaded from the Releases page and installed locally to your virtual python environment with pip. Fair warning, the project doesn't solve any meaningful problems yet. Thus far I've found that the latest model can "win" the Forest game in anywhere from a few hundred to a few thousand iterations. If you have a GPU with Cuda version 12 or higher (nvidia 10-series or later), then you'll be able to use it to test the model on your home pc in a reasonable amount of time. Just write a small python file that imports the package and runs the "run_hamster()" function from the iteration module and off it will go!

# Building from Source

If you'd like to build from source for some reason, maybe to understand how the project works or to contribute, you can do so locally with Hatch. Note that most of the installation and usage scripts will only work on Linux. Windows users can install the project in WSL (Windows Subsystem for Linux) and run those scripts there.

**1)** Clone the repository locally with Git.

**2)** Install Hatch with Pipx or otherwise: https://hatch.pypa.io/1.13/install/

**3)** Enter the upper level directory for the repo from your terminal and run the "install.sh" script.

**4)** You can then test local changes with a few options:
 - Run the "rerun.sh" script to rebuild the project locally and then run the "run_hamster()" function in the Iteration module. A model will be created and then iterated on as it plays a simple game where it navigates a player icon through a simple "forest" of obstacles. If it bumps into an obstacle, it loses, and if it reaches the goal, it wins.
 - Run the "test.sh" script to rebuild the project, again just locally, and then run run pytest to test the project's basic integrity. As of the writing of these edits, 7/29/2025, test coverage is incomplete.
 - Run the "train.sh" script to test the project on the Tiny ImageNet dataset. The model will train on categorizing various images in plain english until it achieves a certain level of accuracy.

On the roadmap currently is setting up the project to test models on a simple version of the classic Aliens arcade game. I'd like to have it play other games like tetris in the future, as well as further testing on it's viability as a language model by testing it on more image classification tasks.
