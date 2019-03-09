grid = [list('..OO.OO..'), list('.OOOOOOO.'),
        list('.OOOOOOO.'), list('..OOOOO..'),
        list('...OOO...'), list('....O....')]

for x in range(0, len(grid)):
    val = ""
    for y in range(0, len(grid[x])):
        val = val + grid[x][y]

    print(val)
