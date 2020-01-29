let units = [];
const BACKEND_URL = "http://192.168.1.15:5000/api/new_team";

$('div.unit').click(function () {
    let u = this;
    if (units.includes(u.id)) {
        $(u).removeClass("bw");
        const index = units.indexOf(u.id);
        if (index > -1){
           units.splice(index,1);
        }
        sendUnits()
    } else {
        if (units.length + 1 < 10) {
            units.push(u.id);
            $(u).addClass("bw");
            sendUnits();
        } else {
            alert("You already have 9 units comp");
        }
    }
})


function sendUnits(){
    let toSend = JSON.stringify({units})
    $.ajax({
        url: BACKEND_URL,
        type: "POST",
        dataType: "json",
        contentType: "application/json",
        data: toSend,
        success: function (result) {
            displayTeam(result);
        },
        error: function (error) {
            console.log(`Error ${error}`)
        }
    })
}

function displayTeam(teamcomp){
    let yourTeamDiv = $('div.your-team');
    yourTeamDiv.empty();
    Object.keys(teamcomp).forEach(function (key){
        yourTeamDiv.append($("<div></div>").addClass(`c${key} elemento m-1`));
        currentClassDiv = $('.c'+key);
        currentClassDiv.append($(`<p class="classnumber"></p>`).text(`${teamcomp[key]["units"].length}`));
        currentClassDiv.append($(`<div class="classicon rounded-circle bg-secondary" data-container="body" data-toggle="popover" data-trigger="hover" data-placement="top" data-content=${key}><img class="classiconinside" src="https://rerollcdn.com/icons/${key}.png"/></div>`));
        $('[data-toggle="popover"]').popover();
    })

}

$(document).ready(function(){
    $('[data-toggle="popover"]').popover();
});