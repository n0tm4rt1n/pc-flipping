let queue = []
const express = require('express')
const app = express()
const port = 3000

app.use(express.json());
app.use(express.urlencoded({
    extended: true
}));

app.get('/', (req, res) => {
    let currentOffer = queue.pop()
    res.send('<a href=' + currentOffer.link + '>' + currentOffer.offerName + '</a><img src=' + currentOffer.img + '></img>')
})
app.post('/sendPost', (req, res) => {
    queue.push(req.body)
    res.sendStatus(200)
})

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
})
