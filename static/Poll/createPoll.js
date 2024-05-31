// for createPoll page
const addOptionBtn = document.getElementById("addOption");
const deleteOptionBtn = document.getElementById("deleteOption");
const optionsDiv = document.getElementById("options");
const optionsCountInput = document.getElementById("optionsCount");
var optionCounter = 2;
optionsCountInput.value = optionCounter;

addOptionBtn.addEventListener("click", () => {
    // Create a new input element
    const newInput = document.createElement("input");
    newInput.id = `answerOptions${optionCounter + 1}`; // Increment the ID for each new option
    newInput.type = "text";
    newInput.className = "form-control mb-3";
    newInput.placeholder = `Option ${optionCounter + 1}`;
    newInput.required = true;
    // Append the new input element to the optionsDiv
    optionsDiv.appendChild(newInput);
    // Increment the optionCounter
    optionCounter++;
    optionsCountInput.value = optionCounter;

    if (optionCounter > 2) {
        deleteOptionBtn.hidden = false;
    } else {
        deleteOptionBtn.hidden = true;
    }
});

deleteOptionBtn.addEventListener("click", () =>{
    const lastInput = document.getElementById(`answerOptions${optionCounter}`);
    if (optionCounter > 2) {
        lastInput.remove();
        optionCounter--;
        optionsCountInput.value = optionCounter;
    }
    if (optionCounter === 2) {
        deleteOptionBtn.hidden = true;
    }
     
});