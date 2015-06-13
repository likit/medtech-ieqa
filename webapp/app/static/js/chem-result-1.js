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
    $('#form input, select').each(function(idx) {
        $(this).on('focus', function() {
            $(this).parents("tr").addClass('info');
        });
        $(this).on('blur', function() {
            $(this).parents("tr").removeClass('info');
        });
    });
});
