


$(document).ready(function () {
    //alert("ready");
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
                    $("#ok2").show().fadeOut(3000);
                    thisform.find("#btns_2").hide();
                    thisform.find("#img_reco").hide();
                    thisform.find("#imgreco").text("Cambiar");

                    //$("#btns_2").hide();
                }
            },
            errors: function (errorData) {
                console.log("error")
                console.log(errorData)
            }

        });

    });
    //cambio en select tipo
    $("#id_tipo_comprobante").on("change", function () {
        $("#btns").show();
    });
    //cambio en select tipo
    $("#id_banco").on("change", function () {
        $("#btns").show();
    });
    // doble click input seccion 1 y 2
    $("#data_1 :input").dblclick(function () {
        $(this).removeAttr("readonly");
    });
    //abandonar componente seccion 1 y 2
    $("#data_1 input").blur(function (e) {
        if (!$(this).is("[readonly]")) {
            $(this).val($(this).attr("value"));
            $(this).attr("readonly", "readonly");
        }
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
    //click en boton cancelar seccion1
    $('#btncanCom').click(function (e) {
        e.preventDefault();
        $("#frm_com")[0].reset();
        $("#img_com").hide();
        $("#img_con").hide();
        $(".imgcom").text("Cambiar");
        $(".imgcon").text("Cambiar");
        $("#btns").hide();
    });
    //click en cambiar comprobante
    $(".imgcom").click(function (e) {
        e.preventDefault();
        if (!$("#img_com").is(":visible")) {
            $(this).text("Cancelar");
            $("#img_com").show();
        } else {
            $(this).text("Cambiar");
            $("#img_com").hide();
        }
    });
    //click en cambiar contrato
    $(".imgcon").click(function (e) {
        e.preventDefault();
        if (!$("#img_con").is(":visible")) {
            $(this).text("Cancelar");
            $("#img_con").show();
        } else {
            $(this).text("Cambiar");
            $("#img_con").hide();
        }
    });
    //click en cambiar recomendacion

    $("#data_2 .imgreco").click(function (e) {
        var hermano = $(this).parent().parent().children("#img_reco");
        //var sigima= $(this).next()
        e.preventDefault();
        if (!hermano.is(":visible")) {
            $(this).text("Cancelar");
            hermano.show();
        }
        else {
            $(this).text("Cambiar");
            hermano.hide();
        }
    });

    //cambio en comprobante image
    $("#img_com").change(function () {
        $("#btns").show();
    });
    //cambio en contrato image
    $("#img_con").change(function () {
        $("#btns").show();
    });

    //cambio en img reco
    $("#data_2 #id_carta_recomendacion").change(function () {
        var btn = $(this).parent().parent().parent().find("#btns_2")
        btn.show();
    });

    $('#data_2 #btncanReco').click(function (e) {
        e.preventDefault();
        var el = $(this)
        var padre = $(this).parent();
        var abuelo = padre.parent();
        var bisabuelo = abuelo.parent();
        form = el.closest('form').get(0);
        form.reset();
        padre.hide();
        img = bisabuelo.find(".imgreco");
        img.text("Cambiar");
        im = bisabuelo.find("#img_reco");
        im.hide();

    });





    $('#btnactCom').click(function (e) {
        e.preventDefault();
        var thisform = $('#frm_com');
        var actionEndpoint = thisform.attr("action");
        var httpMethod = thisform.attr("method");
        var form = thisform[0];
        var formData = new FormData(form);
        //var formData = $('#frm_com').serialize();

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
                    $("#btns").hide();
                    thisform.find("#img_com").hide();
                    thisform.find("#imgcom").text("Cambiar");
                    thisform.find("#img_con").hide();
                    thisform.find("#imgcon").text("Cambiar");
                }
                //$("#editComModal").modal('hide');
                //location.reload();
            },
            errors: function (errorData) {
                console.log("error")
                console.log(errorData)
            }

        });

    });

    $('#frm_rec').submit(function (event) {

        event.preventDefault();
        var thisform = $(this);
        var actionEndpoint = thisform.attr("action");
        var httpMethod = thisform.attr("method");
        var formData = $('#frm_rec').serialize();


        $.ajax({
            cache: false,
            url: actionEndpoint,
            method: httpMethod,
            data: formData,
            success: function (data) {
                console.log("success")
                console.log(data)
                $("#editRecModal").modal('hide');
                location.reload();
            },
            errors: function (errorData) {
                console.log("error")
                console.log(errorData)
            }

        });

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
