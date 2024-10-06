import nltk
from nltk.corpus import words
nltk.download('words')

common_usernames = [
    "shadow", "dragon", "ninja", "warrior", "legend", "ghost", 
    "phoenix", "wolf", "king", "queen", "noob", "pro", "dark", 
    "killer", "hero", "master", "gamer", "player", "wizard", 
    "sniper", "beast", "devil", "god", "knight", "viper", "joker", 
    "angel", "demon", "death", "hunter", "storm", "raven", "crash",
    "samurai", "blade", "venom", "hawk", "xXx", "xx", "xxX", "fire", "ice", "skull"
]

basic_words = set(words.words())

def check_username_rarity(username):
    rarity_score = 0
    
    if len(username) <= 4:
        rarity_score += 5
    elif len(username) <= 7:
        rarity_score += 3
    else:
        rarity_score += 1
    
    if username.lower() in basic_words:
        rarity_score -= 5
    else:
        rarity_score += 2
    
    for common_name in common_usernames:
        if common_name.lower() in username.lower():
            rarity_score -= 3
            break
    
    if rarity_score >= 8:
        rarity_class = "Very Rare"
    elif 5 <= rarity_score < 8:
        rarity_class = "Rare"
    elif 3 <= rarity_score < 5:
        rarity_class = "Uncommon"
    else:
        rarity_class = "Common"
    
    return rarity_class, rarity_score

username = input("Enter your Discord username: ")
rarity_class, score = check_username_rarity(username)
print(f"Username Rarity: {rarity_class} (Score: {score})")
