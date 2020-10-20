const guildId = "767997083739095070";
const memberLimit = 47;

document.addEventListener('DOMContentLoaded', async function (event) {
    const xhReq = new XMLHttpRequest();
    xhReq.open('GET', `https://discordapp.com/api/guilds/${guildId}/widget.json`, true);
    xhReq.send(null);
    xhReq.onload = (r, p) => {
        const discordjson = JSON.parse(xhReq.responseText);
        if (discordjson != null) {
            const memberList = document.getElementById('members-list');
            discordjson.members.slice(0, memberLimit).forEach(function (member) {
                const avatar = member.avatar_url.replace('.jpg', '.png');
                memberList.innerHTML += `<div style="position: relative">
                <div class="discord-profile-pic" style="background-image: url(${avatar});"
                    title="${member.username}#${member.discriminator}">
                </div>
                <div class="discord-status discord-status-${member.status}">
                </div>
                </div>`;
            })

            if (discordjson.members.length > memberLimit) {
                let toShow = discordjson.members.length - memberLimit;
                if (toShow > 99) {
                    toShow = 99;
                }
                memberList.innerHTML += `<div style="position: relative">
                <div class="discord-more">
                    <span>+${toShow}</span>
                </div>
                </div>`;
            }
        }

        const link = document.getElementById('discord-invite');
        if (link) {
            link.href = discordjson.instant_invite;
        }
    }
})



$('#search-input').on('keyup', function() {
    var value = $(this)
        .val()
        .toLowerCase();
    $('.tab-content .card').filter(function() {
        $(this).toggle(
            $(this)
                .text()
                .toLowerCase()
                .indexOf(value) > -1
        );
    });
    if ($('.tab-content .card').length === 0) {
        $('#notfound').show();
    } else {
        $('#notfound').hide();
    }
});

// Filter by buttons
// Activate current nav commands button
$('.cmd-btn-list').click(function() {
    $('.cmd-btn-list').each(function() {
        $(this).removeClass('cmd-btn-list-focus');
    });
    $(this).addClass('cmd-btn-list-focus');

    var id = $(this).attr('id');
    console.log(id);
    $('.tab-content .card').filter(function() {
        $(this).toggle(
            $(this)
                .attr('class')
                .indexOf(id) > -1
        );
    });
});


