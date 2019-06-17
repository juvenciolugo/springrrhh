
var ref = 0;



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
        document.getElementById('id_solicitud_permiso_trabajo').style.display = 'block';
        $("#sol_").show();
    }


};

function ValidaEmail(elem) {
    var input = elem.val();
    var pattern = /^\b[A-Z0-9._%-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b$/i
    if (!pattern.test(input)) {
        return false;
    }
    return true;
};

$(document).ready(function () {

    var msg_fec = "hola";

    $(':input').on('drop', function (event) {
        event.preventDefault();
    });

    $(":input").on('paste', function (e) {
        e.preventDefault();
    });

    $(":input").on('copy', function (e) {
        e.preventDefault();
    });

    $("#id_pais_direc").change(function () {
        if ($(this).val() == '1')
            $("#esdo_div").show();

        else
            $("#esdo_div").hide();

    });

    $("#btn_aceptar").click(function (e) {


        padre = $("#id_fecha_nacimiento").parent();
        msg = padre.find(".error");
        if (msg.length > 0) {//si hay error da focus y no submit
            $("#id_fecha_nacimiento").focus();
            e.preventDefault();
        } else {
            padre = $("#id_email_personal").parent();
            msg = padre.find(".error");
            if (msg.length > 0) {//si hay error da focus y no submit
                $("#id_email_personal").focus();
                e.preventDefault();
            } else {
                padre = $("#id_fecha_vencimiento_pasaporte").parent();
                msg = padre.find(".error");
                if (msg.length > 0) {//si hay error da focus y no submit
                    $("#id_fecha_vencimiento_pasaporte").focus();
                    e.preventDefault();
                }
                else {
                    padre = $("#id_fecha_llegada_year").parent();
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

    });

    $("#id_nacionalidad").change(function () {
        if ($("#id_nacionalidad").val() != '') {
            padre = $("#id_nacionalidad").parent();
            msg = padre.find(".error");
            if (msg.length > 0)
                msg.remove();
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

    yesnoCheck();
    $("#id_referencia").keypress(function (e) {
        var key = e.keyCode;
        if (e.keyCode == 13) {
            ref = 1;
        } else ref = 0;
    });

    $('form').bind("keypress", function (e) {

        if (e.keyCode == 13 && ref == 0) {
            e.preventDefault();
            return false;
        }
    });
    $("#id_cp").keypress(function (event) {
        var key = event.keyCode;
        if ((this.value.length == 5) || (key == 101) || (key == 69)) return false;
    });
    $("#id_cp").change(function (event) {
        var key = event.keyCode;
        if (this.value < 0) {
            this.value = 0;
            return false;
        }
        else if (this.value > 99999) {
            this.value = 99999;
            return false;
        }
    });

    function obten_edad(cumpleStr) {
        var hoy = new Date();
        var annio = cumpleStr.substring(6, 10);
        var mes = cumpleStr.substring(3, 5);
        var dia = cumpleStr.substring(0, 2);
        var cumple = new Date(annio, mes - 1, dia);
        var edad = hoy.getFullYear() - cumple.getFullYear();
        var m = hoy.getMonth() - cumple.getMonth();
        if (m < 0 || (m === 0 && hoy.getDate() < cumple.getDate())) {
            edad--;
        }
        return edad;
    };

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
                $("<span class='error'> Archivo no válido  </span>").insertAfter(abuelo);
                //abuelo.find('.fileinput-filename').text('');
                this.files[0].name = '';
                this.value = '';

            }
        }


    });
    $("#pascheck").change(function () {
        if ($(this).is(":checked")) {
            $("#pass_").show();
            $("#id_pasaporte").attr("required", true);

        }
        else {
            $("#pass_").hide();
            $("#id_pasaporte").attr("required", false);
        }
    });

    $("#id_email_personal").change(function (e) {
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


    $("#id_tipo_documento_identidad").change(function () {
        if ($(this).val() == 3) {
            $("#pass_").show();
            $("#cedine_").hide();
            $("#pascheck").prop("checked", true);
        }
        else if (($(this).val() == 1) || ($(this).val() == 2)) {
            $("#pass_").hide();
            $("#cedine_").show();
            $("#pascheck").prop("checked", false);
        }

    });

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

    /*$("#id_fecha_nacimiento").focusout(function() {
        if ($("#id_fecha_nacimiento").val())
           $("#id_edad").val(obten_edad($("#id_fecha_nacimiento").val()));
    });*/

    $("#id_fecha_nacimiento").change(function (e) {
        //alert("entro");
        e.preventDefault();
        var dtVal = $(this).val();
        padre = $(this).parent();
        msg = padre.find(".error");
        if (msg.length > 0)
            msg.remove();
        if ($(this).val() != '') {
            if (ValidateDate(dtVal)) {
                if (fecha_mayor(dtVal)) {
                    var edad = obten_edad($(this).val());
                    $("#id_edad").val(edad);
                }
                else {
                    $(this).focus();
                    $("<span class='error'>" + msg_fec + "</span>").insertAfter($(this));
                }
            } else {
                $(this).focus();
                $("<span class='error'>" + msg_fec + "</span>").insertAfter($(this));
            }
        }
        //if ($("#id_fecha_nacimiento").val())
        //   $("#id_edad").val(obten_edad($("#id_fecha_nacimiento").val()));
    });

    $("#id_fecha_vencimiento_pasaporte").change(function (e) {
        //alert("entro");
        e.preventDefault();
        var dtVal = $(this).val();
        padre = $(this).parent();
        msg = padre.find(".error");
        if (msg.length > 0)
            msg.remove();
        if ($(this).val() != '') {
            if (ValidateDate(dtVal)) {

            } else {
                $(this).focus();
                $("<span class='error'>" + msg_fec + "</span>").insertAfter($(this));
            }
        }
        //if ($("#id_fecha_nacimiento").val())
        //   $("#id_edad").val(obten_edad($("#id_fecha_nacimiento").val()));
    });

    $("#id_fecha_llegada_day, #id_fecha_llegada_month, #id_fecha_llegada_year").change(function (e) {
        var dia = $("#id_fecha_llegada_day").val();
        var mes = $("#id_fecha_llegada_month").val();
        var annio = $("#id_fecha_llegada_year").val();
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
        padre = $("#id_fecha_llegada_year").parent();
        msg = padre.find(".error");
        if (msg.length > 0)
            msg.remove();
        if (ValidateDate(fechallegada)) {
            if (fecha_mayor(fechallegada)) {
            }
            else {
                $(this).focus();
                $("<span class='error'>" + msg_fec + "</span>").insertAfter($("#id_fecha_llegada_year"));
            }
        } else {
            $(this).focus();
            $("<span class='error'>" + msg_fec + "</span>").insertAfter($("#id_fecha_llegada_year"));
        }

    });

    $("#id_tipo").change(function () {
        if ($(this).val() == "Casa") {
            $("#piso").val("");
            $("#depto").val("");
            $("#tipo_c").hide();
        }
        else $("#tipo_c").show();
    });

    $('#data_1 .input-group.date').datepicker({
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
