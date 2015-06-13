$(function() {
    $('#form input[type="text"]').each(function(idx) {
        $(this).change(function() {
            if($(this).val().trim()) {
                $(this).parents("tr").addClass('success');
            } else {
                $(this).parents("tr").removeClass('success');
            }
        });
    });
});
