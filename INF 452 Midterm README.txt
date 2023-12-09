Author: Jason Ngo
Class: INF 0452H; Information Design Studio V: Coding
Institution: University of Toronto
Instructor: Maher Elshakankiri
Activity: Midterm Project
Date Created: 10/24/2023
Last Modified: 10/29/2023

Purpose: The project is a battling game where you choose your character and go through a series of 5 battles. When the program launches, the user is prompted to either see or skip the prologue. The prologue is recommended for first time players, but users can skip it if they know it already. Next, the game prompts the users to select their character. Each character has their own elemental type, unique moveset, and different internal stats (health, attack, defense, speed, dexterity).

The internal stats have the following characteristics:
Health: Governs how much health you have
Attack: Governs how much damage you do
Defense: Governs how much damage you take
Speed: Governs who attacks first (you or opponent)
Dexterity: Governs your hit and crit chanace

The elemental types have the following properties:
Fire Types deal extra damage against Wind Types
Wind Types deal extra damage against Earth Types
Earth Types deal extra damage against Water Types
Water Types deal extra damage against Fire Types

After selecting your character, you start battling. During battle, you can use 4 moves - 3 unique moves and a potion that heals you. The potion has limited uses per battle. If you use an attacking move, the game will internally use random luck to determine if the attack misses, and if the attack is a critical hit (double damage). Each battle ramps up in difficulty. The last battle is the hardest; if you beat the last battle you beat the game.

Instructions:

When prompted to view the prologue, enter either Yes or No

When prompted to choose your Bissellmon, enter one of: Singlish, Merraticus, Rossjamus, Xelanahor

When prompted to enter your move, enter either 1, 2, 3, 4, corresponding to which number represents what action. Be strategic!

Sample Output:

**** Welcome to the Wonderful World of Bissellmon! ****
>Would you like to view the prologue Yes or No: 

(the prologue is very long so I will not output it, but it is just flavor text and world building)

Choose your Bissellmon: singlish

>You choose Singlish!

JASON: Singlish eh? That's a nice choice. Now, let's get to battling! Let's start off with something easy.

Commencing battle, your oppoment is Tersisa


YOUR HP: 50
OPPONENT HP: 30


*** YOUR MOVES ***
1. Flaming Strike - strike the opponent with fire
2. Stoke Fire - increase self attack
3. Grim Glare - decrease opponent defense
4. Potion - heals 20 hp (uses left: 5)
Enter your choice: 

1


>You used Flaming Strike!
>Critical hit!
>You dealt 28 damage!
>The opponent attacks!
>The opponent dealt 1 damage!


YOUR HP: 49
OPPONENT HP: 2


*** YOUR MOVES ***
1. Flaming Strike - strike the opponent with fire
2. Stoke Fire - increase self attack
3. Grim Glare - decrease opponent defense
4. Potion - heals 20 hp (uses left: 5)
Enter your choice:
