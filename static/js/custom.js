$(document).ready(function () {
    var $commentTrigger = $("#add_comment");
    var $commentTarget = $("#comment_form");
    $commentTrigger.click(function () {
        $commentTarget.slideToggle("fast");
        $(this).toggleClass("btn-success btn-danger");
        $(this).text(function (i, text) {
            return text === "Add Comment" ? "Cancel" : "Add Comment";
        });
    });
});