var fs = require('fs')
var back = require('./back.js')
var front = require('./front.js')

var inFile = '../../drafts/cards_data.json'
var outDir = './build'

if (!fs.existsSync(outDir)){
    fs.mkdirSync(outDir);
}

var cardData = JSON.parse(fs.readFileSync(inFile))

for (var index in cardData) {
  if (index == 1) {
    if (cardData.hasOwnProperty(index)) {
    card = cardData[index]

    cardName = card.symbol.replace('\+', 'plus')
    .replace('/', 'slash')
      backFName = outDir + '/' + cardName + "_back.svg"
      frontFName = outDir + '/' + cardName + "_front.svg"

      frontData = front.gen(card.symbol, card.front)
      fs.writeFile(frontFName, frontData, function(err) {
        if (err) return console.log(err);
      })

      backData = back.gen(card.symbol, card.back)
      fs.writeFile(backFName, backData, function(err) {
        if (err) return console.log(err);
      })
    }
  }
}