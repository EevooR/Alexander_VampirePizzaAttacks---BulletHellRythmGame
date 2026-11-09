# Custom Bullet Hell Rhythm Game

# AKA, Rizumu Hebi \- Corruption of the Hollow Moon

This is a long term project based off of the Attack of the Vampire Pizzas project, altered to the forme of a rhythm game, borrowing from Lynn / r3dhummingbird, [GitHub](https://github.com/RuolinZheng08/renpy-rhythm) \<[https\://github.com/RuolinZheng08/renpy-rhythm](https://github.com/RuolinZheng08/renpy-rhythm)\> , [itch.io](https://r3dhummingbird.itch.io/renpy-rhythm-game) \<[https\://r3dhummingbird.itch.io/renpy-rhythm-game](https://r3dhummingbird.itch.io/renpy-rhythm-game)\>’s Renpy rhythm game, to create a fully modular Rhythm game based off, in concept, Zun’s Touhou 19, using the PyGame Library

## How to Play

The Moon has been corrupted and as such all the monsters of Halloween have turned Evil, Freshly carved Jack’o’Lantern Jack has been carved and is the last bastion of hope to save humanity. 

| Q | W | E |  | Basic Attack | Move Up | Bomb |  | Z | ↑ | X |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| A | S | D |  | Move Left | Move Down | Move Right |  | ←  | ↓  | → |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | Left Shift | Sneak | Right Shift |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  | Heal Spell | Slow Spell | Block Spell |  | I | O | P |
|  |  |  |  | Draw Spell | Safe Spell | Random Spell |  | J | K | L |
|  |  |  |  |  |  |  |  |  |  |  |
| esc |  |  |  | Close Game |  |  |  |  |  |  |

## Spell Cards

When an enemy or bullet touches a spell Card, it’s effects will trigger, In ver1, all spell cards depend on RNG to reload and their time lengths. In ver2 Innocents grant “Power” which acts as a sort of a currency, and the card effects last for set amounts of time.

Candy Corn : Saps the life from all enemies and corruptive stars on the field, granting the player a small life boost.

Spider Web: Halves all enemies and corruptive stars on the field’s speed.

Fallen Leaf: Clogs up the paths for Enemies or Corruptive stars temporarily.

Corn: Draws all enemies and Corruptive stars in, 

Christmas Tree: Kills random enemies and Corruptive stars

Lantern: Grants temporary immunity to Jack, letting him take hits without losing a life

Bullet: Does light damage  
Bomb: defeats all enemies on field, has limited uses

## Enemies

Corruptive Star : Odd abnormalities casted by the moon, Seem to have this corruptive effect on halloween monsters, they cannot be harmed by bullets

Vampire: Perfectly mediocre.

Zombie Snail (ver2): Slow and Tanky

Wolf Spider (ver2): Quick and Weak

Crow (ver2): Random Speed, Random Health

Ghost (ver2): Consumes other enemies, adding their health to its own and going over to Jack’s X coordinate.

## 

## 

## File Guides

gameassets/\_\_Skin \- These folders hold the game skins and the assets used.  
gameassets/music \- This holds the mp3s and the beatmaps, using other formats is not recommended, try to stick with MP3 and TXT  
BGTemplate \- you can use this to make your own background  
src/ \- actual game files  
src/config \- this is where you add songs or change the game skin  
src/ver\_ \- version 1.0.0 and 2.0.0 Respectively  
Utils/ \- These are from the Renpy Rhythm game and have their own Read Me, allow you to make beatmaps  
Convertwavtobmp \- (for windows only) auto runs the conversion tool, allowing quick transformation of wav files to beatmaps  
customRythmBulletHell \- (for windows only) auto runs 2.0.0

## Dependencies

Requires an up to date version of Python and Pygame

