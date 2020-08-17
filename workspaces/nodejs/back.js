const D3Node = require('d3-node')
const d3 = require('d3')

// poker card dimensions in inches
const inches = {
        width: 3.5,
        height: 2.5
    },
    dpi = 95,
    dots = {
        width: inches.width * dpi,
        height: inches.height * dpi
    }

// ratio of cell size to pad size
const padRatio = {
        vertical: 1,
        horizontal: 1
    },
    numCells = {
        horizontal: 14 + 2 * padRatio.horizontal,
        vertical: 10 + 2 * padRatio.horizontal
    },
    cellDimensions = {
        width: dots.width / numCells.horizontal,
        height: dots.height / numCells.vertical
    }

const pad = {
    horizontal: padRatio.horizontal * cellDimensions.width,
    vertical: padRatio.vertical * cellDimensions.height
}

const styles = `

    .cellParent {
        width: ${cellDimensions.width * 2}px;
        height: ${cellDimensions.height}px;
    }
    .cell{
        width: ${cellDimensions.width}px;
        height: ${cellDimensions.height + 1}px;
    }

    .leftCell {
      fill: #cba6e3;
    }

    .rightCell {
      fill: #61c5e6;
      transform: translate(${cellDimensions.width}px, 0px);
    }

    .highlighted {
        stroke: red;
    }


    .columnBoundary {
      stroke: black;
      stroke-width: 2px;
    }

    .gridBoundary {
      stroke: black;
      stroke-width: 2px;
      fill: white;
    }

    .cardBoundary {
      stroke-width: 0px;
      fill: white;
    }

    .highlighted {
      stroke: #c2da4e;
      stroke-width: 2px;
      fill-opacity: 0;
    }

    .elementText {
      font: 12px Code New Roman;
    }

    .borderHeaderText {
      font: 10px Archivo Narrow;
      font-weight: bold;
    }

    .borderText {
      font: 10px Archivo Narrow;
      font-weight: bold;
    }
`

function gen(symbol, data) {

    console.log("generating back for", symbol)

    // derive card features
    var cells = [],
        gridBoundary = {
            minX: 999,
            maxX: 0,
            minY: 999,
            maxY: 0
        },
        uniqueXs = new Set()

    for (var i = 1; i <= data.length; i += 1) {
        var x, y
        if (i < 11) {
            y = i
            x = 1
        } else if (i >= 11 && i < 21) {
            y = i - 10
            x = 2
        } else if (i >= 21 && i < 25) {
            y = i - 20
            x = 3
        } else if (i >= 25 && i < 29) {
            y = i - 18
            x = 3
        } else if (i >= 29 && i < 33) {
            y = i - 28
            x = 4
        } else if (i >= 33 && i < 37) {
            y = i - 26
            x = 4
        } else if (i >= 37 && i < 41) {
            y = i - 36
            x = 5
        } else if (i >= 41 && i < 45) {
            y = i - 34
            x = 5
        } else if (i >= 45 && i < 55) {
            y = i - 44
            x = 6
        } else if (i >= 54 && i < 65) {
            y = i - 54
            x = 7
        } else {
            console.log("Received an", i, "th symbol pair.  Ignoring it.")
        }

        // cell 1 is in the upper left, where x and y are 0
        // subtract one to make this line up
        xLoc = pad.horizontal + (x - 1) * 2 * cellDimensions.width,
            yLoc = pad.vertical + (y - 1) * cellDimensions.height

        if (xLoc < gridBoundary.minX) {
            gridBoundary.minX = xLoc
        }
        if (xLoc > gridBoundary.maxX) {
            gridBoundary.maxX = xLoc
        }
        if (yLoc < gridBoundary.minY) {
            gridBoundary.minY = yLoc
        }
        if (yLoc > gridBoundary.maxY) {
            gridBoundary.maxY = yLoc
        }

        datum = data[i - 1]

        var highlight = false
        if (datum.middle) {
            cells.push({
                x: pad.horizontal + 6 * cellDimensions.width,
                y: pad.vertical + 4 * cellDimensions.height,
                left: datum.middle.left,
                right: datum.middle.right
            })
            cells.push({
                x: pad.horizontal + 6 * cellDimensions.width,
                y: pad.vertical + 5 * cellDimensions.height,
                left: datum.middle.left,
                right: datum.middle.right
            })
            highlight = true
        }

        cells.push({
            x: xLoc,
            y: yLoc,
            left: datum.left,
            right: datum.right,
            highlight: highlight
        })


        uniqueXs.add(xLoc)
    }

    gridBoundary.maxX += 2 * cellDimensions.width
    gridBoundary.maxY += cellDimensions.height

    cardBoundary = {
        minX: gridBoundary.minX - pad.horizontal,
        maxX: gridBoundary.maxX + pad.horizontal,
        minY: gridBoundary.minY - pad.vertical,
        maxY: gridBoundary.maxY + pad.vertical,
        center: {
            x: (gridBoundary.minX - gridBoundary.maxX) / 2,
            y: (gridBoundary.minY - gridBoundary.maxY) / 2
        }
    }

    middle = {
        minX: pad.horizontal + 4 * cellDimensions.width,
        minY: pad.vertical + 4 * cellDimensions.height,
        maxX: pad.horizontal + 10 * cellDimensions.width,
        maxY: pad.vertical + 6 * cellDimensions.height
    }

    columnBoundaries = []
    xs = Array.from(uniqueXs)
    xs.forEach(function (x) {
        if (x < middle.minX || x > middle.maxX) {
            // left and right columns run the full height of the card
            columnBoundaries.push({
                x1: x,
                y1: gridBoundary.minY,
                x2: x,
                y2: gridBoundary.maxY
            })
        } else if (x >= middle.minX && x <= middle.maxX) {
            // middle columns have a gap in the middle
            columnBoundaries.push({
                x1: x,
                y1: gridBoundary.minY,
                x2: x,
                y2: middle.minY
            })
            columnBoundaries.push({
                x1: x,
                y1: middle.maxY,
                x2: x,
                y2: gridBoundary.maxY
            })
        }
    })

    // middle section left boundary
    columnBoundaries.push({
        x1: pad.horizontal + 4 * cellDimensions.width,
        y1: pad.vertical + 4 * cellDimensions.height,
        x2: pad.horizontal + 4 * cellDimensions.width,
        y2: pad.vertical + 6 * cellDimensions.height
    })

    // middle section right boundary
    columnBoundaries.push({
        x1: pad.horizontal + 10 * cellDimensions.width,
        y1: pad.vertical + 4 * cellDimensions.height,
        x2: pad.horizontal + 10 * cellDimensions.width,
        y2: pad.vertical + 6 * cellDimensions.height
    })

    cells.p


    var options = {
        styles: styles,
        d3Module: d3
    }

    var d3n = D3Node(options)
    var svg = d3n.createSVG()
    svg.append("rect")
        .attr("class", "cardBoundary")
        .attr("width", cardBoundary.maxX - cardBoundary.minX)
        .attr("height", cardBoundary.maxY - cardBoundary.minY)
        .attr("transform", "translate(" + cardBoundary.minX + "," + cardBoundary.minY + ")")


    var cells = svg.selectAll(".cell")
        .data(cells)
        .enter().append("g")
        .attr("class", "cellParent")
        .attr("transform", function (d) {
            return "translate(" + d.x + "," + d.y + ")"
        })


    cells.append("rect")
        .attr("class", "cell leftCell")

    cells.append("rect")
        .attr("class", "cell rightCell")

    cells.filter(function (d) {
            return d.highlight;
        })
        .append("rect")
        .attr("width", 10)
        .attr("height", 10)
        .attr("class", "highlighted")




    svg.append("rect")
        .attr("class", "gridBoundary")
        .attr("width", gridBoundary.maxX - gridBoundary.minX)
        .attr("height", gridBoundary.maxY - gridBoundary.minY)
        .attr("transform", "translate(" + gridBoundary.minX + "," + gridBoundary.minY + ")")
        .attr("fill-opacity", 0)


    svg.selectAll(".line")
        .data(columnBoundaries)
        .enter().append("line")
        .attr("class", "columnBoundary")
        .attr("x1", function (d) {
            return d.x1
        })
        .attr("y1", function (d) {
            return d.y1
        })
        .attr("x2", function (d) {
            return d.x2
        })
        .attr("y2", function (d) {
            return d.y2
        })

    svg.attr("width", cardBoundary.maxX - cardBoundary.minX)
    svg.attr("height", cardBoundary.maxY - cardBoundary.minY)
    return d3n.svgString()
}

module.exports = {
    "gen": gen
}