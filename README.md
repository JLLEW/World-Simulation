# simple world simulation with GUI

### It was my first ever project in python.
Every color represents different organism. There are different plants, animals and there is
one human that you control using arrows (direction of most animal's movement is random). Plants don't move. Organisms take action by priority. Basic rules:
- when there is a collision of diffent kind animals, stronger kills weaker one,
- when there is a collision of animals that are the same kind, they reproduce,
- plants are trying to spread every tour (of course different plants have different propability of spread),
- human has special skill you may activate every 5 tours. His power will increase by 5 points and it will drop by one point next 5 tours,
- you may change game board size,
- you may save and load the simulation. Changes will be saved in save.txt

Unfortunately code is written in Polish language but it was required by my professor.
Every action is described in console.
To run the program just run GUI.py

# Legend:

#### Buttons
"nowa tura" - evokes new tour
"specjalna umiejetnosc" - activates human's special skill
"zapisz" - save
"wczytaj" - load
"stworz swiat" - creates new world

#### Human
color: aqua
power: 5
priority: 4
use arrows to move,

## Animals:

#### Wolf
color: gray
power: 9
priority: 5
no special skills

#### Antelope
color:chocolate
power: 4
priority: 4
jumps every 2 fields, may escape the attack with 50% probability

#### Sheep
color: snow
power: 4
priority: 4
no special skills

#### Cyber sheep
color: aliceblue
power: 11
priority: 4
it's life goal is to eliminate all hogweeds growing on the field. When that specific plant is growing on the field it moves towards the closest hogweed in order to eliminate it.
When there is no hogweeds at all it behaves as usual sheep.

#### Turtle
color: olive
power: 2
priority: 1
there is only 25% chance for this animal to move from its position

#### Fox
color: red
power: 3
priority: 7
Fox is smart. It will never go to the position where stronger organism is.

## Plants

#### Grass
color: green
power: 0
priority: 0
spread index: 15%

#### Dandelion
color: yellow
power: 0
priority: 0
spread index: 25%
It tries 3 times to spread.

#### Wolf's blueberries
color: yellow
power: 99
priority: 0
spread index: 5%
Every organism dies after consumption.

#### Guarana
color: orange
power: 0
priority: 0
spread index: 10%
It increases animal's power by 3 after consumption.

#### hogweed
color: black
power: 10
priority: 0
spread index: 10%
it kills every organism standing on the field next to it except cyber sheep.


