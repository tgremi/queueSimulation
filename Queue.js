module.exports = function Queue() {
    this.lista = new Array();

    this.Push = function (obj) {
        this.lista[this.lista.length] = obj;
    }

    this.Pop = function () {
        if (this.lista.length > 0) {
            let obj = this.lista[0];
            this.lista.splice(0, 1);
            console.log(obj, "<--- saporra")
            console.log(this.lista, "<--- saporra2")
            return obj;
        }
        return [];
    }

    this.Ler = function () {
        if (this.lista.length > 0) {
            return this.lista[0];
        }

    }
}