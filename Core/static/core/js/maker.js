//
//
// $("html").on("dragover", function(event) {
//     event.preventDefault();
//     event.stopPropagation();
//     $(this).addClass('dragging');
// });
//
// $("html").on("dragleave", function(event) {
//     event.preventDefault();
//     event.stopPropagation();
//     $(this).removeClass('dragging');
// });
//
// $("html").on("drop", function(event) {
//     event.preventDefault();
//     event.stopPropagation();
//
// });


$(document).ready(function () {         //loading js //

//binder div in maker.html. Keeps it from opening pdf on drop
    $('#binder').on("dragover drop", function (e) {
        e.preventDefault();
    }).on("drop", function (e) {        //sends to hidden div
        $("#hidden_binder")
            .prop("files", e.originalEvent.dataTransfer.files)
            .closest("form")
    });
//study guide div
    $('#stgd').on("dragover drop", function (e) {
        e.preventDefault();
    }).on("drop", function (e) {
        $("#hidden_stgd")
            .prop("files", e.originalEvent.dataTransfer.files)
            .closest("form")

    });
//binder image div
    $('#binder_img').on("dragover drop", function (e) {
        e.preventDefault();
    }).on("drop", function (e) {
        $("#hidden_binder_img")
            .prop("files", e.originalEvent.dataTransfer.files)
            .closest("form")
    });
//study guide image div
    $('#stgd_img').on("dragover drop", function (e) {
        e.preventDefault();
    }).on("drop", function (e) {
        $("#hidden_stgd_img")
            .prop("files", e.originalEvent.dataTransfer.files)
            .closest("form")
    });

//splash image div
    $('#splash').on("dragover drop", function (e) {
        e.preventDefault();
    }).on("drop", function (e) {
        $("#hidden_splash")
            .prop("files", e.originalEvent.dataTransfer.files)
            .closest("form")
    });
//bulk files div
    $('#bulk').on("dragover drop", function (e) {
        e.preventDefault();
    }).on("drop", function (e) {
        $("#hidden_bulk")
            .prop("files", e.originalEvent.dataTransfer.files)
            .closest("form")
    });

    });

