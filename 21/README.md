# Day 21 Tool-Assisted Solve

## Simplifications

* It is always exactly 131 steps to move from the center of the grid to the center of an adjacent (N/S/E/W) grid.
  * The grid has "gutters" across the sides and middle in both horizontal and vertical directions.
  * It also has diagonal gutters between the midpoints of each edge.

## Magic Numbers

* **131**: The width and height of the grid.
* **26501365**: The number of steps the agent will take.
* **202300**: int(steps / grid width)
* **65**: steps % grid width
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

## Towards a fully-generalizable solution

If the input was less carefully crafted - i.e. we could not take gutters, symmetric tile dimensions, central starting position, etc. for granted:
* The cost to fully explore a single tile may vary (imagine a maze running from the middle to the border)
* Horizontal and vertical path distance may differ (in the extreme, it may not be possible to leave the tile in one or more directions)
* Intuitively, an overall diamond pattern of tiles (possibly with skew) would generally occur, but the edge tiles' coverage may not be as cleanly defined.

One approach I might take to handle this:
* Determine the distribution of positions reached from the initial position as a function of step count.
  * Distinguish between positions reached in the initial tile vs. its tesselations.
  * Make particular note of:
    * any positions that are adjacent to open positions in one or more adjacent tiles
    * any positions that may only be reachable by traversing another tile then returning
    * the point at which the initial tile is "fully explored"
* Determine the distribution of positions and distances reached from each open-adjacent edge position.
  * Ideally, a small number of initial edge positions "dominate" by some combination of being reached early and being connected to the rest of the positions in the tile (and presumably itself in the next tile)

With these patterns, it should be possible to calculate how many tiles are fully explored, and with some effort, a pattern of exploration along the tiles on the edge of the diamond should be discoverable to use.
