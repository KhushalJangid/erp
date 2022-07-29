function manageCheck(evt){
    let target = evt.target;
    let buttonType = "";
    let otherButtons = [];
    let presentBtn, absentBtn;

    //Selecting the parent cell:
    for(let i = 0; i < 10; i++){
        if(target.tagName == "BUTTON"){
            if(target.classList.contains("present-btn")){
                buttonType = "present";
            }else if(target.classList.contains("absent-btn")){
                buttonType = "absent";
            }
        }
        if(target.tagName == "BODY"){
            break;
        }
        if(target.tagName == "TD"){
            break;
        }
        target = target.parentElement;
    }
    
    //Selecting the buttons in the parent cell:
    if(target.tagName == "TD"){
        for(i = 0; i < target.childNodes.length; i++){
            if(target.childNodes[i].tagName == "BUTTON"){
                otherButtons.push(target.childNodes[i]);
                if(target.childNodes[i].classList.contains("present-btn")){
                    presentBtn = target.childNodes[i];
                }
                if(target.childNodes[i].classList.contains("absent-btn")){
                    absentBtn = target.childNodes[i];
                }
            }
        }
    }else{
        return;
    }

    //If present was clicked:
    if(buttonType == "present"){
        if(presentBtn.classList.contains("checked")){
            presentBtn.classList.remove("checked");
        }else{
            presentBtn.classList.add("checked");
            absentBtn.classList.remove("checked");
        }
    }

    //If absent was clicked:
    if(buttonType == "absent"){
        if(absentBtn.classList.contains("checked")){
            absentBtn.classList.remove("checked");
        }else{
            absentBtn.classList.add("checked");
            presentBtn.classList.remove("checked");
        }
    }

}


// Apply click event listeners to all attendance marker buttons:

function addEventsToAllButtons(){
    let allBtns = document.querySelectorAll("#edit-class-attendance button.attendance-marker");
    for(let i = 0; i < allBtns.length; i++){
        allBtns[i].addEventListener("click", function(){
            manageCheck(event);
        });
    }
}
addEventsToAllButtons();