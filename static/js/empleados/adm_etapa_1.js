
function checa(str1, str2) {
    if (str1 != str2)
        //alert("1"+str1);

        //$("#btnactBas").show();
        return false;
};



$(document).ready(function () {
    $(':input').on('drop', function (event) {
        event.preventDefault();
    });

    $(":input").on('paste', function (e) {
        e.preventDefault();
    });

    $(":input").on('copy', function (e) {
        e.preventDefault();
    });

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
    //click en cambiar nacionalidades
    $(".nnac").click(function (e) {
        e.preventDefault();
        if (!$("#n_nac").is(":visible")) {
            $(this).text("Cancelar");
            $("#n_nac").show();
        }
        else {
            $(this).text("Modificar");
            $("#n_nac").hide();
        }

    });
    //click en cambiar pasaporte
    $(".imgpas").click(function (e) {
        e.preventDefault();
        if (!$("#img_pas").is(":visible")) {
            $(this).text("Cancelar");
            $("#img_pas").show();
        }
        else {
            $(this).text("Cambiar");
            $("#img_pas").hide();
        }

    });
    //click en cambiar frente(INE)
    $(".imgfrente").click(function (e) {
        e.preventDefault();
        if (!$("#img_frente").is(":visible")) {
            $(this).text("Cancelar");
            $("#img_frente").show();
        }
        else {
            $(this).text("Cambiar");
            $("#img_frente").hide();
        }

    });

    //click en cambiar atras(INE)
    $(".imgatras").click(function (e) {
        e.preventDefault();
        if (!$("#img_atras").is(":visible")) {
            $(this).text("Cancelar");
            $("#img_atras").show();
        }
        else {
            $(this).text("Cambiar");
            $("#img_atras").hide();
        }

    });
    //click en cambiar foto
    $(".imgfoto").click(function (e) {
        e.preventDefault();
        if (!$("#img_foto").is(":visible")) {
            $(this).text("Cancelar");
            $("#img_foto").show();
        }
        else {
            $(this).text("Cambiar");
            $("#img_foto").hide();
        }

    });

    //click en cambiar acta
    $(".imgacta").click(function (e) {
        e.preventDefault();
        if (!$("#img_acta").is(":visible")) {
            $(this).text("Cancelar");
            $("#img_acta").show();
        }
        else {
            $(this).text("Cambiar");
            $("#img_acta").hide();
        }

    });


    function set_valores() {
        //alert("entro");
        $("#frm_bas")[0].reset();
        //alert();
        $("#nombrelbl").text($("#id_nombre").attr("value"));
        $("#paternolbl").text($("#id_apellido_paterno").val());
        $("#maternolbl").text($("#id_apellido_materno").val());
        $("#naclbl").text($("#id_fecha_nacimiento").val());
        $("#edadlbl").text($("#id_edad").val());
        $("#tellbl").text($("#id_tel").val());
        $("#cellbl").text($("#id_cel").val());
        $("#emaillbl").text($("#id_email_personal").val());
        //$("#tipolbl").text(text);
        $("#callelbl").text($("#id_calle").val());
        $("#nextlbl").text($("#id_num_ext").val());
        $("#nintlbl").text($("#id_num_int").val());
        $("#entrelbl").text($("#id_calle_uno").val());
        $("#ylbl").text($("#id_calle_dos").val());
        $("#cplbl").text($("#id_cp").val());
        $("#collbl").text($("#id_colonia").val());
        //alert("termino");
        //$("#esdolbl").text(text);
        //$("#paislbl").text(text);
        //$("#paisnaclbl").text(text);
    };

    // doble click input seccion 1 y 2
    $("#data_1 :input").dblclick(function () {
        $(this).removeAttr("readonly");
    });
    $("#data_2 :input").dblclick(function () {
        $(this).removeAttr("readonly");
    });

    //abandonar componente seccion 1 y 2
    $("#data_1 input").blur(function (e) {
        if (!$(this).is("[readonly]")) {
            $(this).val($(this).attr("value"));
            //$(this).attr("readonly", "readonly");
        }
    });

    $("#data_2 input").blur(function (e) {

        if (!$(this).is("[readonly]")) {
            $(this).attr("readonly", "readonly");
            $(this).val($(this).attr("value"));
        }
    });

    //abandona selects seccion 1 y 2

    $("#data_1 select").blur(function (e) {
        $("#data_1 .editlbl").show();
    });

    $("#data_2 select").blur(function (e) {
        $("#data_2 .editlbl").show();
    });

    //preciona tecla esc en select seccion 1 y 2
    $("#data_1 select").keydown(function (e) {
        if (e.keyCode == 27) {
            e.preventDefault();
            $("#data_1 .select_").hide();
            $("#data_1 .editlbl").show();
        }
    });

    $("#data_2 select").keydown(function (e) {
        if (e.keyCode == 27) {
            e.preventDefault();
            $("#data_2 .select_").hide();
            $("#data_2 .editlbl").show();
        }
    });

    //preciona tecla esc y enter en input seccion 1 y 2
    $("#data_2 input").keypress(function (e) {
        if (e.keyCode == 27) {
            $(this).val($(this).attr("value"));
            $(this).attr("readonly", "readonly");
        } else if (e.keyCode == 13) {
            e.preventDefault();
            e.keyCode = null;
            $(this).attr("readonly", "readonly");
            $("#btns_2").show();
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
    //cambio en foto
    $("#id_foto").change(function () {
        $("#btns").show();
    });

    //cambio en acta
    $("#id_acta_nacimiento").change(function () {
        $("#btns").show();
    });
    //cambio en ine front
    $("#id_docu_ident_front").change(function () {
        $("#btns_2").show();
    });
    //cambio en ine back
    $("#id_docu_ident_back").change(function () {
        $("#btns_2").show();
    });
    //cambio en pasaporte
    $("#id_imagen_pasaporte").change(function () {
        $("#btns_2").show();
    });


    //cambio en multichoice nacionalidades
    $("#id_nacionalidad").on("change", function () {
        //if(!$("#id_nacionalidad").length==0)
        $("#btns_2").show();
    });
    //cambio en select seccion 1 y 2
    $("#id_pais_direc").on("change", function () {
        //$("#paislbl").text($("#id_pais_direc option:selected").text());
        $("#btns").show();
    });

    $("#id_pais_nacimiento").on("change", function () {
        //$("#paisnaclbl").text($("#id_pais_nacimiento option:selected").text());
        $("#btns").show();
    });

    $("#id_esdo").on("change", function () {
        //$("#esdolbl").text($("#id_esdo option:selected").text());
        $("#btns").show();
    });

    $("#id_tipo_documento_identidad").on("change", function () {
        $("#btns_2").show();
    });

    $("#id_tipo").on("change", function () {
        if ($("#id_tipo option:selected").text() == "Departamento") {
            $("#opc_dep").show();

        } else $("#opc_dep").hide();
        $("#btns").show();
    });

    //cambio en calendarios seccion 1 y 2
    $("#id_fecha_nacimiento").change(function () {
        $(this).attr("readonly", "readonly");
        $("#btns").show();
    });

    $("#id_fecha_vencimiento_pasaporte").change(function () {
        $(this).attr("readonly", "readonly");
        $("#btns_2").show();
    });

    //click en boton cancelar seccion1
    $('#btncanBas').click(function (e) {
        e.preventDefault();
        $("#frm_bas")[0].reset();
        if ($("#id_tipo").val() == "Casa")
            $("#opc_dep").hide();
        else
            $("#opc_dep").show();
        $("#img_foto").hide();
        $("#img_acta").hide();
        $(".imgfoto").text("Cambiar");
        $(".imgacta").text("Cambiar");
        $("#btns").hide();
    });
    //click en boton cancelar seccion2
    $('#btncanNac').click(function (e) {
        e.preventDefault();
        $("#frm_nac")[0].reset();
        $("#img_frente").hide();
        $("#img_atras").hide();
        $("#img_pas").hide();
        $(".imgfrente").text("Cambiar");
        $(".imgatras").text("Cambiar");
        $(".imgpas").text("Cambiar");
        $("#btns_2").hide();
    });

    /*$('#edit_nac').click(function () {
        $("#frm_nac")[0].reset();
        $("#editNacModal").modal('show');
    });*/

    //llamado ajax por boton actualizar seccion1
    $('#btnactBas').click(function (e) {
        e.preventDefault();
        padre = $("#id_foto").parent();
        msg = padre.find(".error");
        if (msg.length > 0) {//si hay error da focus y no submit
            $("#id_foto").focus();
            
        }
        var thisform = $('#frm_bas');
        var actionEndpoint = thisform.attr("action");
        var httpMethod = thisform.attr("method");
        var form = thisform[0];

        var formData = new FormData(form);
        //var formData = thisform.serialize();
        $.ajax({
            cache: false,
            url: actionEndpoint,
            method: httpMethod,
            processData: false,
            contentType: false,
            data: formData,
            success: function (data) {
                console.log("success")
                console.log(data);
                if (data == "OK") {
                    $("#ok").show().fadeOut(3000);
                    //alert("Datos Actualizados!!");
                    $("#btns").hide();
                }
            },
            errors: function (errorData) {
                console.log("error")
                console.log(errorData)
            }
        });
    });

    //llamado ajax por boton actualizar seccion2

    $('#btnactNac').click(function (e) {
        e.preventDefault();
        var thisform = $('#frm_nac');
        var actionEndpoint = thisform.attr("action");
        var httpMethod = thisform.attr("method");
        var form = thisform[0];

        var formData = new FormData(form);
        //var formData = thisform.serialize();
        $.ajax({
            cache: false,
            url: actionEndpoint,
            method: httpMethod,
            processData: false,
            contentType: false,
            data: formData,
            success: function (data) {
                if (data == "OK") {
                    $("#ok2").show().fadeOut(3000);
                    //alert("Datos Actualizados!!");
                    $("#btns_2").hide();
                }
            },
            errors: function (errorData) {
                console.log("error")
                console.log(errorData)
            }
        });
    });



    $('#id_fecha_nacimiento').datepicker({
        language: "es",
        todayBtn: "linked",
        keyboardNavigation: false,
        forceParse: false,
        calendarWeeks: true,
        autoclose: true
    });

    $('#id_fecha_vencimiento_pasaporte').datepicker({
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

