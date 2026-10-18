
full_dot = '●'
empty_dot = '○'
def create_character(character_name,strength,intelligence,charisma):
    if type(character_name) != str:
        print("The character name should be a string")
    elif not character_name:
        print("The character should have a name.")
    elif len(character_name)>10:
        print("The character name is too long")
    elif " " in character_name:
        print("The character name should not contain spaces")
    elif type(strength)!= int and type(intelligence)!= int and type(charisma)!= int:
        print("All stats should be integers")
    elif strength<1 and intelligence<1 and charisma<1:
        print("All stats should be no less than 1")
    elif strength>4 and intelligence>4 and charisma>4:
        print("All stats should be no more than 4")
    elif strength+intelligence+charisma !=7:
        print("The character should start with 7 points")
    else:
        str_dots=full_dot*strength
        int_dots=full_dot*intelligence
        cha_dots=full_dot*charisma
        str_empty_dots=empty_dot*(10-strength)
        int_empty_dots=empty_dot*(10-intelligence)
        cha_empty_dots=empty_dot*(10-charisma)
        print(character_name)
        print("STR "+str_dots+str_empty_dots)
        print("INT "+int_dots+int_empty_dots)
        print("CHA "+cha_dots+cha_empty_dots)
create_character("Anu",2,3,2)
