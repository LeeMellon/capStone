

$("html").on("dragover", function(event) {
    event.preventDefault();
    event.stopPropagation();
    $(this).addClass('dragging');
});

$("html").on("dragleave", function(event) {
    event.preventDefault();
    event.stopPropagation();
    $(this).removeClass('dragging');
});

$("html").on("drop", function(event) {
    event.preventDefault();
    event.stopPropagation();

});



$(document).ready(function() {


     $('#binder').on("dragover drop", function (e) {
        e.preventDefault();
    }).on("drop", function (e) {
        $("#hidden_binder")
            .prop("files", e.originalEvent.dataTransfer.files)
            .closest("form")
    });

    $('#stgd').on("dragover drop", function (e) {
        e.preventDefault();
    }).on("drop", function (e) {
        $("#hidden_stgd")
            .prop("files", e.originalEvent.dataTransfer.files)
            .closest("form")

    });

    $('#splash').on("dragover drop", function (e) {
        e.preventDefault();
    }).on("drop", function (e) {
        $("#hidden_splash")
            .prop("files", e.originalEvent.dataTransfer.files)
            .closest("form")
    });

    $('#bulk').on("dragover drop", function (e) {
        e.preventDefault();
    }).on("drop", function (e) {
        $("#hidden_bulk")
            .prop("files", e.originalEvent.dataTransfer.files)
            .closest("form")
    });

});

