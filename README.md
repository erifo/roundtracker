# Roundtracker
A python application for counting down the varying durations of effects in turn-based games.

## Usage
Enter an integer for duration and decide if the number represents rounds (6 seconds), minutes, or hours. Give the effect a name and press the button labeled "Add". Repeat until all effects you desire to track are listed. Similarly set how much time a single tick will represent, and also decide whether to tick up or down. Press the button labeled "tick" to adjust all listed effects. Each effect is listed together with its duration split into hours, minutes, and rounds remaining. The list of effects can be sorted in three different ways using the "Sort By..." dropdown menu. Changing the sorting method, adding or removing an effect, or modifying the duration of the effects triggers a save into "roundtracker_save.txt" in the same directory. The application will load this file on launch if able, in order to maintain your list of effects constant between uses.


## Built with
Python 3.6 64bit
DearPyGui 0.6.312