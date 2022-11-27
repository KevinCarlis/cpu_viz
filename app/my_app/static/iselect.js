function setInsBtn() {
    const insBtn =  document.getElementById("ins0");
    insBtn.checked= true;
}
setInsBtn();

var rnel = document.getElementById("ins");
rnel.addEventListener("change", function() {
    document.querySelector("#rmdiv").style.display = "none";
    document.getElementById("rnlabel").innerHTML = "Operand1";
    if (this.value !== "MOV") {
        document.querySelector("#rmdiv").style.display = "inline-block";
        document.getElementById("rnlabel").innerHTML = "Operand2";
    }
    if (this.value === "CMP") {
        document.querySelector("#updatediv").style.display = "none";
        document.querySelector("#rddiv").style.display = "none";
    } else {
        document.querySelector("#rddiv").style.display = "inline-block";
        document.querySelector("#updatediv").style.display = "inline-block";
    }
});

var immel = document.getElementById("rn");
immel.addEventListener("change", function() {
    document.querySelector("#immdiv").style.display = "inline-block";
    document.querySelector("#immsdiv").style.display = "inline-block";
    if (this.value !== "immediate") {
        document.querySelector("#immdiv").style.display = "none";
        document.querySelector("#immsdiv").style.display = "none";
    }
});

var radios = document.forms["radios"].elements["regbutt"];
for(var i = 0, max = radios.length; i < max; i++) {
    radios[i].onclick = function() {
        if (this.value === "b") {
            var col = document.getElementsByClassName("bin")
            for(let i=0; i < col.length; i++) {
                col[i].style.display = "table-cell";
            }
            var col = document.getElementsByClassName("hex")
            for(let i=0; i < col.length; i++) {
                col[i].style.display = "none";
            }
            var col = document.getElementsByClassName("dec")
            for(let i=0; i < col.length; i++ ) {
                col[i].style.display = "none";
            }
        }
        else if (this.value === "x") {
            var col = document.getElementsByClassName("bin")
            for(let i=0; i < col.length; i++) {
                col[i].style.display = "none";
            }
            col = document.getElementsByClassName("hex")
            for(let i=0; i < col.length; i++) {
                col[i].style.display = "table-cell";
            }
            var col = document.getElementsByClassName("dec")
            for(let i=0; i < col.length; i++) {
                col[i].style.display = "none";
            }
        }
        else {
            let col = document.getElementsByClassName("bin")
            for(let i=0; i < col.length; i++) {
                col[i].style.display = "none";
            }
            col = document.getElementsByClassName("hex")
            for(let i=0; i < col.length; i++) {
                col[i].style.display = "none";
            }
            col = document.getElementsByClassName("dec")
            for(let i=0; i < col.length; i++) {
                col[i].style.display = "table-cell";
            }
        }
    }
}
