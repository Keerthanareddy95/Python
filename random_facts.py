import random
facts = ["Bananas Are Berries, But Strawberries Aren’t – Botanically speaking, bananas qualify as berries, but strawberries do not!",

"Octopuses Have Three Hearts – Two pump blood to the gills, while the third pumps it to the rest of the body.",

"A Group of Flamingos Is Called a 'Flamboyance' – The bright pink birds form an aptly named, colorful gathering!",

"Honey Never Spoils – Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",

"Wombat Poop Is Cube-Shaped – This helps it stay in place, preventing it from rolling away and marking their territory effectively.",

"Sharks Are Older Than Trees – Sharks have been around for about 400 million years, while the first trees appeared around 350 million years ago.",

"Cleopatra Lived Closer to the Moon Landing Than to the Building of the Pyramids – The Great Pyramid was completed around 2560 BC, while Cleopatra lived around 30 BC.",

"Scotland Has 421 Words for 'Snow' – Some of these include “sneesl” (to start raining or snowing), “feefle” (to swirl), and “flindrikin” (a slight snow shower).",

"The World's Oldest Known Joke Is a Sumerian Fart Joke – Dating back to 1900 BC, it shows humanity's long-standing love of humor!",

"Sloths Can Hold Their Breath Longer Than Dolphins – Sloths can slow their heart rate and hold their breath for up to 40 minutes, whereas dolphins need to surface every 10-15 minutes."]

print("""
Hi, This is a fun fact generator program.
      Hope you enjoy it!
""")
user_input = int(input("Enter any number between 1 to 10 to generate a fun fact: "))

if user_input <= 10:
    print(random.choice(facts))

