import random

lower_characters =['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
upper_characters = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
numbers_characters = ['1','2','3','4','5','6','7','8','9','0']
special_chars = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=',',']
non_alphabetic = numbers_characters + special_chars
key = "lkmkcs98sdmscDLKMdf"
message = "The quick brown fox jumped over the fence"
encrypted_message = ''
lowers = []
uppers = []
numbers = []

for index, character in enumerate(key):
    if character.islower():
        lowers.append(index)
    elif character.isupper():
        uppers.append(index)
    elif character.isnumeric():
        numbers.append(index)


#print(uppers)
#print(lowers)
#print(numbers)

combined = []
order = []
while len(order) != 3:
    suggested = random.randint(1,3)
    if suggested not in order:
        encrypted_message = encrypted_message + special_chars[suggested]
        order.append(suggested)
        if suggested == 1:
            combined = combined + uppers
        elif suggested == 2:
            combined = combined + lowers
        else:
            combined = combined + numbers_characters

print(order)
print(combined)

for index,message_character in enumerate(message):
    for index,order_by in enumerate(combined):
        if index % len(order) == 0:
            pass
            print(upper_characters[index])
        elif index % len(order) == 1:
            pass
            #print(lower_characters[index])
        else:

            print(f'{index} is the index\nCombined ends at {len(combined)-1}\nNon numeric ends at {len(non_alphabetic)}')
            print(len(non_alphabetic) % index)
            if len(combined) < index :
                print(non_alphabetic[len(non_alphabetic) % index])
            else:
                print(non_alphabetic[index])
            print(order_by)

        """
        if index == 1:
        elif index == 2:
        elif index == 3:
        """


"""
sorted_by = random.randint(0,10)
print(sorted_by)
ordered_by = [len(uppers), len(lowers), len(numbers)]
ordered_by.sort(reverse=True if sorted_by % 2 == 0 else False)
print(ordered_by)
grouped_by = random.randrange(1,3)
combined = None
if grouped_by == 1:
    combined = uppers + lowers + numbers
elif grouped_by == 2:
    combined = numbers + lowers  +uppers

ko = []
for order in key:
    ko.append(random.randint(0, len(key)-1))

print(ko)
#print(grouped_by)


encrypted_message = encrypted_message + str(grouped_by)
for index,k in enumerate(ko):
    if grouped_by == 1:
        if index % 3 == 0: 
            encrypted_message = encrypted_message + upper_characters[k]
        if index % 3 == 1: 
            encrypted_message = encrypted_message + lower_characters[k]
        if index % 3 == 2: 
            pass

    elif grouped_by == 2:
        if index % 3 == 0: 
            encrypted_message = encrypted_message + lower_characters[k]
        if index % 3 == 1: 
            encrypted_message = encrypted_message + upper_characters[k]
        if index % 3 == 2: 
            pass
"""


print(encrypted_message)