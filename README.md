# Custom Bullet Hell Rhythm Game

# AKA, Rizumu Hebi \- Corruption of the Hollow Moon

This is a long term project based off of the Attack of the Vampire Pizzas project, altered to the forme of a rhythm game, borrowing from Lynn / r3dhummingbird, [GitHub](https://github.com/RuolinZheng08/renpy-rhythm) \<[https\://github.com/RuolinZheng08/renpy-rhythm](https://github.com/RuolinZheng08/renpy-rhythm)\> , [itch.io](https://r3dhummingbird.itch.io/renpy-rhythm-game) \<[https\://r3dhummingbird.itch.io/renpy-rhythm-game](https://r3dhummingbird.itch.io/renpy-rhythm-game)\>’s Renpy rhythm game, to create a fully modular Rhythm game based off, in concept, Zun’s Touhou 19, using the PyGame Library

## How to Play

The Moon has been corrupted and as such all the monsters of Halloween have turned Evil, Freshly carved Jack’o’Lantern Jack has been carved and is the last bastion of hope to save humanity. 
|  | KEYS |  |  |  | EFFECTS |  |  |  | KEYS |  |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Q | W | E |  | Basic Attack | Move Up | Bomb |  | Z | ↑ | X |
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

## Music Credits

* "Doctor Boctor Bone Doctor" by Ategon, used under CC BY 4.0 - <https://opengameart.org/content/doctor-boctor-bone-doctor>
* "Red Moon Red" by Enzo Alexander
* "WTF! Ghost!" by Alexandr Zhelanov <https://soundcloud.com/alexandr-zhelanov>, used under CC BY 3.0 - <https://opengameart.org/content/wtf-ghost>
* "Swing Along" by bramd, used under CC BY 4.0 - <https://opengameart.org/content/swing-along>
* "Chagrin" by Spring Spring, used under OGA BY 4.0 and CC 0 - <https://opengameart.org/content/chagrin>
* "Spider's Web" by Trevor Lentz, used under CC BY 3.0 - <https://opengameart.org/content/spiders-web>
* "Catchy Sci-Fi Background Track - Snail Walk" by Tavalus, used under CC BY 3.0 - <https://opengameart.org/content/catchy-sci-fi-background-track-snail-walk>
* "Bravery Vampire" by MintoDog, used under CC 0 - <https://opengameart.org/content/bravery-vampire>
* "Jackolantern" by bobjt, used under CC 0 - <https://opengameart.org/content/jackolantern>
* ""Crow Man's Stage"" by Threxx and Spring Spring, used under CC 0 - <https://opengameart.org/content/crow-mans-stage>
* "the final encounter..." by VinylScratch, used under OGA BY 4.0 - <https://opengameart.org/content/the-final-encounter>
* "Eat' sa Pizza" by howeverice, used under CC BY SA 4.0 - <https://opengameart.org/content/eat-sa-pizza>
* "carol of bells - sinister" by bobjt, used under CC BY 4.0 and CC 0 - <https://opengameart.org/content/carol-of-bells-sinister>