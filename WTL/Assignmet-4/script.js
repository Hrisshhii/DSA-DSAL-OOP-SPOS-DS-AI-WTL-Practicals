let display = document.getElementById("result");

// Add numbers/operators
function append(value){
    display.value += value;
}

// Clear screen
function clearDisplay(){
    display.value = "";
}

// Calculate result with validation
function calculate(){

    if(display.value === ""){
        alert("Please enter a value first!");
        return;
    }

    try{
        display.value = eval(display.value);
    }
    catch{
        alert("Invalid Expression!");
        display.value="";
    }
}

// Square function
function square(){

    if(display.value === "" || isNaN(display.value)){
        alert("Enter a valid number to square!");
        return;
    }

    let num = Number(display.value);
    display.value = num * num;
}

function backspace(){
    result.value = result.value.slice(0,-1);
}
