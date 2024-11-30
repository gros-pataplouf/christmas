# Probably a Fire Hazard 🎄

## Kata Description

Inspired by Advent of Code and [kata-log.rocks/christmas-lights-kata](https://kata-log.rocks/christmas-lights-kata)

### Incremental Kata - No Peeping Ahead!

➡️ This is an incremental kata to simulate a real business situation: work your way through the steps in order, but do not read the next requirement before you have finished your current one.

## Background

Every year, your neighbours outshine you in the Christmas lights competition 😣 No wonder, all you have is a 50 x 25 grid of string lights. Luckily, this year a secret Santa sent you a special gift that is guaranteed to get you noticed this year by displaying festive forms and shapes. All you have to do is hang the lights and add the programs :)

## Mission

Write a program to decipher Santa's instructions (see `instructions.json`) and display a series of festive shapes on your grid by turning on/off and toggling the light bulbs.

### Requirements I

Lights in your grid are numbered from 0 to 49 horizontally and from 0 to 25 vertically. Santa's instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

#### Examples

- `turn on 0,0 through 49,24` would turn on (or leave on) every light.
- `toggle 0,0 through 49,0` would toggle the first line of 50 lights, turning off the ones that were on, and turning on the ones that were off.

### Requirements II

You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish. The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

- The phrase `turn on` actually means that you should increase the brightness of those lights by 1.
- The phrase `turn off` actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.
- The phrase `toggle` actually means that you should increase the brightness of those lights by 2.
