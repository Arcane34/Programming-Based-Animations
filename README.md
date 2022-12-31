# Programming-Based-Animations
A compilation of programming based animations that I have made in my spare time while playing around with particle movement and math.

## General Particle
This is a coding foundation for almost all of my particle based animation programs, essentially being a blueprint code that I start off with.

It defines a basic particle class that can hold position, colour, size, velocity and acceleration of a particle and render it on a canvas.
The current particle generation code in the program creates white particles at the center of the window with a random velocity, running at 60 frames per second.

![](https://github.com/Arcane34/Programming-Based-Animations/blob/main/GeneralParticlePreview.gif)


## Lapping Water
This is an animation I made for a project on procedural generation. The aim was to procedurally generate islands and land, and although the animation for waves was simple to recreate for a straight edge, corners proved difficult due to the nature of how I programmed my code, requiring the waves to be in the right phase for it to make sense. Hence I made a separate animation for corners.

This consisted of creating an array of pixels that represented a wave function. Then translating the points respectively to create the illusion of water motion back and forth, done simply by translating the function. 
However this only succeeded in creating a wave function line, so the next step was to create a division, making one side blue and the other a chroma key-able colour (e.g. black or green); this was done by drawing a rectangle with a width of 1 pixel but a length long enough to leave the window, these are then attached to the coordinates of the wave function such that it looks like it is water on one side and land on the other.
And that's how the animation is created:

![](https://github.com/Arcane34/Programming-Based-Animations/blob/main/LappingWaterPreview.gif)
