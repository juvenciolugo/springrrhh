
function editar_hijo(id, nombre, paterno, materno, nac, edad) {
    var annio = nac.substring(6, 10);
    var mes = nac.substring(3, 5);
    var dia = nac.substring(0, 2);
    //alert(id)
    $("#hijoId").val(id);
    $("#id_nombre").val(nombre);
    $("#id_apellido_paterno").val(paterno);
    $("#id_apellido_materno").val(materno);
    $("#id_fecha_nacimiento_month").val(Number(mes));
    $("#id_fecha_nacimiento_day").val(Number(dia));
    $("#id_fecha_nacimiento_year").val(Number(annio));
    $("#id_edad").val(edad);
    $("#editHijoModal").modal('show');
};


$(document).ready(function () {
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




    // doble click input 
    $("#data_1 input").dblclick(function () {
        $(this).removeAttr("readonly");
    });

    //abandonar componente 
    $("#data_1 input").blur(function (e) {
        if (!$(this).is("[readonly]")) {
            $(this).val($(this).attr("value"));
            $(this).attr("readonly", "readonly");
        }
    });
    //precionar tecla esc o enter
    $("#data_1 input").keypress(function (e) {
        if (e.keyCode == 27) {
            $(this).val($(this).attr("value"));
            $(this).attr("readonly", "readonly");
        } else if (e.keyCode == 13) {
            e.preventDefault();
            e.keyCode = null;
            $(this).attr("readonly", "readonly");
            $(this).parent().parent().parent().find("#btns").show();
            //$("#btns").show();
        };
    });
    //cancelar modificacion
    $('#data_1 #btncanHijo').click(function (e) {
        e.preventDefault();
        var el = $(this)
        var padre = $(this).parent();
        form = el.closest('form').get(0);
        form.reset();
        padre.hide();
    });
    //cambio en calendarios 
    $("#data_1 #id_fecha_nacimiento").change(function () {
        $(this).attr("readonly", "readonly");
        $(this).parent().parent().parent().find("#btns").show();
    });

    $("form").submit(function (e) {
        e.preventDefault();
        var formID = $(this).attr("id");
        var thisform = $("#" + formID);
        var actionEndpoint = thisform.attr("action");
        var httpMethod = thisform.attr("method");
        var form = thisform[0];
        var formData = new FormData(form);
        $.ajax({
            cache: false,
            url: actionEndpoint,
            method: httpMethod,
            processData: false,
            contentType: false,
            data: formData,
            success: function (data) {
                console.log("success")
                console.log(data)
                if (data == "OK") {
                    $("#ok").show().fadeOut(3000);
                    thisform.find("#btns").hide();

                }
            },
            errors: function (errorData) {
                console.log("error")
                console.log(errorData)
            }

        });

    });

    $('#agregar_hijo').click(function () {
        $("#frm_add")[0].reset();
        $("#addHijoModal").modal('show');
    });



    $('#frm_add').submit(function (event) {
        event.preventDefault();
        var thisform = $(this);
        var actionEndpoint = thisform.attr("action");
        var httpMethod = thisform.attr("method");
        var formData = $('#frm_add').serialize();

        $.ajax({
            cache: false,
            url: actionEndpoint,
            method: httpMethod,
            data: formData,
            success: function (data) {
                console.log("success")
                console.log(data)
                $("#addHijoModal").modal('hide');
                location.reload();
            },
            errors: function (errorData) {
                console.log("error")
                console.log(errorData)
            }

        });

    });





    $('#data_1 #id_fecha_nacimiento').datepicker({
        language: "es",
        todayBtn: "linked",
        keyboardNavigation: false,
        forceParse: false,
        calendarWeeks: true,
        autoclose: true
    });

    $('#data_2 .input-group.date').datepicker({
        language: "es",
        todayBtn: "linked",
        keyboardNavigation: false,
        forceParse: false,
        calendarWeeks: true,
        autoclose: true
    });

    $('.chosen-select').chosen({ width: "100%" });


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

    $('.i-checks').iCheck({
        checkboxClass: 'icheckbox_square-green',
        radioClass: 'iradio_square-green',
    });

});
