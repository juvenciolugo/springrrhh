
$(document).ready(function () {
    //alert("ready");
    $(':input').on('drop', function (event) {
        event.preventDefault();
    });

    $(":input").on('paste', function (e) {
        e.preventDefault();
    });

    $(":input").on('copy', function (e) {
        e.preventDefault();
    });

    $(".soloNumeros").keypress(function (e) {
        key = e.keyCode || e.which;
        tecla = String.fromCharCode(key).toLowerCase();
        if (($(this).val().length == 0) && (tecla == " ")) {
            e.preventDefault();
            return false;
        }
        letras = "0123456789";
        especiales = "8-37-39-46";
        tecla_especial = false
        for (var i in especiales) {
            if (key == especiales[i]) {
                tecla_especial = true;
                break;
            }
        }
        if (letras.indexOf(tecla) == -1 && !tecla_especial) {
            e.preventDefault();
            return false;
        }
    });
    $(".soloLetras").keypress(function (e) {
        key = e.keyCode || e.which;
        tecla = String.fromCharCode(key).toLowerCase();
        if (($(this).val().length == 0) && (tecla == " ")) {
            e.preventDefault();
            return false;
        }
        letras = " áéíóúabcdefghijklmnñopqrstuvwxyz";
        especiales = "8-37-39-46";
        tecla_especial = false
        for (var i in especiales) {
            if (key == especiales[i]) {
                tecla_especial = true;
                break;
            }
        }
        if (letras.indexOf(tecla) == -1 && !tecla_especial) {
            e.preventDefault();
            return false;
        }

    });


    $('form').bind("keypress", function (e) {
        if (e.keyCode == 13) {
            e.preventDefault();
            return false;
        }
    });

    $('.tagsinput').tagsinput({
        tagClass: 'label label-primary'
    });

    var $image = $(".image-crop > img")
    $($image).cropper({
        aspectRatio: 1.618,
        preview: ".img-preview",
        done: function (data) {
            // Output the result data for cropping image.
        }
    });

    var $inputImage = $("#inputImage");
    if (window.FileReader) {
        $inputImage.change(function () {
            var fileReader = new FileReader(),
                files = this.files,
                file;

            if (!files.length) {
                return;
            }

            file = files[0];

            if (/^image\/\w+$/.test(file.type)) {
                fileReader.readAsDataURL(file);
                fileReader.onload = function () {
                    $inputImage.val("");
                    $image.cropper("reset", true).cropper("replace", this.result);
                };
            } else {
                showMessage("Please choose an image file.");
            }
        });
    } else {
        $inputImage.addClass("hide");
    }

    $("#download").click(function () {
        window.open($image.cropper("getDataURL"));
    });

    $("#zoomIn").click(function () {
        $image.cropper("zoom", 0.1);
    });

    $("#zoomOut").click(function () {
        $image.cropper("zoom", -0.1);
    });

    $("#rotateLeft").click(function () {
        $image.cropper("rotate", 45);
    });

    $("#rotateRight").click(function () {
        $image.cropper("rotate", -45);
    });

    $("#setDrag").click(function () {
        $image.cropper("setDragMode", "crop");
    });

    $('#data_1 .input-group.date').datepicker({
        todayBtn: "linked",
        keyboardNavigation: false,
        forceParse: false,
        calendarWeeks: true,
        autoclose: true
    });

    $('#data_2 .input-group.date').datepicker({
        startView: 1,
        todayBtn: "linked",
        keyboardNavigation: false,
        forceParse: false,
        autoclose: true,
        format: "dd/mm/yyyy"
    });

    $('#data_3 .input-group.date').datepicker({
        startView: 2,
        todayBtn: "linked",
        keyboardNavigation: false,
        forceParse: false,
        autoclose: true
    });

    $('#data_4 .input-group.date').datepicker({
        minViewMode: 1,
        keyboardNavigation: false,
        forceParse: false,
        forceParse: false,
        autoclose: true,
        todayHighlight: true
    });

    $('#data_5 .input-daterange').datepicker({
        keyboardNavigation: false,
        forceParse: false,
        autoclose: true
    });

    $('.i-checks').iCheck({
        checkboxClass: 'icheckbox_square-green',
        radioClass: 'iradio_square-green'
    });


    $(".touchspin1").TouchSpin({
        buttondown_class: 'btn btn-white',
        buttonup_class: 'btn btn-white'
    });

    $(".touchspin2").TouchSpin({
        min: 0,
        max: 100,
        step: 0.1,
        decimals: 2,
        boostat: 5,
        maxboostedstep: 10,
        postfix: '%',
        buttondown_class: 'btn btn-white',
        buttonup_class: 'btn btn-white'
    });

    $(".touchspin3").TouchSpin({
        verticalbuttons: true,
        buttondown_class: 'btn btn-white',
        buttonup_class: 'btn btn-white'
    });

    $('.dual_select').bootstrapDualListbox({
        selectorMinimalHeight: 160
    });


});

$('.chosen-select').chosen({ width: "100%" });

$("#ionrange_1").ionRangeSlider({
    min: 0,
    max: 5000,
    type: 'double',
    prefix: "$",
    maxPostfix: "+",
    prettify: false,
    hasGrid: true
});

$("#ionrange_2").ionRangeSlider({
    min: 0,
    max: 10,
    type: 'single',
    step: 0.1,
    postfix: " carats",
    prettify: false,
    hasGrid: true
});

$("#ionrange_3").ionRangeSlider({
    min: -50,
    max: 50,
    from: 0,
    postfix: "°",
    prettify: false,
    hasGrid: true
});

$("#ionrange_4").ionRangeSlider({
    values: [
        "January", "February", "March",
        "April", "May", "June",
        "July", "August", "September",
        "October", "November", "December"
    ],
    type: 'single',
    hasGrid: true
});

$("#ionrange_5").ionRangeSlider({
    min: 10000,
    max: 100000,
    step: 100,
    postfix: " km",
    from: 55000,
    hideMinMax: true,
    hideFromTo: false
});




    </script >

    <script type="text/javascript">

        function yesnoCheck() {
        if (document.getElementById('id_estado_civil_1').checked) {
            document.getElementById('visa_1').style.display = 'block';
        }
        else if (document.getElementById('id_estado_civil_2').checked) {
            document.getElementById('visa_1').style.display = 'block';
        }
        else{
            document.getElementById('visa_1').style.display = 'none';
        }

        if (document.getElementById('id_SiNo_0').checked) {

            document.getElementById('Si').style.display = 'none';
        }
        else
        {
            document.getElementById('Si').style.display = 'block';
        }

        if (document.getElementById('id_permiso_trabajo').checked) {

            document.getElementById('id_solicitud_permiso_trabajo').style.display = 'none';
        document.getElementById('id_solicitud_permiso_trabajo').checked = false;
    }
    else
        {
            document.getElementById('id_solicitud_permiso_trabajo').style.display = 'block';
        }


    }
    