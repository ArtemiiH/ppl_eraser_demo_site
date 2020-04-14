$(function () {
    // Create the preview image
    $(".image-input-group input:file").change(function () {
        var file = this.files[0];
        var reader = new FileReader();
        reader.onload = function (e) {
            $("#uploaded-image-file-title").text(file.name);
            $("#uploaded-image-preview").attr('src', e.target.result);
            $('#processed-image-preview').attr('src', './static/svg/photo-placeholder.svg');
        }
        reader.readAsDataURL(file);
    });
});

// Attach a submit handler to the form
$("#image-submitting-form").submit(function (event) {
    // Stop form from submitting normally
    event.preventDefault();
    if ($('#image-input').get(0).files.length === 0) {
        $('#no-files-modal').modal('toggle')
        return;
    }
    $('#processed-image-preview').attr('src', './static/svg/loading.svg');

    var form = new FormData();
    form.append('image', $('#image-input').prop('files')[0]);

    // Send the data using ajax
    var request = $.ajax({
        type: 'POST',
        data: form,
        cache: false,
        processData: false,
        contentType: false,
    });
    request.done(function (data) {
        $('#processed-image-preview').attr('src', 'data:image/png;base64,' + data['image']);
    });
    request.fail(function (jqXHR, textStatus) {
        $('#no-server-modal').modal('toggle')
        $('#processed-image-preview').attr('src', './static/svg/photo-placeholder.svg');
    });
});
