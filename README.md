# techin509b-tictactoe
Starter code for the Tic Tac Toe assignments

# Board Game Test Suite
This repository contains a suite of unit tests for a board game application, designed to ensure the integrity and functionality of the game's logic.

# Getting Started
These instructions will guide you through running the test suite on your local machine.

# Prerequisites
Before running the tests, ensure you have Python installed on your system. The tests are written using Python's built-in ‘unittest’ framework.

# Installing
Clone the repository to your local machine:

bash
git clone https://github.com/[your-username]/[your-repo-name].git
cd [your-repo-name]

# Running the Tests
To run the tests, execute the following command in the terminal:

bash
python -m unittest tests.py

This command will discover and run all the tests defined in the tests.py file. If you have multiple test files and want to run all tests in the directory, use:

bash
python -m unittest discover

# Test Breakdown
The test suite includes the following components:

TestBoard
Tests related to the game board's functionality.

TestPlayer: 
Tests for player actions and attributes.

TestBot: 
Tests specific to the bot's behavior in the game.

TestGame: 
Overall game logic and flow tests.

