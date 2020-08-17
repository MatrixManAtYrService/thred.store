const D3Node = require('d3-node')
const d3 = require('d3')

const styles = `
    .good-rect {
      stroke: #326e3a;
    }
`
function gen(symbol, data) {
    console.log("generating front for", symbol)
    return "foo"
}

module.exports = {"gen": gen}