# Clock Angle Visualization

##### Watch the process on YouTube: https://youtu.be/G9NHYXDCt7M

## Overview

    This mini-project visualizes the angle between the hour and minute hands on a clock. 
    The inspiration for this project comes from a classic interview problem that involves calculating the smallest angle between the hour and minute hands at any given time. 
    I found the problem intriguing and decided to create this visualization to dynamically demonstrate the correctness of the algorithm.

## Project Motivation

    The project is based on a common interview question that tests one's understanding of clock arithmetic and angle calculations. During an interview, 
    I was asked to compute the smallest angle between the hour and minute hands of a clock, considering that the hour hand moves dynamically as the minutes pass. 
    This challenge sparked my interest, and I decided to delve deeper by building a mini-project to visualize the solution.

## How It Works

    Hour Hand Movement: The hour hand moves 30 degrees per hour and 0.5 degrees per minute.
    Minute Hand Movement: The minute hand moves 6 degrees per minute.
    Angle Calculation: The algorithm calculates the absolute difference between the angles of the hour and minute hands, ensuring that the angle is the smallest possible (i.e., less than or equal to 180 degrees).

## Features

    Dynamic Visualization: The project dynamically displays the clock with the hour and minute hands positioned according to the input time.
    Accurate Angle Calculation: The angle between the hands is calculated considering the minute-by-minute movement of the hour hand.
    Interactive Interface: Users can input different times to see how the angle changes.
