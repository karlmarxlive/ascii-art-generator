# ASCII Art Generator

A Python tool that converts regular images into ASCII art. This program transforms images pixel by pixel into text characters, creating a artistic text representation of your images.

## Features

-   Transforms images into ASCII art
    
-   Supports three brightness mapping methods: average, minmax, luminosity
    
-   Allows brightness inversion for creative effects
    
-   Accepts input via command-line arguments or through an interactive interface
    
-   Outputs ASCII art to a text file for easy sharing or printing
    

## Requirements

-   Python 3.6+
    
-   Pillow (PIL Fork) library
    

## Installation

1.  Clone this repository or download the source code
    
2.  Install the required dependencies:  

    `pip install pillow` 
    

## Usage

You can run the program in two ways:

## Command-line Mode

`python ascii-art.py [image_path] [method] [invert]` 

Parameters:

-   `image_path`: Path to the image file you want to convert
    
-   `method`: Brightness mapping method (average, minmax, or luminosity)
    
-   `invert`: Use 1 to invert brightness, 0 to keep original brightness
    

Example:

`python ascii-art.py ascii-pinapple.jpg luminosity 1` 

## Interactive Mode

Simply run the program without arguments:

`python ascii-art.py` 

The program will guide you through:

1.  Entering an image path
    
2.  Selecting a brightness mapping method
    
3.  Choosing whether to invert brightness
    

## Brightness Mapping Methods

-   **Average**: Uses the average of RGB values
    
-   **MinMax**: Uses the average of minimum and maximum RGB values
    
-   **Luminosity**: Uses weighted values (0.21R + 0.72G + 0.07B) to account for human perception
    

## Output

The program creates a text file named after your original image with "-ascii.txt" appended:

`[original_filename]-ascii.txt` 

## How It Works

The program:

1.  Loads an image using PIL
    
2.  Analyzes brightness of each pixel
    
3.  Maps each pixel to an ASCII character based on brightness
    
4.  Outputs the resulting ASCII art to a text file
    
