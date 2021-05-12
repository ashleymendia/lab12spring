## CS-UY 1114 — Final Lab
# List Comprehensions and the Grand Review™
#### May 7th, 2021

***This lab is entirely optional***. As with the previous optional lab, whether you complete it or not, care about it
or not, or will its existence away or not, you will not gain or lose any points over it.

Still, though, you may ask your TAs questions on it, email me about it, and use it in any way that will help you study
for the final exam. As usual, we are at your behest.

---

### This is it.

First of all, I would like to say that it was a pleasure and privilege being your lab instructor this semester. My 
deepest regret is not being able to have interacted with all of you as much as I would've liked to (though I could, and
probably will, chalk it up to the unfortunate current state of the world.)

I sincerely hope that you enjoyed the problems that I made for you all throughout the semester, and that they helped you
find ways to enjoy computer science even when you didn't think it was possible. And if I didn't succeed there, this
last lab will finally let you settle the score with all the TAs. You'll see what I mean soon.

Good luck studying, and I hope that everybody has a safe and fun summer break!

— Sebastián.

---
### The Story

Professor and Pokémon trainer Reeves wants to be the very best that no one ever was. To that end, he has travelled
across the land and caught and trained a bunch of [**Eevees**](https://en.wikipedia.org/wiki/Eevee), which have now
evolved. His team looks like this at the moment:

- A [**Clairion**](https://inprogresspokemon.tumblr.com/post/629891395121020928/claireon-psychicice-on-rare-occasion)
(Ice/Psychic) named "Sebastián".
- A [**Faereon**](https://inprogresspokemon.tumblr.com/post/184207090351/inspired-loosely-by-will-o-wisps-and-general)
(Fairy/Fire) named "Selina".
- An [**Espeon**](https://bulbapedia.bulbagarden.net/wiki/Espeon_(Pokémon)) (Psychic) named "Kori".
- A [**Soluneon**](https://inprogresspokemon.tumblr.com/post/150083202738/after-our-discussion-about-hybriddual-type)
(Dark/Psychic) named "Ollie".
- A [**Mytheon**](https://inprogresspokemon.tumblr.com/post/186703818424/dd) (Fairy/Dragon) named "Thy".
- A [**Manteon**](https://inprogresspokemon.tumblr.com/post/638230094464368640/manteon-dragonwater-on-rare-occasion)
(Dragon/Water) named "Mohini"

He feels
confident enough to take on the strongest trainers in New York: The Tandon League, whose leader is
[**Gary Oak**](https://bulbapedia.bulbagarden.net/wiki/Gary_Oak). Gary's team looks like this:

- A [**Plasmeon**](https://inprogresspokemon.tumblr.com/post/187446283071/whats-this-i-was-never-that-happy-with)
(Fire/Electric) named "Prachi".
- A [**Spectreon**](https://inprogresspokemon.tumblr.com/post/643847211890933760/this-rainbow-fired-dual-type-eeveelution-was)
(Fire/Flying) named "Smit".
- A [**Blitzeon**](https://inprogresspokemon.tumblr.com/post/185729797507/inspired-by-thunderstorms-and-requested-by-tzigi)
(Electric/Dark) named "John".
- An [**Arcteon**](https://inprogresspokemon.tumblr.com/post/177910518394/on-rare-occasion-an-eevee-can-be-affected)
(Dark/Ice) named "Eliot".
- An [**Acideon**](https://inprogresspokemon.tumblr.com/post/621012955929182208/acideon-firewater-sometimes-an) named
(Fire/Water) "Apoorva".
- A [**Polareon**](https://inprogresspokemon.tumblr.com/post/613402829105840128/this-iceelectric-dual-type-eeveelution-was)
(Ice/Electric) named "Rihui".

(_Note: Yes, we each **did** pick our Pokemon. [**Source**](https://inprogresspokemon.tumblr.com/eeveelutions)_)

Our job is to make that happen
through the power of all of the concepts that you have learned throughout the semester. Good luck.

_**P.S.**: If you've never played/watched Pokémon, or a similar game/show, I'm so sorry._

_**P.P.S.**: Please don't post this online anywhere else. I don't want to get sued by Nintendo :)_

_NOTE_: All of our code will go in the file [**tandon_league.py**](tandon_league.py).

### Problem 1: The **`Pokemon`** Class

Let's start with creating our professor's Pokémon. In our file, create a class called **`Pokemon`**. The **`Pokemon`**
class will have the following methods, which we will tackle one-by-one:

| **Method**                  | **Type of Method** | **Returns**     | **Notes**                                                                                         |
|-----------------------------|--------------------|-----------------|---------------------------------------------------------------------------------------------------|
|                `__init__()` | Dunder / Special   | `None`          | The constructor of the `Pokemon` class.                                                           |
|                 `__str__()` | Dunder / Special   | `str`           | Returns informal string representation of `Pokemon` object.                                       |
| `__gt__()`                  | Dunder / Special   | `bool`          | Returns whether this `Pokemon` object has a greater **speed** stat than another `Pokemon` object. |
| `attack()`                  | Public             | `float` / `int` | Returns the damage that the `Pokemon` object will inflict in a single attack.                     |
| `_will_land_critical_hit()` | Private            | `bool`          | Returns whether a Pokemon will land a critical hit.                                               |

It might look like a lot to do, but a lot of these methods are very short and easy. So take it one step at a time and
don't move on to the next section until you understand everything that's going on in what you've already implemented!

#### 1.1: The **`__init__()`** Method

Write your **`Pokemon`** class's constructor so that it contains the following attributes (note that type 1 and type 2,
along with strength and speed are accepted as separate parameters in the constructor, but are not necessarily a
separate attribute in the class):

| **Attribute**      | **Type**       | **Comments**                                                                                                                                                |
|--------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `pokemon_name`     | _`str`_        | The name of our Pokémon.                                                                                                                                    |
| `nickname`         | _`str`_        | The nickname of our Pokémon, given by Prof. Reeves.                                                                                                         |
| `level`            | _`int`_        | The level of our Pokémon.                                                                                                                                   |
| `types`            | _`(str, str)`_ | The two types of the Pokémon. Will be passed as **two individual parameters** to the constructor.                                                           |
| `hp`               | _`int`_        | The health of our Pokémon.                                                                                                                                  |
| `stats`            | _`{str: int}`_ | The battle statistics of our Pokémon. These key-values include: `"attack"`: an `int`, and `"speed"`: an `int` |

_**Table 1**: **`Pokemon`**'s attributes. Note that these are **not** necessarily the parameters passed into
the constructor._

If all goes smoothly, your **`Pokemon`** class will behave as follows:

```python
def main():
   your_TA = Pokemon("Espeon", "Kori", 100, "Psychic", "", 160, 55, 80)
   print(your_TA.pokemon_name)
   print(your_TA.nickname)
   print(your_TA.level)
   print(your_TA.types)
   print(your_TA.hp)
   print(your_TA.stats)

main()
```
Output
```text
Espeon
Kori
100
('Psychic', None)
160
{'attack': 55, 'speed': 80}
```

A couple of things to note here:

- You may assume that all will be passed as their intended types (i.e. `pokemon_name` will always receive a
string, `attack` will always receive an integer, etc.) but keep in mind that, inside the file, everything is text. You 
have to convert values explicitly to integers, floats, etc..
- Pokemon _may_ not have a second type. Your constructor should check if an empty string is passed in instead of
`type2`. If this is the case, the second element inside our `types` tuple should be the keyword **`None`**:

```python
your_TA = Pokemon("Espeon", "Kori", 100, "Psychic", "CS", 160, 55, 80)
print(your_TA.types)  # will print ('Psychic', 'CS')
```

#### 1.2 The `__str__()` Method

Let's, like last time, get this one out of the way quickly. Define **`Pokemon`**'s `__str__()` method so that it
behaves, ***exactly***, as follows:

```python
def main():
   pokemon_1 = Pokemon("Gothorita", "Saya", 75, "Psychic", "", 160, 55, 80)
   pokemon_2 = Pokemon("Hatterene", "Elaina", 100, "Psychic", "Fairy", 160, 55, 80)
   print(pokemon_1)
   print(pokemon_2)

main()
```
Output:
```text
Gothorita Pokemon object 'Saya' of type(s) Psychic, level 75
Hatterene Pokemon object 'Elaina' of type(s) Psychic/Fairy, level 100
```

#### 1.3 The **`attack()`** and **`__will_land_critical_hit()`** Methods

The next method we'll define for the **`Pokemon`**'s class will be the **`attack()`** method, which itself will make use
of another method we have to define: the **`__will_land_critical_hit()`**. We'll borrow from one of our previous labs
here, so I will just adapt the instructions from there below:

There is always a chance that our Pokemon will land a critical hit when attacking.
This basically means that, based on your Pokemon's stats, your attack **might** roughly double in damage. The "might"
here is actually based on probability:

> Whether a move scores a critical hit is determined by comparing a 1-byte **random number (0 to 255)** against a 1-byte
> threshold value (also 0 to 255); if the random number is less than the threshold, the Pokemon scores a critical hit.

— _[**Critical hit**](https://bulbapedia.bulbagarden.net/wiki/Critical_hit), Bulbapedia_.

Basically, we'll have two values:
- A random value, **`R`** from 0 to 255.
- A threshold value, **`T`** from 0 to 255. If this value is higher than **`R`**, the **`Pokemon`** object
lands a critical hit; we can calculate a critical value as follows:

```text
T = (speed / 2)
```
_**Figure 1**: Threshold formula, where **`speed`** is equal to the **`Pokemon`** object's `"speed"` stat._

If it is determined that the **`Pokemon`** has landed a critical hit, the damage multiplier (that is, the
number by which the **`Pokemon`**'s `"attack"` stat will be multiplied by) will be equal to:

```text
Multiplier = (2L + 5) / (L + 5)
```
_**Figure 2**: Multiplier formula, where **`L`** is equal to the **`Pokemon`** object's `level`._

So, with this knowledge in hand, first write a method in the **`Pokemon`** class called **`_will_land_critical_hit()`**
that will determine whether our **`Pokemon`** object will land a critical hit. Naturally, the `random` module is
necessary here. That's all this method needs to do: return `True` if the **`Pokemon`** object lands a critical hit, and
`False` if it doesn't.

Next, write a second method called `attack()`, which will return the `attack` stat of the **`Pokemon`** object if
**`_will_land_critical_hit()`** returns `False`, or the `attack` stat of the **`Pokemon`** object multiplied by the
critical hit multiplier if it **`_will_land_critical_hit()`** returns `True`.

Check out the following sample behavior, where I added a `print` function message every time a critical hit is landed.
This is not necessary, but feel free to add it to your code if it helps you:

```python
def main():
   starter_pokemon = Pokemon("Aegislash", "Napoleon", 75, "Steel", "Ghost", 160, 55, 80)
  
   number_of_tests = 10
   for test_number in range(number_of_tests):
       attack_power = starter_pokemon.attack()
       print("In move #{}, {} '{}' attacked with {} power.".format(test_number + 1, starter_pokemon.pokemon_name, starter_pokemon.nickname, attack_power))

main()
```
Possible output (I added a `print` statement in my **`attack()`** function for clarity of what's going on):
```text
Napoleon attacks!
Napoleon lands a critical hit!
In move #1, Aegislash 'Napoleon' attacked with 106.5625 power.
Napoleon attacks!
In move #2, Aegislash 'Napoleon' attacked with 55 power.
Napoleon attacks!
In move #3, Aegislash 'Napoleon' attacked with 55 power.
Napoleon attacks!
Napoleon lands a critical hit!
In move #4, Aegislash 'Napoleon' attacked with 106.5625 power.
Napoleon attacks!
In move #5, Aegislash 'Napoleon' attacked with 55 power.
Napoleon attacks!
In move #6, Aegislash 'Napoleon' attacked with 55 power.
Napoleon attacks!
Napoleon lands a critical hit!
In move #7, Aegislash 'Napoleon' attacked with 106.5625 power.
Napoleon attacks!
In move #8, Aegislash 'Napoleon' attacked with 55 power.
Napoleon attacks!
In move #9, Aegislash 'Napoleon' attacked with 55 power.
Napoleon attacks!
In move #10, Aegislash 'Napoleon' attacked with 55 power.
```

Note that `starter_pokemon` lands a critical hit in moves 1, 4, and 7.

#### 1.4 The **`__gt__()`** Method

Finally, we'll define the `Pokemon` class's **`__gt__()`** method. For our `Pokemon` class, this will mean the
following: very simply, return `True` when the `Pokemon` object's ***speed*** stat is greater than the other `Pokemon`
object's speed stat. Otherwise, return `False`:

```python
def main():
   trainer_pokemon = Pokemon("Glaceon", "Miu", 80, "Ice", "", 200, 55, 90)  # speed stat: 90
   rival_pokemon = Pokemon("Sylveon", "Ayaka", 75, "Fairy", "", 160, 55, 80)  # speed stat: 80
   winner = "{}".format(trainer_pokemon.pokemon_name if trainer_pokemon > rival_pokemon else rival_pokemon.pokemon_name)
   print(winner)

main()
```
Output:
```text
Glaceon
```

### Problem 2: The **`ProfessorTrainer`** Class

Oh yeah, it's all coming together. The **`ProfessorTrainer`** class will contain the following methods:

| **Method**        | **Type of Method** | **Returns** | **Notes**                                                                                                                                         |
|-------------------|--------------------|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
|      `__init__()` | Dunder / Special   | `None`      | The constructor of the `ProfessorTrainer` class.                                                                                                  |
|       `__str__()` | Dunder / Special   | `str`       | Returns informal string representation of `ProfessorTrainer` object.                                                                              |
| `_load_pokemon()` | Private            | `None`      | Loads a file passed into the `ProfessorTrainer` constructor and uses its contents to populate the `ProfessorTrainer`'s list of `Pokemon` objects. |

#### 2.1: The **`__init__()`** Method

Each **`ProfessorTrainer`** object will be equipped with the following attributes:

| **Attribute**         | **Type**                | **Comments**                                    |
|-----------------------|-------------------------|-------------------------------------------------|
| `professor_name`      | _`str`_                 | The name of our professor.                      |
| `party`               | _`[Pokemon]`_           | That is, a list of `Pokemon` objects.           |

_**Table 2**: **`ProfessorTrainer`**'s attributes. Note that these are **not** necessarily the parameters passed into
the constructor._

However, each **`ProfessorTrainer`** object will be instantiated, and will behave, as follows:

```python
def main():
   file_path = "save_file_1.csv"
   trainer_name = "Darryl Reeves"
   your_professor = ProfessorTrainer(trainer_name, file_path)

   print("Professor {}, and their Pokemon:".format(your_professor.professor_name))
   for pokemon in your_professor.party:
       print("{}, a {}.".format(pokemon.nickname, pokemon.pokemon_name))

main()
```
Output:
```text
Professor Darryl Reeves, and their Pokemon:
Sebastian, a Clairion.
Selina, a Faereon.
Kori, a Espeon.
Ollie, a Soluneon.
Thy, a Mytheon.
```
That is, each **`ProfessorTrainer`** object will accept one string as its `professor_name`, and a second string denoting
the name of a file where their Pokemon's information can be found. In the above case, file `save_file_1.csv` looks as
follows:

```csv
Pokemon Name,Nickname,Level,Type 1,Type 2,Total,HP,Attack,Speed
Clairion,Sebastian,50,Psychic,Ice,465,150,60,70,
Faereon,Selina,50,Fairy,Fire,525,165,60,65
Espeon,Kori,50,Psychic,,520,160,55,80
Soluneon,Ollie,50,Dark,Psychic,520,160,150,60
Mytheon,Thy,50,Fairy,Dragon,470,165,75,95
```

In other words, you have to read this file inside your constructor and create a list of **`Pokemon`** objects from it.
We could do this inside the `__init__()` method itself, but it would clutter it a bit too much.

Instead, initialize the **`ProfessorTrainer`** object's `party` attribute as an empty list. Then, make a call to a
"private" method called `_load_pokemon()`, which will populate this empty list with the file's contents, and which 
we'll define next...

#### 2.2 The `_load_pokemon()` Method

The **`_load_pokemon()`** will accept the file path string that was passed into the **`ProfessorTrainer`**'s
`__init__()` method, and:

1. Attempt to open this file in read-mode.
2. If the file does not exist at the provided file path, return immediately.
3. If it does find the file, creates a `Pokemon` object per line in the file (ignore the header). Keep in mind that not
every value per line is useful when creating a `Pokemon` object.
4. Append that new `Pokemon` object to the **`ProfessorTrainer`**'s `party` attribute.
5. Close the file, and return immediately.

Again, this method should be called inside the `__init__()` method ***after*** initializing the `party` attribute to an
empty list.

#### 2.3 The `__str__` Method

Write your **`ProfessorTrainer`** class's **`__str__`** method so that it behaves ***exactly*** as follows:

```python
def main():
   their_professor = ProfessorTrainer("Gary Oak", "save_file_2.csv")
   print(their_professor)

main()
```
Output:
```text
ProfessorTrainer object 'Gary Oak' and contains the following Pokemon objects:
Plasmeon, called Prachi ('Fire', 'Electric')
Spectreon, called Smit ('Fire', 'Flying')
Blitzeon, called John ('Dark', 'Electric')
Arcteon, called Eliot ('Dark', 'Ice')
Acideon, called Apoorva ('Fire', 'Water')
Polareon, called Rihui ('Ice', 'Electric')
```

Pretty simple, right? Give yourself a challenge, and try to use a **list comprehension** in at least part of your
implementation! Ask your TAs for guidance if you need it.

And that's it for the **`ProfessorTrainer`** class. Now for the fun.

### Problem 3: Becoming the Tandon League Champion

Let's put our classes to good use. Write a standalone function (that is, not a method of either class) that will accept
two `ProfessorTrainer` objects. This function, called **`ultimate_showdown()`**, will then:

1. Pick a random `Pokemon` object from each `ProfessorTrainer` object's `party` list. You may assume that each
`ProfessorTrainer` object will have at least 1 `Pokemon` object inside their list. ***Be sure to not mutate either
`ProfessorTrainer` object's `party` attribute when doing this.***
2. Have both `Pokemon` attack each other until either reaches an `hp` of 0. The way we determine who attacks first every
turn is as follows: Determine which `Pokemon` object has the highest speed stat. Do this without accessing their `stats`
attribute. (Hint: We defined the `__gt__()` attribute for the `Pokemon` class, which is based on the speed stat) If
Pokemon A's speed stat is greater than Pokemon B's, then Pokemon A attacks first. Similarly, if Pokemon B's speed stat
is greater than Pokemon A's, then Pokemon B attacks first. If they both have the same speed stat, flip a coin (50/50)
to determine who attacks first.
3. The way we attack is by subtracting the attack stat of the attacking Pokémon from the `hp` attribute of the defending
Pokeémon. ***Remember to check the defending Pokemon's `hp` attribute right after it gets attacked. If it fainted (that
is, if it's `hp` attribute reached 0 or below) it can no longer attack. If this happens, go immediately to step 4.***
4. Return the `professor_name` attribute of whichever `ProfessorTrainer` object won.

Be aware that the **`battle`** function should not actually alter the `Pokemon` objects inside the `party` attribute
(hint: the `copy` module is useful here).

Here is some sample behavior to consider. As before, I added some `print` function messages to better illustrate what
is going on:
```python
def main():
   your_professor = ProfessorTrainer("Darryl Reeves", "save_file_1.csv")
   their_professor = ProfessorTrainer("Gary Oak", "save_file_2.csv")

   winner = ultimate_showdown(your_professor, their_professor)
   print("Professor {} wins the ultimate showdown!".format(winner))

main()
```
Possible output:
```text
Professor Darryl Reeves sends out a Soluneon called 'Ollie'!
Professor Gary Oak sends out a Polareon called 'Rihui'!

Rihui attacks!
Ollie attacks!
Rihui attacks!
Ollie attacks!
Ollie lands a critical hit!
Professor Darryl Reeves's Pokemon Ollie wins!
Professor Darryl Reeves wins the ultimate showdown!
```
Another possible output:
```text
Professor Darryl Reeves sends out a Clairion called 'Sebastian'!
Professor Gary Oak sends out a Arcteon called 'Eliot'!

Eliot attacks!
Sebastian attacks!
Eliot attacks!
Eliot lands a critical hit!
Sebastian attacks!
Eliot attacks!
Professor Gary Oak's Pokemon Eliot wins!
Professor Gary Oak wins the ultimate showdown!
```


Where `save_file_2.csv` looks as follows:

```csv
Pokemon Name,Name,Level,Type 1,Type 2,Total,HP,Attack,Speed
Plasmeon,Prachi,50,Fire,Electric,384,175,65,69
Spectreon,Smit,50,Fire,Flying,514,195,117,28
Blitzeon,John,50,Dark,Electric,335,159,66,41
Arcteon,Eliot,50,Dark,Ice,290,140,45,90
Acideon,Apoorva,50,Fire,Water,600,180,135,70
Polareon,Rihui,50,Ice,Electric,400,165,73,85
```

I have included both of these sample files [**here**](save_file_1.csv) and [**here**](save_file_2.csv), in case you
want to use them, but feel free to create your own and have fun with it!

---

Anyway, that's it for me. The solution for this lab can be found [**here**](solution.py), but please try every single
problem out first (you'll also have to change the configuration to the one called `"solution"`)! Feel free to email me
at [**src402@nyu.edu**](src402@nyu.edu) anytime before the final exam if you have any questions about any of the labs. I
hope to see you all at the review session, and good luck!

