"""Classes for Lviv game"""
class Gamer:
    """Class for a user"""
    def __init__(self , name) -> None:
        """Construcrs a gamer"""
        self.lives = 1
        self.name = name
        self.backpack = []

    def add_to_backpack(self , item):
        """Apends to the backpack"""
        self.backpack.append(item)
    
    def add_lives(self,quantity):
        """Adds lives"""
        self.lives += quantity
    
    def minus_lives(self,quantity):
        """Minuses lives"""
        self.lives -= quantity

class Character:
    """Class - character"""
    def __init__(self,name,description) -> None:
        """Constructs a character"""
        self.name = name
        self.description = description
    
    def set_conversation(self,conversation):
        """Sets the character's conversation"""
        self.conversation = conversation
    
    def talk(self):
        """Displays the conversation of the character"""
        print(self.conversation)

class Enemy(Character):
    """Class - enemy"""
    def __init__(self, name,description) -> None:
        """Constructs an enemy"""
        super().__init__(name,description)
        self.weakness = None
        self.__lives = None

    
    def set_weakness(self,weakness):
        """Sets the weakness of the enemy"""
        self.weakness = weakness

    def set_lives(self,lives):
        """Sets the quantity of lives to the character"""
        self.__lives = lives
    
    def get_info(self):
        """Displays the info about the character"""
        print('Your enemy is called - ',self.name)
        print('This enemy has these many lives - ',self.__lives)
        print('His weakness is - ', self.weakness)
        if isinstance(self,EnemyBoss):
            print('His soft spot is - ',self.soft_spot)
    
    def set_conversation(self, conversation):
        """Sets the conversation"""
        self.conversation = conversation
    
    def talk(self):
        """Talks with the gamer"""
        return self.conversation
    
    def fight(self , fight_with):
        """Fights with the gamer"""
        if fight_with == self.weakness:
            return True
        return False
    
    def info(self):
        """Gets info about the enemy"""
        print('Your enemy is - ', self.name)
        print()
        print(self.description)
        print()
        print(self.name, 'says: ',self.conversation)

class EnemyBoss(Enemy):
    """Class - enemy boss"""
    def __init__(self, name, description) -> None:
        """Constructs an enemy boss"""
        super().__init__(name, description)
        self.weakness = None
        self.soft_spot = None
    
    def set_lives(self, lives):
        """Set the lives of the enemy boss"""
        return super().set_lives(lives)
    
    def set_weakness(self, weakness):
        """Set the weakness of the enemy boss"""
        return super().set_weakness(weakness)
    
    def set_soft_spot(self,soft_spot):
        """Sets the soft spot of the mafia boss"""
        self.soft_spot = str(soft_spot)
    
    def get_info(self):
        """Gets the info about the enemy boss"""
        return super().get_info()
    
    def set_conversation(self, conversation):
        """Sets the conversation"""
        return super().set_conversation(conversation)
    
    def fight(self, fight_with,spot_to_harm):
        """Fifght with the enemy boss"""
        if self.weakness == fight_with and spot_to_harm == self.soft_spot:
            return True
        return False

class Friend(Character):
    """Class Friend"""
    def __init__(self, name, description) -> None:
        """Constructs a friend"""
        super().__init__(name, description)

    def set_conversation(self, conversation):
        """Sets the conversation"""
        return super().set_conversation(conversation)
    
    def set_advice(self,advice):
        """Sets the advice which the friend will give"""
        self.advice = advice
    
    def give_advice(self):
        """Gives an actual advice"""
        return self.advice


class Item:
    """Class Iteem"""
    def __init__(self,name) -> None:
        """Constructs an item"""
        self.name = name

    def set_description(self,description):
        """Set the description of an item"""
        self.description = description
    
    def describe(self):
        """Describes an item"""
        print('This item is called - ',self.name,'. ',self.description)

    def __repr__(self) -> str:
        """Represents an item"""
        return f'{self.name}'

class MedicalKit(Item):
    """Medical Kit - item with use"""
    def __init__(self, name) -> None:
        """Constucts a medical kit"""
        super().__init__(name)

    def set_add_lives(self,lives):
        """Adds lives """
        self.lives_to_add = lives
    
class Weapon(Item):
    """Class weapon"""
    def __init__(self, name) -> None:
        """Comstructs a weapon"""
        super().__init__(name)
    
    def set_minus_lives(self,lives):
        """Minuses lives"""
        self.minus_lives = lives

class Location:
    """Class Location"""
    def __init__(self,name) -> None:
        """Constructs a location"""
        self.name = name
        self.lst_ways = []
        self.item = None
        self.inhabitants = []


    def link_location(self,location,vector):
        """Links locations"""
        self.lst_ways.append((location, vector))
    
    def set_description(self,description):
        """Sets description of an item"""
        self.description = description
    
    def set_item(self,item):
        """Sets the item to the place"""
        self.item = item
    
    def set_character(self,character):
        """Sets the character to the place"""
        self.character = character
    
    def move(self,command):
        """Movement of the character"""
        for way in self.lst_ways:
            if way[1] == command:
                return way[0]
    
    def set_character(self , character):
        """Sets character to the list of room inhabitants"""
        self.inhabitants.append(character)