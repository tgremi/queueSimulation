const getRandomInt = require("./helpers")
module.exports = class Processador {

    constructor(pacotes, timeProcess) {
        this.pacotes = pacotes
        this.timeProcess = timeProcess
        this.time = ''
    }


    process() {
        console.log('No process ----', this.pacotes.lista.length)
        console.log('No process ----', this.timeProcess)
        let i = 0;
        while (this.pacotes.lista.length > i) {
            //setTimeout(() => {
            console.log(i)
            console.log(this.pacotes.lista)
            console.log("processando pacote - ", this.pacotes.lista[i])
            this.pacotes.Pop();
            //}, this.timeProcess);
            i++;
        }
        return;
    }

    getTime() {

    }

    setTime() {

    }

    setEvent() {

    }
}