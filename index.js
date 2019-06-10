const Queue = require("./Queue")
const Processador = require("./Processador")
const getRandomInt = require('./helpers')
const testeDeFila = () => {
    let fila1 = new Queue()
    let fila2 = new Queue()

    for (let i = 0; i < 20; i++) {
        fila1.Push(getRandomInt(0, 200))
    }
    //console.log(fila1)
    let server = new Processador(fila1, 2000)
    server.process()

}


testeDeFila()