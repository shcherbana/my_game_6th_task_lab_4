import my_game

mafia_man = my_game.Enemy('Mafiosi','A man from local mafia group')
mafia_man.set_weakness('Knive')
mafia_man.set_lives(1)
mafia_man.set_conversation('Ooouuu I am going to kill you.Bthw, my boss will be happy!')


mafia_helper = my_game.Enemy('Helper of the local mafia','Helps mafia to find new victims')
mafia_helper.set_weakness('Pepper spray')
mafia_helper.set_lives(1)
mafia_helper.set_conversation('I am going to sell you to my mafia friends and they will kill you!')

mafia_don = my_game.EnemyBoss('Mafia Don','One of the dons in Lviv mafia')
mafia_don.set_weakness('Pistol')
mafia_don.set_lives(3)
mafia_don.set_soft_spot('Heart')
mafia_don.set_conversation('If my helpers did not kill you - I will')


student = my_game.Friend('Student','Student of Lviv university')
student.set_conversation('Hey,I am a student at Lviv uni')
student.set_advice('Stay away from helpers of local mafia.Use peper spray against them!')

old_lviv_women = my_game.Friend('Old women','This women has been living in Lviv for a really long time - she must know everything about local mafia')
old_lviv_women.set_conversation('Good evening, ladies!')
old_lviv_women.set_advice('Find mafia`s soft spot!')

medical_help = my_game.MedicalKit('Medical kit')
medical_help.set_description('This is your medical kit!')
medical_help.set_add_lives(2)

weapon_pistol = my_game.Weapon('Pistol')
weapon_pistol.set_description('You can kill mafia`s members with it')
weapon_pistol.set_minus_lives(3)

weapon_spray = my_game.Weapon('Pepper spray')
weapon_spray.set_description('Use that if you do not want someone to see you!')
weapon_spray.set_minus_lives(1)

weapon_knives = my_game.Weapon('Knives')
weapon_knives.set_description('Use that if someone tries to harm you')
weapon_knives.set_minus_lives(1)

Naukova_street = my_game.Location("Naukova street")
Naukova_street.set_description('One of the longest streets in Lviv, where troleybus run.')
Naukova_street.set_item(weapon_spray)

Stryiska_street = my_game.Location('Stryiska street')
Stryiska_street.set_description('One more long street, which is connected to Kozelnytska street.')
Stryiska_street.set_item(medical_help)
Stryiska_street.set_character(old_lviv_women)


Kozelnytska_street = my_game.Location('Kozelnytska street')
Kozelnytska_street.set_description('Street connected to Stryiska')
Kozelnytska_street.set_item(weapon_knives)
Kozelnytska_street.set_character(student)

Krakivska_street = my_game.Location('The heart of the Lviv - the city center')
Krakivska_street.set_description('The oldest part of the city, it`s soul - the city center')
Krakivska_street.set_character(mafia_helper)
Krakivska_street.set_item(weapon_pistol)

High_Castle = my_game.Location('High castle')
High_Castle.set_description('The highest point in Lviv. Once there was a legend that witches had their meeting there - currently that`s the place for mafia.')
High_Castle.set_character(mafia_don)

Naukova_street.link_location(Stryiska_street, 'north')
Naukova_street.link_location(Krakivska_street ,'south')
Stryiska_street.link_location(Kozelnytska_street , 'west')
Stryiska_street.link_location(Krakivska_street, 'east')
Stryiska_street.link_location(Naukova_street, 'south')
Krakivska_street.link_location(Stryiska_street , 'south')
Krakivska_street.link_location(Naukova_street , 'west')
Kozelnytska_street.link_location(Stryiska_street , 'north')
High_Castle.link_location(Krakivska_street, 'east')  
Krakivska_street.link_location(High_Castle , 'north')

current_location = Naukova_street
if __name__ == "__main__":
    print('Enter your name')
    name = input('> ')
    user= my_game.Gamer(name)
    print(f'Hello, {user.name}')
    print('Let me introduce you to this game. This game takes place in a magnificent city called Lviv.')
    print()
    print('This city leaves a peaceful life. However there are some minor problems - mafia. Your goal is to find and deminish all of the mafia members.')
    print()
    print('On your long road you will meet some friends that will be more than eager to help you - you just have to ask for this help.')
    print()
    print()
    print()
    print('Before we start, let me explain you, which commands you can use and what do they mean')
    print()
    print('These are commands that you can use through the game: ')
    print('help - to receive help from your friends')
    print('fight - to fight with your oponents')
    print('take - put item in your backpack')
    print('side of the world(north,east,west,south) - to move from one location to another')
    print()
    print('The condition of your victory - kill the mafia`s bos and meanwhile have fun')
    print('So let`s start!')
    current_room = Naukova_street
    dead = user.lives

    while dead != 0 or dead<0:

        print("\n")
        print(current_room.name)
        print('--------------------')
        print(current_room.description)
        for i in current_room.lst_ways:
            print(f'{i[0].name} is {i[1]}')
        
        inhabitants = current_room.inhabitants
        for i in inhabitants:
            print(f'{i.name} is here - {i.description}')
        enemy = False
        friend = False

        item = current_room.item
        if item is not None:
            print(f'The [{item.name}] is here - {item.description}')

        command = input("> ")
        if command in ["north", "south", "east", "west"]:
            current_room = current_room.move(command)
        elif command == "talk":
            for object in inhabitants:
                if isinstance(object , my_game.Enemy):
                    print(object.talk())
            else:
                print('There is no enemy.')
        elif command == "take":
            if item is not None and isinstance(item,my_game.MedicalKit) == False:
                print("You have new item!You put the " + item.name + " in your backpack")
                user.add_to_backpack(item)
                current_room.item = None
            elif item is not None and isinstance(item,my_game.MedicalKit) == True:
                print('You have two extra lives!')
                user.add_lives(item.lives_to_add)
                print('Currently the quantity of your lives is equal to - ', user.lives)
                current_room.item = None
            else:
                print("There's nothing to take")

        elif command == 'help':
            for obj in inhabitants:
                if isinstance(obj , my_game.Friend):
                    print()
                    print('[',obj.name,'] says', obj.conversation)
                    print(obj.advice)
                    friend = True
            if friend == False:
                print('There is no friend in this room, who can help you')
        elif command == 'fight':
            for obj in inhabitants:
                if isinstance(obj,my_game.Enemy) == True or isinstance(obj,my_game.EnemyBoss):
                    enemy = True
                    inhabitant = obj
                    break
            if enemy == True:
                print('It`s high time to fight with your oponents!')
                inhabitant.info()
                print('Now you have to choose your weapon! Remember all of the pieces of advice, which were given to you by your friends!')
                print('Choose the weapon from your backpack - ',user.backpack)
                fight_with = input('> ')

                if isinstance(inhabitant,my_game.EnemyBoss) == True:
                    if fight_with in list(map(str, user.backpack)):
                        print('Choose a spot in which you want to hit!')
                        print('For example type - Heart, if you want to shoot at chest of your oponent or Head, if you want to shoot there')
                        spot_to_harm = str(input('> '))
                        if inhabitant.fight(fight_with,spot_to_harm) == True:
                            print('Congratulations,you`ve killed the mafia don - this mean that you won the game!')
                            dead = 0
                            exit("The end")

                        else:
                            print('I`m sorry but mafia don has killed you in a horrible fight!You`ve lost')
                            dead = 0
                            exit("The end")

                    
                elif inhabitant == mafia_helper or inhabitant == mafia_man:
                    if fight_with in list(map(str, user.backpack)):
                        if inhabitant.fight(fight_with) == True:
                            print('You deminished one of the mafia`s members. Keep going!')
                            inhabitants.remove(inhabitant)
                        else:
                            user.minus_lives(1)
                            print('You missed! For this reason the quanttity of your lives will be smaller.')
                            print('Currently the quantity of your lives is equal to - ', user.lives)
                            if user.lives == 0 or user.lives<0:
                                print('That is the end the game.')
                                exit("You've lost")
                    else:
                        print('You cannot fight with this')
                else:
                    print('You cannot fight with this item as it is not in your backpack.')
            else:
                print('There is no one to fight with - the space is clear.')
        else:
            print("I don't know how to " + command)
