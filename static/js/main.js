
$(document).ready(function () {
    getEmployeeData();
});

function getEmployeeData() {
    $.ajax({
        type: 'GET',
        url: '/data',
        dataType: 'json',
        success: function(data) {
            displayEmployeeData(data);
            initializeTooltipData();
        }
    });
}

function displayEmployeeData(data) {
    const $tableBody = $("#dataTable tbody");
    $tableBody.empty();

    $.each(data, function(index, employee) {
        $tableBody.append(`
            <tr>
                <td><span class="tooltip_trigger" data-firstname="${employee.firstname}" data-lastname="${employee.lastname}" data-id="${employee.file_id}" data-filename="${employee.filename}" data-description="${employee.description}" data-email="${employee.email}" data-phone="${employee.phone}">${employee.firstname}</span></td>
                <td><span class="tooltip_trigger" data-firstname="${employee.firstname}" data-lastname="${employee.lastname}" data-id="${employee.file_id}" data-filename="${employee.filename}" data-description="${employee.description}" data-email="${employee.email}" data-phone="${employee.phone}">${employee.lastname}</span></td>
                <td><span>${employee.departmentName}</span></td>
                <td><span>${employee.companyName}</span></td>
            </tr>
        `);
    });
}

function getFileBaseName(fileName) {
    if (!fileName) return "";
    return fileName.substring(0, fileName.lastIndexOf("."));
}

function initializeTooltipData() {

    const $tableBody = $("#dataTable tbody");
    let $spanElem = $tableBody
                .children("tr")
                .find("td")
                .find("span");

    $spanElem.each(function () {
        const $span = $(this);
        let firstname = $span.data("firstname");
        let lastname = $span.data("lastname");
        if (firstname || lastname) {
            let email = $span.data("email");
            let phone = $span.data("phone");
            let fileName = $span.data("filename");
            let description = $span.data("description");
            let file_id = $span.data("id");
            let info_head = "<span class='menu-head'>" + firstname + " " + lastname + "</span>";
            let info_foot = "<span class='menu-head'>" + "Title: " + "</span>"
                            + "<span class='menu-body'>" + getFileBaseName(fileName) + "</span>"
                            + "<br>"
                            + "<span class='menu-head'>" +  "Description: " + "</span>"
                            + "<span class='menu-body'>" + description + "</span>";
            let info_menu = "<span class='menu-head'>" + "Email: " + "</span>"
                            + "<span class='menu-body'>" + email + "</span>"
                            + "<br>"
                            + "<span class='menu-head'>" + "Phone: " + "</span>"
                            + "<span class='menu-body'>" + phone + "</span>";
            $span.tooltipData({
                id: file_id,
                title: $span.text(),
                contentClass: "content-tooltip",
                containerClass: "tooltip-container",
                tooltipImgClass: "tooltip_img",
                headerClass: "header",
                menuClass: "menu",
                contentClass: "content",
                footerClass: "footer",
                image: "",
                info_head: info_head,
                info_foot: info_foot,
                info_menu: info_menu,
                imageurl: "/imagedata",
                position: { my: "left+10 center", at: "right center" },
                show: {
                    effect: "fadeIn",      // Use fade-in effect
                    duration: 400        // Duration of fade-in animation
                },
                hide: {
                    effect: "fadeOut",   // Use fade-out effect
                    duration: 400        // Duration of fade-out animation
                },
                track: true,            // Tooltip follows the mouse
                classes: {
                    "ui-tooltip": "highlight"
                },
            });
        }
    });
}