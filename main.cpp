#include <iostream>
#include <stdlib.h>

//  Monty Hall Simulation.
//  Two doors have goats behind them, one door has a car. First we pick a door. Then a door is opened.
//  Is it better for us to switch our choice or to stick to our original choice?
//  AUTHOR: Philip de Castro, 2017

using namespace std;

float car_door() {
    float door1; float door2; float door3;
    door1 = rand() % 3;
    door2 = rand() % 3;
    door3 = rand() % 3;
    //
    if (door2 == door1 || door2 == door3){
        while (door2 == door1 || door2 == door3){
            door2 = rand() % 3;
        }
    }
    else if (door3 == door1 || door3 == door2){
        while (door3 == door1 || door3 == door2){
            door3 = rand() % 3;
        }
    }
    //
    if (door1 == 0){
        return door1;
    }
    else if (door2 == 0){
        return door2;
    }
    else{
        return door3;
    }
}
//
int main() {
    float correct_choices;
    correct_choices = 0.0;
    float incorrect_choices;
    incorrect_choices = 0.0;
    float trials;
    trials = 0.0;
    for (; trials <= 10000000; trials++){
        float first_choice; float second_choice;
        float revealed_door; float correct_door;
        float cardoor;
        cardoor = car_door();
        //
        first_choice = rand() % 3;
        revealed_door = rand() % 3;
        correct_door = car_door();
        if (revealed_door == first_choice || revealed_door == cardoor){
            while (revealed_door == first_choice || revealed_door == cardoor){
                revealed_door = rand() % 3;
            }
        }
        //
        second_choice = rand() % 3;
        if (second_choice == first_choice || second_choice == revealed_door){
            while (second_choice == first_choice || second_choice == revealed_door){
                second_choice = rand() % 3;
            }
        }
        //
        if (second_choice == correct_door){
            correct_choices++;
        }
        else{
            incorrect_choices++;
        }
    }
    float probability_correct; float probability_incorrect;
    probability_correct = correct_choices/trials;
    probability_incorrect = incorrect_choices/trials;
    cout << "Probability of getting second choice correct: " << probability_correct << "\n" << endl;
    cout << "Probability of getting second choice incorrect: " << probability_incorrect << endl;
    return 0;
}