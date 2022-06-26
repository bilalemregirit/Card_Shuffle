#çok güzel

import random

suits=['Hearts','Spades','Clubs','Diamonds']
values=['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
all_cards =[]

for x in suits:
    for y in values:
        all_cards.append(x +' '+ str(y)) 

p1=[]
p2=[]
p3=[]
p4=[]
p5=[]
p6=[]
people = [p1,p2,p3,p4,p5,p6]
number_of_people = int(input("Kisi Sayisini Giriniz:"))

##card_per_people = int(52 / number_of_people)
card_per_people = 5

people_in_game = people[0:number_of_people]

for x in people_in_game:
    for y in range(card_per_people):
        random_choice = random.choice(all_cards)
        all_cards.pop(all_cards.index(random_choice))
        x.append(random_choice)
              
print("kalan kartlar: ",all_cards)        
print("p1: ",p1)
print("p2: ",p2)
print("p3: ",p3)
print("p4: ",p4)
print("p5: ",p5)
print("p6: ",p6)
