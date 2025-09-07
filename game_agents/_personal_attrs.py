from dataclasses import dataclass


@dataclass
class Allegiance:
    whom:str
    amount:int
    
    
@dataclass
class PersonalAtrrs:
    strength: int
    intelligence: int
    dexterity: int
    constitution: int
    charisma: int
    wisdom: int
    
