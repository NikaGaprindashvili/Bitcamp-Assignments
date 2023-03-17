# Shows the list of characters with defined quotes

quotes = {'Evelynn' : "A Man Once Told Me To Put On Some Clothes. So I Wore His Skin.",
          'Irelia' : "To Live Under A Boot, Is Not To Live.",
          'Yone' : "Wear A Mask Long Enough, And You Forget The Face Beneath.",
          'Riven' : "What Is Broken Can Be Reforged.",
          'Viego' : "In a world without love, death means nothing.",
}

# Asks the person Who is the author and prints the quote
author = input("Who is the author? ").title()
print(quotes[author])