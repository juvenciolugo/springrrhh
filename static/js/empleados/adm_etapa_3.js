
function yesnoCheck() {
    
    /*if (document.getElementById('id_estado_civil_1').checked) {
        document.getElementById('visa_1').style.display = 'block';
    }
    else if (document.getElementById('id_estado_civil_2').checked) {
        document.getElementById('visa_1').style.display = 'block';
    }
    else {
        document.getElementById('visa_1').style.display = 'none';
    }*/


    if (document.getElementById('id_SiNo_0').checked) {

        document.getElementById('Si').style.display = 'none';
    }
    else {
        document.getElementById('Si').style.display = 'block';
    }


    if (document.getElementById('id_permiso_trabajo').checked) {
        //document.getElementById('id_solicitud_permiso_trabajo').style.display = 'none';
        document.getElementById('id_solicitud_permiso_trabajo').checked = false;
        $("#sol_").hide();
    }
    else {
        document.getElementById('id_solicitud_permiso_trabajo').style.display = 'block';
        $("#sol_").show();

    }


}

$(document).ready(function () {

    $("input[type='file']").change(function () {
        var fileName = this.files[0].name;
        var ext = fileName.split('.').pop();
        var abuelo = $(this).parent();
        //var bisabuelo = $(this).parent().parent().parent();
        msg = abuelo.find(".error");
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
                $("<span class='error'> Archivo no válido  </span>").insertAfter($(this));
                //abuelo.find('.fileinput-filename').text('');
                this.files[0].name = '';
                this.value = '';

            }
        }


    });
    $('#btncanEsdo').click(function (e) {
        e.preventDefault();

        var el = $(this)
        var padre = $(this).parent();
        var abuelo = padre.parent();
        var bisabuelo = abuelo.parent();
        form = el.closest('form').get(0);
        form.reset();
        padre.hide();
        img = bisabuelo.find(".imgmat");
        img.text("Cambiar");
        im = bisabuelo.find("#img_mat");
        im.hide();
        img = bisabuelo.find(".imgnac");
        img.text("Cambiar");
        im = bisabuelo.find("#img_nac");
        im.hide();
        $("#btns").hide();

    });

    $("#data_1 input").keypress(function (e) {
        if (e.keyCode == 27) {
            $(this).val($(this).attr("value"));
            $(this).attr("readonly", "readonly");
        } else if (e.keyCode == 13) {
            e.preventDefault();
            e.keyCode = null;
            $(this).attr("readonly", "readonly");
            $("#btns").show();
        };
    });

     //cambio en calendarios seccion 1 y 2
     $("#data_2 #id_fecha_llegada").change(function () {
        var btn = $(this).parent().parent().find("#btns_2")
        btn.show();
        //$(this).attr("readonly", "readonly");
        //$("#btns").show();
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

    //click en cambiar acta de matrimonio
    $(".imgmat").click(function (e) {

        e.preventDefault();
        if (!$("#img_mat").is(":visible")) {
            $(this).text("Cancelar");
            $("#img_mat").show();
        }
        else {
            $(this).text("Cambiar");
            $("#img_mat").hide();
        }

    });

    //click en cambiar acta de nacimiento
    $(".imgnac").click(function (e) {

        e.preventDefault();
        if (!$("#img_nac").is(":visible")) {
            $(this).text("Cancelar");
            $("#img_nac").show();
        }
        else {
            $(this).text("Cambiar");
            $("#img_nac").hide();
        }

    });
    //cambio en select tipo
    $("#data_1 select").on("change", function () {
        $("#btns").show();
        if ($(this).attr("id") == "id_estado_civil") {
            if ($(this).val() == "Soltero(a)") {
                $(".conyu").hide();
            }
            else $(".conyu").show();
        }
    });
    // doble click input seccion 1
    $("#data_1 :input").dblclick(function () {
        $(this).removeAttr("readonly");
    });

    //cambio en acta
    $("#id_acta").change(function () {
        $("#btns").show();
    });

    //cambio en acta
    $("#id_acta_nacimiento").change(function () {
        $("#btns").show();
    });















    $('#frm_esdo').submit(function (event) {
        event.preventDefault();
        var thisform = $(this);
        var actionEndpoint = thisform.attr("action");
        var httpMethod = thisform.attr("method");
        var formData = $('#frm_esdo').serialize();

        $.ajax({
            cache: false,
            url: actionEndpoint,
            method: httpMethod,
            data: formData,
            success: function (data) {
                console.log("success")
                console.log(data)
                $("#editEsdoModal").modal('hide');
                location.reload();
            },
            errors: function (errorData) {
                console.log("error")
                console.log(errorData)
            }

        });

    });

    $('#frm_ext').submit(function (event) {

        event.preventDefault();
        var thisform = $(this);
        var actionEndpoint = thisform.attr("action");
        var httpMethod = thisform.attr("method");
        var formData = $('#frm_ext').serialize();


        $.ajax({
            cache: false,
            url: actionEndpoint,
            method: httpMethod,
            data: formData,
            success: function (data) {
                console.log("success")
                console.log(data)
                $("#editExtModal").modal('hide');
                location.reload();
            },
            errors: function (errorData) {
                console.log("error")
                console.log(errorData)
            }

        });

    });



    $('#id_fecha_llegada').datepicker({
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
