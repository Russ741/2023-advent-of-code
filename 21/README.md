# Day 21 Tool-Assisted Solve

## Simplifications

* It is always exactly 131 steps to move from the center of the grid to the center of an adjacent (N/S/E/W) grid.
  * The grid has "gutters" across the sides and middle in both horizontal and vertical directions.
  * It also has diagonal gutters between the midpoints of each edge.

## Magic Numbers

**131**: The width and height of the grid.
**26501365**: The number of steps the agent will take.
**202300**: int(steps / grid width)
**65**: steps % grid width
  * Note that this is also the coordinate of the the center of the grid

## My Solution

1) Build a breadth-first-y search that tells me how many plots are reachable for a given number of steps.
2) Run it in a loop from 0 to, oh, let's say 2000.
3) Print the plot count for steps where step % 2 == 0 and step % 131 == 65.
4) For those series, put (step - 65) / 131 and plot count into Google Sheets.
5) Make it into a scatter plot.
6) Add a polynomial trendline of degree 2 to the plot.
    * Formula: reachable cells = 15197 * x^2 + 15303 * x + 3868
8) Put the coefficients for the trendline back into Python and solve for x = 202300 (which is (steps - 65) / 131)
