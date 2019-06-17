

function yesnoCheck() {


    if (document.getElementById('id_SiNo_0').checked) {

        document.getElementById('Si').style.display = 'none';
    }
    else {
        document.getElementById('Si').style.display = 'block';
    }

    if (document.getElementById('id_permiso_trabajo').checked) {

        // document.getElementById('id_solicitud_permiso_trabajo').style.display = 'none';
        document.getElementById('id_solicitud_permiso_trabajo').checked = false;
        $("#sol_").hide();
    }
    else {
        //document.getElementById('id_solicitud_permiso_trabajo').style.display = 'block';
        $("#sol_").show();
    }


}

function ValidateDate(dtValue) {
    //var validator = this;
    //alert("validatexxxx");
    msg_fec = "";
    var datePat = /^(\d{1,2})(\/|-)(\d{1,2})(\/|-)(\d{4})$/;
    var fechaCompleta = dtValue.match(datePat);
    if (fechaCompleta == null) {
        msg_fec = "Formato no válido";
        return false;
    }
    dia = fechaCompleta[1];
    mes = fechaCompleta[3];
    anio = fechaCompleta[5];

    if (dia < 1 || dia > 31) {
        msg_fec = "El valor del día debe estar comprendido entre 1 y 31.";
        return false;
    }
    if (mes < 1 || mes > 12) {
        msg_fec = "El valor del mes debe estar comprendido entre 1 y 12.";
        return false;
    }
    if ((mes == 4 || mes == 6 || mes == 9 || mes == 11) && dia == 31) {
        msg_fec = "El mes no tiene 31 días!";
        return false;
    }
    if (mes == 2) { // bisiesto
        var bisiesto = (anio % 4 == 0 && (anio % 100 != 0 || anio % 400 == 0));
        if (dia > 29 || (dia == 29 && !bisiesto)) {
            msg_fec = "Febrero de este año no contiene " + dia + " dias!";
            return false;
        }
    }
    return true;
};


function ValidaEmail(elem) {
    var input = elem.val();
    var pattern = /^\b[A-Z0-9._%-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b$/i
    if (!pattern.test(input)) {
        return false;
    }
    return true;
};

function fecha_mayor(dtVal) {
    msg_fec = ""
    //investigar si es mayor al año actual
    var hoy = new Date();
    //var fechaFormulario = dtVal;
    // Comparamos solo las fechas => no las horas!!
    hoy.setHours(0, 0, 0, 0);  // Lo iniciamos a 00:00 horas
    //convertir a fecha
    var annio = dtVal.substring(6, 10);
    var mes = dtVal.substring(3, 5);
    var dia = dtVal.substring(0, 2);
    var fechaFormulario = new Date(annio, mes - 1, dia);
    if (hoy <= fechaFormulario) {
        msg_fec = "Fecha posterior a la actual";
        //$("#id_edad").val("");
        //botones_f();
        return false;
    } else {
        //alert("es menor");
        return true;
    }

};


$(document).ready(function () {
    var es_sol = document.getElementById("status_sol").innerHTML;
    var es_casa = document.getElementById("status_casa").innerHTML;
    //alert(es_sol);
    if (!es_sol){
            $("#vista_1").hide();
            $("#id_nombre").attr("required", false);
            $("#id_apellido_paterno").attr("required", false);
            $("#id_apellido_materno").attr("required", false);
            $("#id_acta").attr("required", false);
            $("#id_acta_nacimiento").attr("required", false);
            $("#id_tlf").attr("required", false);
            $("#id_email").attr("required", false);
            $("#id_profesion").attr("required", false);
            $("#id_lugar_de_trabajo").attr("required", false);
            $("#id_profesion").attr("required", false);
            $("#id_nombre").val('');
            $("#id_apellido_paterno").val('');
            $("#id_apellido_materno").val('');
            $("#id_acta").val('');
            $("#id_acta_nacimiento").val('');
            $("#id_tlf").val('');
            $("#id_email").val('');
            $("#id_profesion").val('');
            $("#id_lugar_de_trabajo").val('');
            $("#id_profesion").val('');
    }else{
        $("#vista_1").show();
            ///////poner requeridos los campos
            $("#id_nombre").attr("required", true);
            $("#id_apellido_paterno").attr("required", true);
            $("#id_apellido_materno").attr("required", true);
            if (es_casa) {
                $("#id_acta").attr("required", true);
                $("#matri").show();
            } else {
                $("#id_acta").attr("required", false);
                $("#matri").hide();
            }

            $("#id_acta_nacimiento").attr("required", true);
            $("#id_tlf").attr("required", true);
            $("#id_email").attr("required", true);
            $("#id_profesion").attr("required", true);
            $("#id_lugar_de_trabajo").attr("required", true);
            $("#id_profesion").attr("required", true);
    }


    $(':input').on('drop', function (event) {
        event.preventDefault();
    });

    $(":input").on('paste', function (e) {
        e.preventDefault();
    });

    $(":input").on('copy', function (e) {
        e.preventDefault();
    });


    $("#btn_aceptar").click(function (e) {
        padre = $("#id_acta_nacimiento").parent();
        msg = padre.find(".error");
        if (msg.length > 0) {//si hay error da focus y no submit
            $("#id_acta_nacimiento").focus();
            e.preventDefault();
        } else {
            padre = $("#id_acta").parent();
            msg = padre.find(".error");
            if (msg.length > 0) {//si hay error da focus y no submit
                $("#id_acta").focus();
                e.preventDefault();
            } else {
                padre = $("#id_email").parent();
                msg = padre.find(".error");
                if (msg.length > 0) {//si hay error da focus y no submit
                    $("#id_email").focus();
                    e.preventDefault();
                } else {
                    padre = $("#id_email_trabajo").parent();
                    msg = padre.find(".error");
                    if (msg.length > 0) {//si hay error da focus y no submit
                        $("#id_email_trabajo").focus();
                        e.preventDefault();
                    }
                    else {
                        padre = $("#id_fecha_nacimiento_year").parent();
                        msg = padre.find(".error");
                        if (msg.length > 0) {//si hay error da focus y no submit
                            //$("#id_fecha_vencimiento_pasaporte").focus();
                            e.preventDefault();
                        }
                        else {
                            if ($("#id_nacionalidad").val() == '') {
                                padre = $("#id_nacionalidad").next();
                                msg = padre.find(".error");
                                if (msg.length > 0)
                                    msg.remove();
                                $("<span class='error'> Agrega nacionalidad  </span>").insertAfter(padre);
                                e.preventDefault();
                            }
                        }
                    }
                }
            }
        }
    });


    $('form').bind("keypress", function (e) {
        if (e.keyCode == 13) {
            e.preventDefault();
            return false;
        }
    });
    $("input[type='file']").change(function () {
        var fileName = this.files[0].name;
        var ext = fileName.split('.').pop();
        var abuelo = $(this).parent().parent();
        var bisabuelo = $(this).parent().parent().parent();
        msg = bisabuelo.find(".error");
        if (msg.length > 0)
            msg.remove();
        //abuelo.find('fileinput-filename').hide();
        switch (ext) {
            case 'jpg':
            case 'jpeg':
            case 'png':
            case 'pdf': break;
            default: {
                //alert("Archivo no válido");
                $("<span class='error'> Archivo no válido  </span>").insertAfter(this);
                //abuelo.find('.fileinput-filename').text('');
                this.files[0].name = '';
                this.value = '';

            }
        }


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

    $(".sololetrasynumeros").keypress(function (e) {
        key = e.keyCode || e.which;
        tecla = String.fromCharCode(key).toLowerCase();
        if (($(this).val().length == 0) && (tecla == " ")) {
            e.preventDefault();
            return false;
        }
        letras = " áéíóúabcdefghijklmnñopqrstuvwxyz0123456789";
        especiales = "8-37-39-46";
        tecla_especial = false
        for (var i in especiales) {
            if (key == especiales[i]) {
                tecla_especial = true;
                break;
            }
        }
        if (letras.indexOf(tecla) == -1 && !tecla_especial) {
            return false;
        }

    });

    $("#id_fecha_nacimiento_day, #id_fecha_nacimiento_month, #id_fecha_nacimiento_year").change(function (e) {
        var dia = $("#id_fecha_nacimiento_day").val();
        var mes = $("#id_fecha_nacimiento_month").val();
        var annio = $("#id_fecha_nacimiento_year").val();
        //var fechallegada = new Date(annio,mes-1,dia);
        if (dia.length == 1)
            dia = '0' + dia
        if (mes.length == 1)
            mes = '0' + mes
        var fechallegada = dia + '/' + mes + '/' + annio;
        //alert(fechallegada);
        //alert("entro");
        e.preventDefault();
        var dtVal = $(this).val();
        padre = $("#id_fecha_nacimiento_year").parent();
        msg = padre.find(".error");
        if (msg.length > 0)
            msg.remove();
        if (ValidateDate(fechallegada)) {
            if (fecha_mayor(fechallegada)) {
            }
            else {
                $(this).focus();
                $("<span class='error'>" + msg_fec + "</span>").insertAfter($("#id_fecha_nacimiento_year"));
            }
        } else {
            $(this).focus();
            $("<span class='error'>" + msg_fec + "</span>").insertAfter($("#id_fecha_nacimiento_year"));
        }

    });



    $(".emailconyu").change(function (e) {
        padre = $(this).parent();
        msg = padre.find(".error");
        if (msg.length > 0)
            msg.remove();
        if ($(this).val() != '') {
            if (!ValidaEmail($(this))) {
                $("<span class='error'> Esto no es correo  </span>").insertAfter(this);
                $(this).focus();
            };
        }
    });




    $("#id_estado_civil").change(function () {
        if ($(this).val() == "Soltero(a)" || $(this).val() == "Viudo(a)") {
            $("#vista_1").hide();
            $("#id_nombre").attr("required", false);
            $("#id_apellido_paterno").attr("required", false);
            $("#id_apellido_materno").attr("required", false);
            $("#id_acta").attr("required", false);
            $("#id_acta_nacimiento").attr("required", false);
            $("#id_tlf").attr("required", false);
            $("#id_email").attr("required", false);
            $("#id_profesion").attr("required", false);
            $("#id_lugar_de_trabajo").attr("required", false);
            $("#id_profesion").attr("required", false);
            $("#id_nombre").val('');
            $("#id_apellido_paterno").val('');
            $("#id_apellido_materno").val('');
            $("#id_acta").val('');
            $("#id_acta_nacimiento").val('');
            $("#id_tlf").val('');
            $("#id_email").val('');
            $("#id_profesion").val('');
            $("#id_lugar_de_trabajo").val('');
            $("#id_profesion").val('');
        } else {
            $("#vista_1").show();
            ///////poner requeridos los campos
            $("#id_nombre").attr("required", true);
            $("#id_apellido_paterno").attr("required", true);
            $("#id_apellido_materno").attr("required", true);
            if ($(this).val() == "Casado(a)") {
                //alert("casado");
                $("#id_acta").attr("required", true);
                $("#matri").show();
            } else {
                //alert("union");
                $("#id_acta").attr("required", false);
                $("#matri").hide();
            }

            $("#id_acta_nacimiento").attr("required", true);
            $("#id_tlf").attr("required", true);
            $("#id_email").attr("required", true);
            $("#id_profesion").attr("required", true);
            $("#id_lugar_de_trabajo").attr("required", true);
            $("#id_profesion").attr("required", true);

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
        language: "es",
        todayBtn: "linked",
        keyboardNavigation: false,
        forceParse: false,
        calendarWeeks: true,
        autoclose: true,
        format: "dd/mm/yyyy"
    });

    $('#data_2 .input-group.date').datepicker({
        language: "es",
        startView: 1,
        todayBtn: "linked",
        keyboardNavigation: false,
        forceParse: false,
        autoclose: true,
        format: "dd/mm/yyyy"
    });

    $('#data_3 .input-group.date').datepicker({
        language: "es",
        startView: 2,
        todayBtn: "linked",
        keyboardNavigation: false,
        forceParse: false,
        autoclose: true,
        format: "dd/mm/yyyy"
    });

    $('#data_4 .input-group.date').datepicker({
        language: "es",
        minViewMode: 1,
        keyboardNavigation: false,
        forceParse: false,
        forceParse: false,
        autoclose: true,
        todayHighlight: true,
        format: "dd/mm/yyyy"
    });

    $('#data_5 .input-daterange').datepicker({
        keyboardNavigation: false,
        forceParse: false,
        autoclose: true
    });

    var elem = document.querySelector('.js-switch');
    var switchery = new Switchery(elem, { color: '#1AB394' });

    var elem_2 = document.querySelector('.js-switch_2');
    var switchery_2 = new Switchery(elem_2, { color: '#ED5565' });

    var elem_3 = document.querySelector('.js-switch_3');
    var switchery_3 = new Switchery(elem_3, { color: '#1AB394' });

    var elem_4 = document.querySelector('.js-switch_4');
    var switchery_4 = new Switchery(elem_4, { color: '#f8ac59' });
    switchery_4.disable();

    $('.i-checks').iCheck({
        checkboxClass: 'icheckbox_square-green',
        radioClass: 'iradio_square-green'
    });

    $('.demo1').colorpicker();

    var divStyle = $('.back-change')[0].style;
    $('#demo_apidemo').colorpicker({
        color: divStyle.backgroundColor
    }).on('changeColor', function (ev) {
        divStyle.backgroundColor = ev.color.toHex();
    });

    $('.clockpicker').clockpicker();

    $('input[name="daterange"]').daterangepicker();

    $('#reportrange span').html(moment().subtract(29, 'days').format('MMMM D, YYYY') + ' - ' + moment().format('MMMM D, YYYY'));

    $('#reportrange').daterangepicker({
        format: 'MM/DD/YYYY',
        startDate: moment().subtract(29, 'days'),
        endDate: moment(),
        minDate: '01/01/2012',
        maxDate: '12/31/2015',
        dateLimit: { days: 60 },
        showDropdowns: true,
        showWeekNumbers: true,
        timePicker: false,
        timePickerIncrement: 1,
        timePicker12Hour: true,
        ranges: {
            'Today': [moment(), moment()],
            'Yesterday': [moment().subtract(1, 'days'), moment().subtract(1, 'days')],
            'Last 7 Days': [moment().subtract(6, 'days'), moment()],
            'Last 30 Days': [moment().subtract(29, 'days'), moment()],
            'This Month': [moment().startOf('month'), moment().endOf('month')],
            'Last Month': [moment().subtract(1, 'month').startOf('month'), moment().subtract(1, 'month').endOf('month')]
        },
        opens: 'right',
        drops: 'down',
        buttonClasses: ['btn', 'btn-sm'],
        applyClass: 'btn-primary',
        cancelClass: 'btn-default',
        separator: ' to ',
        locale: {
            applyLabel: 'Submit',
            cancelLabel: 'Cancel',
            fromLabel: 'From',
            toLabel: 'To',
            customRangeLabel: 'Custom',
            daysOfWeek: ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa'],
            monthNames: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
            firstDay: 1
        }
    }, function (start, end, label) {
        console.log(start.toISOString(), end.toISOString(), label);
        $('#reportrange span').html(start.format('MMMM D, YYYY') + ' - ' + end.format('MMMM D, YYYY'));
    });

    $(".select2_demo_1").select2();
    $(".select2_demo_2").select2();
    $(".select2_demo_3").select2({
        placeholder: "Select a state",
        allowClear: true
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

$(".dial").knob();

var basic_slider = document.getElementById('basic_slider');

noUiSlider.create(basic_slider, {
    start: 40,
    behaviour: 'tap',
    connect: 'upper',
    range: {
        'min': 20,
        'max': 80
    }
});

var range_slider = document.getElementById('range_slider');

noUiSlider.create(range_slider, {
    start: [40, 60],
    behaviour: 'drag',
    connect: true,
    range: {
        'min': 20,
        'max': 80
    }
});

var drag_fixed = document.getElementById('drag-fixed');

noUiSlider.create(drag_fixed, {
    start: [40, 60],
    behaviour: 'drag-fixed',
    connect: true,
    range: {
        'min': 20,
        'max': 80
    }
});

