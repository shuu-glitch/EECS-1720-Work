#!/usr/bin/python3


import sys
import os
import random
import time


### FORMATTING.
class Game:
    def commands(self):
        print("""\n Enter commands to interact with the world.\n
    'help'     ----    shows commands
    'quit'     ----    quits current game
    'M'        ----    restores health (via a medkit)
    'drink'    ----    restores thirst (costs mystery water)
    'health'   ----    shows current health, energy, hunger and thirst
    'items'    ----    shows inventory""")

    ## MENU FOR GAME + COMMANDS FOR HELP AND OTHERWISE.
    def menu(self):
        self.reset_console()
        self.fprint("Trickery")
        print("Version 1.1")
        self.print_slow("Hello, and welcome to Trickery.\n")
        self.fprint("Please enter 'play' to start the game, 'help' for extra commands, 'info' for information about the game, and 'quit' to quit the game.", 0.8)
        while True:
            choice = input("\n> ")
            if choice == "play":
                new_world.load_intro()
            elif choice == "quit":
                sys.exit()
            elif choice == "help":
                self.commands()
            elif choice == "info":
                self.fprint("© Lilian Ilodigwe 2022. Made for an EECS1720 lab project.")
            elif choice == "items":
                new_world.print_items()
            elif choice == "M":
                new_world.check_medkit()
            elif choice == "drink":
                pass
            elif choice == "health":
                new_world.check_statistics()
            else:
                self.fprint("ERROR. Enter 'play' to launch the game, 'load' to load game, 'quit' to quit, 'info' for info, or 'help' for help.")
    
    
    def play_again(self):
        self.fprint("Do you want to play again?", 1)
        print("Enter 'yes' or 'no'.")
        while True:
            choice = input("\n> ")
            if choice == "yes":
                self.menu()
            elif choice == "no":
                self.fprint("GOODBYE, THEN.", 0.4)
                sys.exit()
            else:
                self.fprint("Invalid command!")


    # creates a dramatic effect; words prints on screen like a typewriter.
    def print_slow(self, str, delay = 0.1):
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(delay)
        print("\n")

    # if you enter a new function, this clears the screen.
    def reset_console(self):
        print("\n")
        os.system('cls||clear')

    # fprint = "format print"; makes it print nicer.
    def fprint(self, str, delay = 0):
        print("\n" + str)
        time.sleep(delay)

    # sprint is somewhat similar to the above function's functionality.
    def sprint(self, str, delay = 0):
        print(str)
        time.sleep(delay)


game_functions = Game()


# PLAYER AND OTHER NPC CATEGORIES:
class player:
    def __init__(self, health, hunger, thirst, location, items, gold, shotgun_ammo, grenades):
        self.health = health
        self.hunger = hunger
        self.thirst = thirst
        self.location = location
        self.items = items
        self.gold = gold
        self.shotgun_ammo = shotgun_ammo
        self.grenades = grenades
        
    
chara = player(100, 82, 96, "entrance", [], 50, 0, 0)


class NPC:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def talk(self):
        surfaces_available = ["right wall", "left wall", "ceiling", "floor", "ground", "corner", "wall behind you", "wall in front of you"]
        surface_chosen = random.choice(surfaces_available)
        game_functions.fprint(f"A {self.name} emerges from the " + surface_chosen + ".")
        game_functions.fprint("'What the hell are you doing here? Get out!'")
        self.combat()

    def move(self):
        available_locations = ["hallway", "controlRoom", "artificial", "store"]
        self.location = random.choice(available_locations)

    # COMBAT:
    def combat(self):
        print("Will you run (r) or talk (t)? Enter the corresponding letter with the option.")
        while True:
            choice = input("\n> ")
            if choice == "r":
                escape = random.choice([True, False])
                if escape == True:
                    time.sleep(2)
                    game_functions.fprint("You manage to escape.")
                    break
                elif escape == False:
                    time.sleep(2)
                    game_functions.fprint("You cannot escape! The survivor shoots you in the back of the head as you turn to run.")
                    new_world.die()
            elif choice == "t":
                aggression = random.choice([True, False])
                if aggression == True:
                    game_functions.fprint("The survivor pulls out a gun.")
                    time.sleep(2)
                    game_functions.fprint("'There's no room for the both of us in this world.'")
                    new_world.die()
                elif aggression == False:
                    new_world.dialog()
            else:
                game_functions.fprint("Invalid command!")


survivor = NPC("Survivor", "controlRoom")

### WHERE THE GAME STARTS.
class World:
    def load_intro(self):
        game_functions.reset_console()
        print("\n")
        game_functions.print_slow("Loading.....", 0.4)
        game_functions.reset_console()
        game_functions.fprint("Do you want to skip the intro?")
        game_functions.fprint("Enter 'yes' or 'no'.")
        while True:
            choice = input("\n> ")
            if choice == "yes":
                game_functions.reset_console()
                game_functions.fprint("You wake up in darkness.")
                self.entrance()
            elif choice == "no":
                self.intro()
            else:
                game_functions.fprint("ERROR.")

    def intro(self):
        game_functions.reset_console()
        print("\n")
        game_functions.print_slow("The last place you were in was a maze; repetitive and mechanical in nature.")
        game_functions.print_slow("You don't think you survived. After all, everywhere around your limited and non-existent scope of vision is dark.")
        game_functions.print_slow(".............")
        game_functions.print_slow("'Am I dead?', you ask no one in particular. At this rate, you hope you are.")
        print("\n")

        # TAKE THE PLAYER'S USERNAME.
        game_functions.fprint("What is your name?")
        username = input("\n--> ")
        playerIGN = username

        game_functions.print_slow(".............")
        game_functions.fprint("Lovely. Let's get started then, " + playerIGN + ".")
        
        game_functions.print_slow("You're on your own.")
        time.sleep(2)
        game_functions.reset_console()
        game_functions.fprint("You wake up in darkness.")
        self.entrance()

    
    def entrance(self):
        chara.location = "entrance"
        print(f"\nHealth: {chara.health}")
        game_functions.fprint("You feel as if you've been here for hours, but you've only just woken up. You try to backtrack; but where is there to go when everything looks the same?", 2)
        print("After spending a few more moments in total darkness, something catches your eye, whirring to life off to your left. A wall opens up, falls away like decaying foliage, and a hallway is revealed to you - with high-tech lighting in a singular violet strip on the walls that rounds a bend. It's not much, but it's lighter compared to what you were just in a second ago. Do you continue?")
        print("Enter 'yes' or 'no'.")
        while True:
            choice = input("\n> ")
            if choice == "yes":
                self.hallway() # continuing on in the game.
    
            elif choice == "no":
                self.check_knife_attack() # knife attack chance
                game_functions.fprint("Do you move now?")
                print("Enter 'yes' or 'no'.")
                while True:
                    crucial = input("\n> ")
                    if crucial == "yes":
                        self.hallway()
            
                    elif crucial == "no":
                        self.badEnd1()
    
            else:
                game_functions.fprint("You choose to sit in total darkness.")    


    # BAD END #1.
    def badEnd1(self):
        chara.location = "entrance"
        print(f"\nHealth: {chara.health}")
        game_functions.fprint("The knife keeps going; though no hand is holding it, it continues to stab and cut into flesh, until you are merely meat on the ground, unable to move. Though you aren't dead, you're not regenerating. You're not respawning.") 
        game_functions.fprint("A foot appears where your eyes are affixed. You're unable to look up at your assumed attacker; you have no strength to do so. But you can hear a woman laughing in the distance, even though she's right in front of you.")
        game_functions.fprint("'Looks like you don't get to come back this time; if you're choosing to be so stubborn!'")
        game_functions.print_slow("GOODBYE.")
        sys.exit()


    def hallway(self):
        chara.location = "hallway"
        print(f"\nHealth: {chara.health}")

        game_functions.fprint("You follow the yellow brick road (except it's actually just a hallway with metallic floors, walls, and ceiling segments), and you round the bend, keeping your hand on the continuing source of light - as if should you cease to be in contact with it, it would leave you in the dark again.", 2)
        print("It's a straight path, despite the curvature; there's no forks in the road, no opportuntities to slip out of this narrow space that herds you towards an unknown destination. The hallway seems like it has no end. Do you still press on?")
        print("Enter 'yes' or 'no'.")
        while True:
            choice = input("\n> ")
            if choice == "yes":
                self.controlRoom() # continuing on in the game.
    
            elif choice == "no":
                self.abyss() # straight to BAD END #2.
    
            else:
                game_functions.fprint("You choose to sit in total darkness.")
                self.handle_surv()


    def controlRoom(self):
        chara.location = "controlRoom"
        print(f"\nHealth: {chara.health}")

        game_functions.fprint("Eventually, the hall ends. After what feels like hours of following this strange linear light, you arrive in a wide-open room, with machinery that seems familiar yet alien at the same time. You don't know what to make of it, so you nervously look back.", 2)
        game_functions.sprint("The hallway behind you as just as endless as you remember it, with no clear indication of where the bend you'd turned earlier even was.", 1.5)
        print("You can, however, swear that you see something at the further recesses of the hall. It barely looks like a person - more like a shadow that blocks the light on one side. But it's still person-shaped.")
        print("Doesn't mean that unnerving feeling of being watched disappears; doesn't mean that you feel more secure. But the wall - or door system, supposedly - shuts, blocking off your and that ... THING for the time being.")
        print("What do you do now, that you have the \"freedom\" to explore again?")
        print("Enter 'look around' to look around, or enter 'stay put' to do the opposite.")
        while True:
            choice = input("\n> ")
            if choice == "look around":
                game_functions.fprint("You look at the machinery and the objects scattered in the room once more. Though that feeling of familiarity is still there, you still can't make heads nor tails of what you're looking at.")
                game_functions.sprint("Nobs, gears, doo-hickeys and doo-dads; they all are thin, sleek, but vast and interconnected.")
                print("You don't dare to touch anything on three of walls - on account of them all being similar in nature. But off to the right, close to the corner, is a big, red button.")
                print("Do you press it?")
                while True:
                    choice = input("\n> ")
                    if choice == "yes":
                        self.check_medkit() # medkit check
                        self.store_event()
                        self.dog_chance()
                        self.handle_surv()
                        self.outsideQ()
                    elif choice == "stay put":
                        game_functions.fprint("\"What am I, crazy? I remember what happened the last time you made me do this in the other game!\"")
                        self.store_event() # chance to spawn store
                        self.handle_surv() # chance to spawn survivor
                        self.dog_chance() # chance to spawn dog

                    # copy and paste this afterwards into other loops just in case one decides to save their medkit for later use.
                    elif choice == "M":
                        self.use_medkit()

                    else:
                        game_functions.fprint("Not an option.")
                        self.store_event()
                        self.dog_chance()
                        self.handle_surv()

    
            elif choice == "no":
                game_functions.fprint("You look, but you don't touch anything.")
    
            else:
                game_functions.fprint("You look, but you don't touch anything. Won't you let curiousity take over?")


    # BAD END #2.
    def abyss(self):
        chara.location = "abyss"
        print(f"\nHealth: {chara.health}")

        game_functions.fprint("You pause once the though crosses your mind. \"I don't want to go any further,\" you can clearly hear yourself saying - but your mouth feels like sandpaper, pain sparking in every nerve as you speak.", 2)
        game_functions.sprint("The longer you stand there, the heavier your chest gets. You REALLy can't be bothered to go further. You really need to sit down. You want to close your eyes, you want to return to that blissful darkness that you were scared of moments ago.")
        game_functions.sprint("It would be better than the fresh waves of agony that wrack your tired mind and body; overstimulating it to its death.", 3)
        print("...Why did you stop?")

        print("GAME OVER.") # END GAME HERE; GIVE OPTION TO RESTART.
        print("Do you wish to do it all over again?")
        game_functions.fprint("Enter 'yes' or 'no'.")
        while True:
            continueOn = input("\n> ")
            if continueOn == "yes":
                game_functions.play_again()
            
            if continueOn == "no":
                sys.exit() # quits the game.


    def outsideQ(self):
        chara.location = "artificial"
        print(f"\nHealth: {chara.health}")
        game_functions.fprint("You found a cabin inside of a large room; an artificial environment. Do you want to explore it?", 1)
        game_functions.fprint("Enter 'yes' or 'no'.")
        while True:
            choice = input("\n> ")
            if choice == "yes":
                event = random.choice([True, False])
                if event == True:
                    amount = random.randint(1, 1001)
                    game_functions.fprint(f"As you enter the cabin and look around the otherwise empty space, you find {amount} gold. There is a locked trapdoor in the middle of the house, but you decide not to open it for some reason.")
                    chara.gold += amount
                    self.store_event()
                    self.dog_chance()
                    self.handle_surv()
                    self.outsideQ() # intentional; it's a looping room :)
                elif event == False:
                    game_functions.fprint("As you search the cabin, a man comes out of the trapdoor in the floor that you previously noted, dressed in a labcoat and a singular black mask that completely obscures any facial features he may have had. He charges in your direction almost immediately, slashing you with a hatchet.")
                    chara.health -= random.randint(1,100)
                    print(f"\nHealth: {chara.health}")
                    if chara.health == 0:
                        self.die()
                    else:
                        game_functions.fprint("You run out the front door and around to the back of the house, through the large metal door looks so out of place.")
                        self.store_event()
                        self.dog_chance()
                        self.handle_surv()
                        self.outsideQ()
                        # random chance for store + dog or surv to appear.
            elif choice == "no":
                game_functions.fprint("You decide to ignore the odd cabin, and you go towards the back of the house, exiting the room through the large metal door the wooden house obscured.")
                self.outsideQ() # intentional; it's a looping room :)
            else:
                game_functions.fprint("Bad time to enter that.")
                self.store_event()
                self.dog_chance()
                self.handle_surv()


    # VISITNG THE RANDOM-CHANCE STORE.
    def storefront(self):
        chara.location = "store"
        print(f"\nHealth: {chara.health}")
        game_functions.fprint("You were transported to a storefront at random. It's a bench sheltered by the walls and the ceiling - a cordoned-off segement with various items laid out of the table. Should you peruse?")
        print("Enter 'buy' or 'leave'.")
        while True:
            choice = input("\n> ")
            if choice == "leave": # leave the shop.
                game_functions.fprint("You left the shop.")
                self.handle_surv()
                self.outsideQ()
                # insert function that takes you a random set of functions or a new place here.
            elif choice == "buy": # buy items in the shop.
                store_inventory = {
                    '1': ("Dagger", random.randint(25, 45), "A sturdy dagger."),
                    '2': ("Shotgun", random.randint(500, 600), "A shotgun."),
                    '3': ("Shotgun Shell", random.randint(50, 70), "A singular shotgun shell."),
                    '4': ("Water", random.randint(10, 20), "Some mysterious, purple water."),
                    '5': ("Grenade", random.randint(100, 200), "A grenade."),
                    '6': ("Medkit", random.randint(25, 45), "A medkit, worn but useful.")
                }
                game_functions.fprint("\"THE STRANGER'S DEN:\"\n")
                for key, item_data in store_inventory.items():
                    item, cost, description = item_data
                    print(f"A {item}({key}) costs {cost} gold.")
                game_functions.fprint(f"You have {chara.gold} gold.")
                game_functions.fprint("Enter 'exit' if you don't want to buy anything.")
                while True:
                    choice = input("\n> ")
                    if choice in store_inventory:
                        item, cost, description = store_inventory[choice]
                        self.buy(item, cost, description)
                        game_functions.fprint("Press 'exit' at this time to return to the menu and leave the shop, if you'd like - or buy more trinkets.")
                    elif choice == "exit":
                        game_functions.fprint("Enter 'buy', 'sell', or 'leave'.")
                        break
                    else:
                        game_functions.fprint("'I don't have that quite yet. Sorry, friend.'")
            else:
                game_functions.fprint("Invalid command.")


    # MYSTERY "DOG" SPAWN CHANCE.
    def strangeDog(self):
        chara.location = "dog"
        print(f"\nHealth: {chara.health}")
        gift = random.choice(["ritual knife", "mysterious water", "rations", "medkit"])
        chara.items.append(gift)
        if gift == "ritual knife":
            game_functions.fprint("A strange dog trots up to you, eyes glowing white with a body as black as the shadows it emerges from. It holds a ornate ritual knife in its mouth, which it drops on the ground before you, returning the way it came. You continue on.")
        elif gift == "mysterious water":
            game_functions.fprint("A strange dog trots up to you, eyes glowing white with a body as black as the shadows it emerges from. A bottle of cold, yet purple water is placed on the floor in front of your feet - and when you look back up, the dog is gone. You continue on.")
        elif gift == "medkit":
            game_functions.fprint("A strange dog trots up to you, eyes glowing white with a body as black as the shadows it emerges from. It gives you a medkit that dangles from its jaw, free of charge. You continue on.")
        self.outsideQ()


    # TRUE ENDING.
    def true_ending(self):
        game_functions.fprint("'You see, this place is merely a stop between worlds. A reset button was hit, and now, we're in the instance between then and the reset. Or, at least, I've been here longer than you have. You just got here.'")
        game_functions.fprint("'How long does the reset last? Who can say. Could be minutes. Could be hours. Could be days. It could be years and years until someone else opens up the same game again.'")
        game_functions.fprint("'Oh, yes. This is a game. Well, not this part, but we're in the place between games. Where characters go to rest ... and some, die. After all, just because the computer stops running doesn't mean the monsters do. I'm sure you saw something in the hallway or somewhere else at some point that could be a clear example of that.'")
        game_functions.fprint("'I've survived this long, longer than everyone else that's come here to rest because I know not to trust what I see. Being well-equipped does help, but being smart covers enough bases. But that won't last forever.'")
        game_functions.print_slow("'........'")
        game_functions.fprint("'Someone has to open up THAT world again. And then you have to keep playing through it, and keep coming back here, surviving long enough to remember the truth and repeat the process again and again. You're in luck, though ...'")
        game_functions.fprint("The survivor transforms before you, and a familiar sight comes to you. Now you remember - the hallways being the same as the first time you traversed that other land., the control room having similar facilities and even the same big button for you to press and progress. This time though, there was no threat in that room. But the same person from that time was here, white hair and black robes fluttering with an unseen wind behind it.")
        game_functions.print_slow("'........Hello again~!'")
        game_functions.print_slow("She's insane.")
        game_functions.print_slow("And she's followed you here, too.")
        self.end_it()

    
    # FUNCTIONS THAT AID IN REFACTORING PARTS OF CODE.
    def use_medkit(self):
        if "medkit" in chara.items:
            chara.items.remove("medkit")
            game_functions.fprint("You used your medkit.")
            chara.health = 100 # could make it a random heal lmao
            print(f"\nHealth: {chara.health}")
        else:
            game_functions.fprint("You don't have any healing items in your inventory.")

    
    def handle_surv(self):
        survivor.move()
        if chara.location == survivor.location:
            countTalk = 0
            survivor.talk()
            countTalk += 1


    def check_medkit(self):
        medkit_find = random.choice([True, False])
        if medkit_find is True:
            chara.items.append("medkit")
            game_functions.fprint("You picked up a medkit.", 2)
            print("Enter 'M' to use your medkit at any time.")


    def check_knife_attack(self):
        knife_attack = random.choice([True, False])
        if knife_attack is True:
            game_functions.fprint("A knife finds its mark in your lower back; missing vital structures thankfully, but that doesn't make the pain any less meaningful.")
            chara.health -= random.randint(1,100)
            print(f"\nHealth: {chara.health}")

            if chara.health == 0:
                self.die()

    # CHANCE FOR STORE TO APPEAR.
    def store_event(self):
        storeChance = random.choice([True, False])
        if storeChance == True:
            self.storefront()

    # CHANCE FOR STRANGE DOG TO APPEAR.
    def dog_chance(self):
        dogChance = random.choice([True, False])
        if dogChance == True:
            self.strangeDog()

    # PRINT ITEMS TO DISPLAY.
    def print_items(self):
        self.update_ammo()
        game_functions.fprint("BACKPACK:")
        print("Gold:", chara.gold)
        print("Shotgun Ammo:", chara.shotgun_ammo)
        print("Grenades:", chara.grenades)
        for things in chara.items:
            print(things)
            print(chara.items)


    # DIALOGUE:
    def dialog(self):
        game_functions.fprint("The survivor lifts out their hand.", 2)
        game_functions.fprint("'Stay back. If you're not human, I'm warning you - stay the hell back!'")
        while True:
            game_functions.fprint("What do you tell them?")
            print("(1) 'I mean no harm. I'm just someone who landed ... here? Like yourself. I'll just go somewhere else.'")
            print("(2) 'I don't feel human. I feel dead.'")
            choice = input("\n> ")
            if choice == "1":
                game_functions.fprint("The survivor nods once after a tense while, and leaves you be.")
                break
            if choice == "2":
                game_functions.fprint("'What's that? You feel dead? Well, I hate to tell you that where you are is much worse than that.'")
                game_functions.fprint("'Have you been to the control room yet?'")
                while True:
                    choice = input("\n> ")
                    if choice == "yes":
                        game_functions.fprint("'Ah, good. Have you been to that weird outside simulation?'")
                        choice = input("\n> ")
                        if choice == "yes":
                            game_functions.fprint("'Good, so I can tell you. Everything.'")
                            self.true_ending()
                        else:
                            game_functions.fprint("'Well, that's unfortunate. Can't tell you anything if you haven't seen it for yourself.'")
                            game_functions.print_slow("Loading...........")
                            self.outsideQ()
                    else:
                        game_functions.fprint("'Well, that's unfortunate. Can't tell you anything if you haven't seen it for yourself.'")
                        game_functions.print_slow("Loading...........")
                        self.controlRoom()

    # PLAYER STATS + STAT LOSS:
    def check_statistics(self):
        print(f"\nHealth: {chara.health}")
        print(f"\nHunger: {chara.hunger}")
        print(f"\nThirst: {chara.thirst}")

    def lose_health(self):
        self.health -= 1
        print(f"\nHealth: {chara.health}")
        if self.health < 0:
            self.health = 0
        if self.health == 0:
            self.die()

    def lose_hunger(self):
        self.hunger -= random.randint(1, 6)
        print(f"\nHunger: {chara.hunger}")
        if self.hunger < 0:
            self.hunger = 0
        if self.hunger == 0:
            self.lose_health()

    def lose_thirst(self):
        self.thirst -= random.randint(1, 6)
        print(f"\nThirst: {chara.thirst}")
        if self.thirst < 0:
            self.thirst = 0
        if self.thirst == 0:
            self.lose_health()

    # STORE AND WEAPON FUNCTIONALITY.
    def update_ammo(self):
        total_shotgun_ammo = chara.items.count("Shotgun Shell")
        total_grenades = chara.items.count("Grenade")
        chara.shotgun_ammo += total_shotgun_ammo
        chara.grenades += total_grenades
        while "Shotgun Shell" in chara.items:
            chara.items.remove("Shotgun Shell")
        while "Grenade" in chara.items:
            chara.items.remove("Grenade")

    def buy(self, item, cost, description):
        if chara.gold >= cost:
            chara.items.append(item)
            chara.gold -= cost
            game_functions.fprint("'Here you go!'")
            game_functions.fprint(f"You bought {description}.")
        else:
            game_functions.fprint("Sorry, you don't have enough for this.")

    # DEATH COMES FOR US ALL :)
    def die(self):
        time.sleep(2)
        game_functions.fprint("YOU DIED.", 2)
        game_functions.play_again()

    def end_it(self):
        time.sleep(4)
        game_functions.fprint("TRUE ENDING: SELF-PROMOTION(?).", 2)
        game_functions.play_again()


### TO CREATE AN INSTANCE OF THE GAME.
new_world = World()

game_functions.menu()