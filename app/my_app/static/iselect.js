var rnel = document.getElementById("ins");
rnel.addEventListener("change", function() {
    document.querySelector('#rmdiv').style.display = 'none';
    document.getElementById("rnlabel").innerHTML = "Operand1";
    if (this.value !== "move") {
        document.querySelector('#rmdiv').style.display = 'inline-block';
        document.getElementById("rnlabel").innerHTML = "Operand2";
    }
});

var immel = document.getElementById("rn");
immel.addEventListener("change", function() {
    document.querySelector('#immdiv').style.display = 'inline-block';
    if (this.value !== "immediate") {
        document.querySelector('#immdiv').style.display = 'none';
    }
});
