# Daily reflection
- Did we follow the basic principles? 
I tried to! 

- Did we search for the true root cause? 
Not really applicable here

- Did we leave code cleaner than we find it? 
I started with an empty file but I tried to write it as clean as possible 


# What I still wanted to do:
- During every guess a new updated word is created instead of modifying the guessed characters. This feels a bit redundant and it resulted in a nested if-statement, but I could at this moment not think of a way to improve it. 
- I wanted to create a mocker to get the random word from the database, but I didn't succeed (see line 33). Now I overwrite the random word but this is not very neat. 
- The testing for playing the actual game didn't work as I wanted. I tried to mock the letters in the word in `test_win_game`, but I didn't know how to do this in a while loop. When I played the came using the command prompt, it worked as expected. To still test if the game successfully ends I wrote another method `check_if_won`, which passed the test `test_win_game_alternative`. 
- I also forgot to make my methods and properties protected with the underscore. 
- 
