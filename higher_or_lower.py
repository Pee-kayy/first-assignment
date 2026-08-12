import random

data = [

  {
    "name": "Cristiano Ronaldo",
    "follower_count": "640",
    "description": "Professional Footballer",
    "country": "Portugal"
  },
  {
    "name": "Lionel Messi",
    "follower_count": "505",
    "description": "Professional Footballer",
    "country": "Argentina"
  },
  {
    "name": "Selena Gomez",
    "follower_count": "425",
    "description": "Singer and Actress",
    "country": "United States"
  },
  {
    "name": "Kylie Jenner",
    "follower_count": "395",
    "description": "Media Personality and Businesswoman",
    "country": "United States"
  },
  {
    "name": "Dwayne Johnson",
    "follower_count": "390",
    "description": "Actor and Professional Wrestler",
    "country": "United States"
  },
  {
    "name": "Ariana Grande",
    "follower_count": "375",
    "description": "Singer and Actress",
    "country": "United States"
  },
  {
    "name": "Kim Kardashian",
    "follower_count": "360",
    "description": "Media Personality and Businesswoman",
    "country": "United States"
  },
  {
    "name": "Beyoncé",
    "follower_count": "315",
    "description": "Singer and Songwriter",
    "country": "United States"
  },
  {
    "name": "Khloé Kardashian",
    "follower_count": "305",
    "description": "Media Personality and Businesswoman",
    "country": "United States"
  },
  {
    "name": "Justin Bieber",
    "follower_count": "290",
    "description": "Singer and Songwriter",
    "country": "Canada"
  },
  {
    "name": "Kendall Jenner",
    "follower_count": "290",
    "description": "Supermodel and Media Personality",
    "country": "United States"
  },
  {
    "name": "Taylor Swift",
    "follower_count": "280",
    "description": "Singer and Songwriter",
    "country": "United States"
  },
  {
    "name": "Virat Kohli",
    "follower_count": "270",
    "description": "Professional Cricketer",
    "country": "India"
  },
  {
    "name": "Jennifer Lopez",
    "follower_count": "250",
    "description": "Singer, Actress, and Dancer",
    "country": "United States"
  },
  {
    "name": "Nicki Minaj",
    "follower_count": "225",
    "description": "Rapper and Singer",
    "country": "Trinidad and Tobago"
  },
  {
    "name": "Neymar Jr.",
    "follower_count": "220",
    "description": "Professional Footballer",
    "country": "Brazil"
  },
  {
    "name": "Katy Perry",
    "follower_count": "205",
    "description": "Singer and Songwriter",
    "country": "United States"
  },
  {
    "name": "Miley Cyrus",
    "follower_count": "215",
    "description": "Singer and Actress",
    "country": "United States"
  }

]


keep_playing = True

# function that handles comparisons
def compare(user_input):  
   
   if user_input == "a" and  data[random_generated_number[0]]["follower_count"] > data[random_generated_number[1]]["follower_count"]:
    print("you win \n")
    return True
   
   elif user_input == "b" and data[random_generated_number[1]]["follower_count"] > data[random_generated_number[0]]["follower_count"]:
     print("you win \n")
     return True  
   
   else:
     print("you loose")
     return False
    



while keep_playing: 
  random_generated_number = random.sample(range(0, len(data)),2)
  user_input = input(f"who has more followers \nenter a  for {data[random_generated_number[0]]["name"]}. enter b for {data[random_generated_number[1]]["name"]} " )
  if not compare(user_input):
    keep_playing = False 


