<h1 align="center">Pig (dice game)</h1>

<p align="left">
  Test Driven Development
</p>


- [📝 Table of Contents](#-table-of-contents)
- [🧐 About ](#-about-)
- [👨‍💻 Description ](#-description-)
- [🏁 Getting Started ](#-getting-started-)
- [Usage](#usage)
- [⛏️ Built Using ](#️-built-using-)
- [✍️ Authors ](#️-authors-)

## 🧐 About <a name = "about"></a>
<h3> PIG DICE GAME</h3>
<h5> Pig is a simple dice game first described in print by John Scarne in 1945. Players take turns to roll a single dice as many times as they wish, adding all roll results to a running total, but losing their gained score for the turn if they roll a 1.</h5>
<h3>Rules to play the pig dice game</h3>
<h4>
Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to "hold":
If the player rolls a 1, they score nothing and it becomes the next player's turn.
If the player rolls any other number, it is added to their turn total and the player's turn continues.
If a player chooses to "hold", their turn total is added to their score, and it becomes the next player's turn.
The first player to score 100 or more points wins.
</h4> <br>
👨‍💻 Description <a name = "description"></a>
<h4>
Our dicegame project is created using Object Oriented Programming principles. <br>
<h3>Progamming Language Used: Python.</h3> <br>
There are 7 class totally used in project <br>
<b>Dice class: </b> <br>
Defines the dice faces which is 6; randomly rolls between die faces 1 to 6 <br>
<b>Player class: </b> To keep track of player name and their score(Total score) <br>
<b>Dicehand class: </b> <br>
Each round in the game player decides to roll/ hold
If player rolls gamechanger (dice face 1), directly set player turn score to 0 and end their turn.
If player rolls between 2 to 6, the die face rolled will be set as their turn score,
next throw is accumulated to turn total until  he volunteer to hold or he rolls 1.
If player wants to hold then their overall turn score must be added to their total score and turn is ended for current player <br>
<b>Game class: </b> <br>
This is an interesting class, where two dicehand play against each other.
We are keeping track of which player's turn is ongoing, when player holds or rolls 1 we swap their turn's here.
Also here when one player's turn gets over we have functions to start next players turn
We also have cheat code in this class, player cheats and wins the game.
Player name change functionality while game is ongoing has also been added. <br>
<b>Intelligence Class</b> <br>
This Intelligence class inherits from another class called Dicehand. The Intelligence class represents the computer player in a game of pig. The play method randomly chooses whether the computer player should roll the dice or hold, and the "computer_play" method simulates the computer player's turn.
Particularly we are giving more weightage to hold and play wisely the greedy pig game
so that our computer chooses to hold if they have attained some highest turn total instead of rolling 1 and loosing all turn scores.<br>
<b>Usergame Class</b> <br>
UserGame class represents the user interface for playing a game Pig Dice.
We have added player VS computer functionality, which starts a game of Pig Dice with one human player and one computer player. The human player and the computer player each have their own dicehand, which represents their current hand of dice. The game continues until either player reaches the target score of 100 points.
We also added player VS player functionality, which starts a game of Pig Dice with two human players.Each player has their own Dicehand, and the game continues until one of the players reaches the target score of 100 points.<br>
<b>Main Class</b> <br>
In this class we are running our pig dice game.
</h4>
<h3> As we also included Test suites for each modules which we used for development.
</h3>
<h2>White box testing - "Test the code knowing exactly how it look like" Unit testing is white box testing. </h2>
<h3> For testing purpose we used unit testing in python </h3>
<h2> Strategy</h2>
<h4> Test driven development 🧐
We planned how many classes we will be having for game, then planned for what functionality
each class should have. Side by side we have planned for the test cases and implemented the testcases to check whether functions works as indented, then we added more code to make the testcases pass.
</h4>

## 🏁 Getting Started <a name = "getting_started">
<h1> Lets Play PIG DICE GAME
<img src = "src\dice.gif" width = "80px" height = "70px">
</a>

### Installing Game
*Here you can add a description on how to install the project*

### Usage

*Here you can add a description on how to run and use the project*

## ⛏️ Built Using <a name = "built_using"></a>

<h2>Installing Dependency </h2>
*These are essential tools to install before even downloading the game*

### Check version of Python
Check what version of Python you have. The Makefile uses `PYTHON=python` as default.

<h1>Check make installation<h1>
<h5>If you have another naming of the Python executable then you can solve that using an environment variable. This is common on Mac and Linux.
Chocolatey is the package manager/ installer which is used to install make(Note: Run Powershell as administrator)Then use the command:
<h3>choco install make </h3> so that make is installed in computer.
To check whether we installed make succesfully and also which version of make we have </h5>
<h3>make version </h3>
<h1>Python virtual environment<h1>
<h5>Install a Python virtual environment and activate it.</h5>
<h1>Activate on Windows</h1>
<h3 align= "center">. .venv/Scripts/activate</h3>
<h1>Activate on Linx/Mac</h1>
<h3 align = "center">. .venv/bin/activate</h3>
<p>When you are done you can leave the venv using the command `deactivate`.<p>
<h1>Install the dependencies</h1>

<p>
Install the PIP packages that are dependencies to the project and/or the development environment. The dependencies are documented in the `requirements.txt` and pyproject.toml

Do not forget to check that you have an active venv.
</p>
<h3 align = "center"> <b>make install-requirements</b> </h3>
<h3 align = "center"> <b>make install-toml</b> </h3>
<h1>Check what is installed</h1>
<h3 align = "center"> <b> make build-toml</b> </h3>
<h1>Execute the main program</h1>
<h3 align = "center"> <b> make run</b> </h3>
<h1>Run the validators</h1>
<p>You can run the static code validators like this. They check the sourcecode and exclude the testcode.<p>

# Run each at a time
<h3 align = "center"> <b> make flake8</b> </h3>
<h3 align = "center"> <b> make pylint</b> </h3>

<h1>Run the unittests with coverage</h1>
<h3 align = "center"> <b> make coverage</b> </h3>

<h1>Run the unittests</h1>
<h3 align = "center"> <b> make test </b> </h3>


<h1>Remove generated files</h1>
<h2>You can remove all generated files by this.</h2>
# Remove files generated for tests or caching
<h3 align = "center"> <b> make clean </b> </h3>
# Do also remove all you have installed
<h3 align = "center" > <b> make clean-all </b> </h3>

<h1>Codestyle with black</h1>
You can unify the codestyle using black. Running black will change your source code to have a codestyle according to black codestyle.
<h3 align = "center"> <b> make black </b> </h3>


## ✍️ Authors <a name = "authors"></a>

*Here you can add a list of authors/people who worked and maintain the project*

- [@abshir](https://github.com/abshir112) - Idea & Initial work
- [@Lakshmi](https://github.com/lakshmivishal9496 ) - Idea & Initial work
