function addItem() {
    input = document.getElementById("input_to_do");
    text = document.createTextNode(input.value);
    li = document.createElement("li");
    li.appendChild(text);
    
    if (input.value == "") alert("Error, input is empty");
    else document.getElementById("myUL").appendChild(li);
    input.value = "";

    
    var span = document.createElement("span");
    var txt = document.createTextNode("\u00D7");
    span.appendChild(txt);
    span.className = "close";
    li.appendChild(span);


    span.onclick = function() {
        this.parentElement.style.display = "none";
    }
    li.onclick = function() {
        this.classList.toggle('checked');
    }
}