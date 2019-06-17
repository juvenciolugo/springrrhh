
var token = '{{ csrf_token }}';






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
    function borrar_sec3(id) {
        $.ajax({
            cache: false,
            url: "/borrar_idi",
            method: "GET",
            data: { id: id },
            success: function (data) {
                if (data.form_is_valid) {
                    $("#myModalLabel").text("¡Idioma eliminado!");
                    $("#miModal .modal-body").html("pupuPuedes seguir agregando o guardar sección y continuar");
                    $("#miModal").modal('show');
                    location.reload();

                }
            },
            errors: function (errorData) {
                console.log("error")
                console.log(errorData)
            }

        });

    };
    function borrar_capa_sec3(id) {
        $.ajax({
            cache: false,
            url: "/borrar_capa",
            method: "GET",
            data: { id: id },
            success: function (data) {
                if (data.form_is_valid) {
                    $("#myModalLabel").text("¡Capacitación eliminada!");
                    $("#miModal .modal-body").html("pupuPuedes seguir agregando o guardar sección y continuar");
                    $("#miModal").modal('show');
                    location.reload();

                }
            },
            errors: function (errorData) {
                console.log("error")
                console.log(errorData)
            }

        });

    };

    $(".contenido").on("click", ".btnDelete", function (e) {
        e.preventDefault();
        var id = $(this).data('id');
        var reg = $(this).data('reg');
        $('#myModalDel').data({ 'id': id, 'reg': reg }).modal('show');
    });

    $('#btnDelteYes').click(function (e) {
        // Borrar registro
        e.preventDefault();
        var id = $('#myModalDel').data('id');
        var reg = $('#myModalDel').data('reg');
        $('#myModalDel').modal('hide');
        if (reg == "IDIOMA")
            borrar_sec3(id);
        else if (reg == "CAPA")
            borrar_capa_sec3(id);
    });


    $("form").submit(function (e) {
        e.preventDefault();
        var formID = $(this).attr("id");
        if (formID == "frm_addsec2" || formID == "frm_addsec3" || formID == "frm_sec1")
            return false;
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
                if (data == "OK2") {
                    $("#ok2").show().fadeOut(3000);
                    thisform.find("#btns2").hide();
                    icur = thisform.find("#t_curso");
                    scur = thisform.find("#id_tipo_curso");
                    icur.val(scur.val()).show();
                    scur.hide();
                    icer = thisform.find("#img_cur");
                    icer.hide();
                    thisform.find(".imgcur").text("Cambiar");

                } else if (data == "OK3") {
                    $("#ok3").show().fadeOut(3000);
                    thisform.find("#btns3").hide();
                    nesc = thisform.find("#n_esc");
                    sesc = thisform.find("#id_nivel_escrito");
                    nesc.val(sesc.val()).show();
                    sesc.hide();
                    nhab = thisform.find("#n_hab");
                    shab = thisform.find("#id_nivel_hablado");
                    nhab.val(shab.val()).show();
                    shab.hide();
                }
            },
            errors: function (errorData) {
                console.log("error")
                console.log(errorData)
            }
        });
    });

    /* $('#edit_sec1').click(function () {
         $("#frm_sec1")[0].reset();
         $("#editSec1Modal").modal('show');
     });*/

    /*$('#edit_sec2').click(function() {
        $("#editSec2Modal").modal('show');
    });*/
    // doble click input  sec1
    $("#data_1 input").dblclick(function () {
        $(this).removeAttr("readonly");
    });
    // doble click input sec2
    $("#data_2 input").dblclick(function () {

        if ($(this).attr("id") == "t_curso") {
            $(this).next().val($(this).val()).show();
            $(this).hide();
        }
        else $(this).removeAttr("readonly");
    });

    // doble click input sec3
    $("#data_3 input").dblclick(function () {
        id = $(this).attr("id");
        if ((id == "n_esc") || (id == "n_hab")) {
            $(this).next().val($(this).val()).show();
            $(this).hide();
        }
        else $(this).removeAttr("readonly");
    });

    //abandonar componente 
    $("#data_1 input").blur(function (e) {
        if (!$(this).is("[readonly]")) {
            $(this).val($(this).attr("value"));
            $(this).attr("readonly", "readonly");
        }
    });
    //abandonar componente 
    $("#data_2 input").blur(function (e) {
        if (!$(this).is("[readonly]")) {
            $(this).val($(this).attr("value"));
            $(this).attr("readonly", "readonly");
        }
    });
    //abandonar componente 
    $("#data_3 input").blur(function (e) {
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
    //precionar tecla esc o enter sec2
    $("#data_2 input").keypress(function (e) {
        if (e.keyCode == 27) {
            $(this).val($(this).attr("value"));
            $(this).attr("readonly", "readonly");
            sig = $(this).next();
            if (sig.attr("id") == "t_curso")
                sig.hide();
        } else if (e.keyCode == 13) {
            e.preventDefault();
            e.keyCode = null;
            $(this).attr("readonly", "readonly");
            $(this).parent().parent().parent().find("#btns2").show();
            //$("#btns").show();
        };
    });
    //precionar tecla esc o enter sec3
    $("#data_3 input").keypress(function (e) {
        if (e.keyCode == 27) {
            $(this).val($(this).attr("value"));
            $(this).attr("readonly", "readonly");
            sig = $(this).next();
            if (sig.attr("id") == "n_esc" || sig.attr("id") == "n_hab")
                sig.hide();
        } else if (e.keyCode == 13) {
            e.preventDefault();
            e.keyCode = null;
            $(this).attr("readonly", "readonly");
            $(this).parent().parent().parent().find("#btns3").show();
            //$("#btns").show();
        };
    });

    //click en boton cancelar seccion1
    $('#data_1 #btncanSec1').click(function (e) {
        e.preventDefault();
        $("#frm_sec1")[0].reset();
        $("#img_ced").hide();
        $("#img_con").hide();
        $(".imgced").text("Cambiar");
        $(".imgcon").text("Cambiar");
        $("#btns").hide();
    });
    //click en boton cancelar seccion1
    $('#data_2 #btncansec2').click(function (e) {
        e.preventDefault();
        var el = $(this);
        var padre = $(this).parent();
        var abuelo = padre.parent();
        var bisabuelo = abuelo.parent();
        form = el.closest('form').get(0);
        form.reset();
        padre.hide();
        bisabuelo.find("#id_tipo_curso").hide();
        bisabuelo.find("#t_curso").show();
        img = bisabuelo.find(".imgcur");
        img.text("Cambiar");
        im = bisabuelo.find("#img_cur");
        im.hide();


    });
    //click en boton cancelar seccion1
    $('#data_3 #btncansec3').click(function (e) {
        e.preventDefault();
        var el = $(this);
        var padre = $(this).parent();
        var abuelo = padre.parent();
        var bisabuelo = abuelo.parent();
        form = el.closest('form').get(0);
        form.reset();
        padre.hide();
        bisabuelo.find("#id_nivel_escrito").hide();
        bisabuelo.find("#id_nivel_hablado").hide();
        bisabuelo.find("#n_esc").show();
        bisabuelo.find("#n_hab").show();



    });
    /*$('#data_1 #btncanSec1').click(function (e) {
            e.preventDefault();
            var el =$(this)
            var padre=$(this).parent();
            form=el.closest('form').get(0);
            form.reset();
            padre.hide();
    });*/

    //cambio en permanente
    $("#id_nivel_estudios").change(function () {
        $(this).attr("readonly", "readonly");
        $("#btns").show();
    });
    //cambio en cedula image
    $("#id_cedula_profesional_imagen_cedula_profesional").change(function () {
        $("#btns").show();
    });
    //cambio en constancia image
    $("#id_constancia_de_estudio").change(function () {
        $("#btns").show();
    });
    //click en cambiar visa
    $("#data_1 .imgced").click(function (e) {
        e.preventDefault();
        if (!$("#img_ced").is(":visible")) {
            $(this).text("Cancelar");
            $("#img_ced").show();
        }
        else {
            $(this).text("Cambiar");
            $("#img_ced").hide();
        }

    });
    //click en cambiar visa
    $("#data_1 .imgcon").click(function (e) {
        e.preventDefault();
        if (!$("#img_con").is(":visible")) {
            $(this).text("Cancelar");
            $("#img_con").show();
        }
        else {
            $(this).text("Cambiar");
            $("#img_con").hide();
        }

    });
    //click en cambiar curso image sec2
    $("#data_2 .imgcur").click(function (e) {
        var sigima = $(this).next()

        e.preventDefault();
        if (!sigima.is(":visible")) {
            $(this).text("Cancelar");
            sigima.show();
        }
        else {
            $(this).text("Cambiar");
            sigima.hide();
        }

    });
    //cambio en lic anv
    $("#data_2 #id_certificado").change(function () {
        var btn = $(this).parent().parent().parent().parent().find("#btns2")
        btn.show();
    });
    //cambio en tipo curso
    $("#data_2 select").change(function () {
        var btn = $(this).parent().parent().parent().find("#btns2")
        btn.show();
    });
    //cambio en nivelñ hablado/escrito
    $("#data_3 select").change(function () {
        var btn = $(this).parent().parent().parent().find("#btns3")
        btn.show();
    });








    $('#add_sec2').click(function () {
        $("#frm_addsec2")[0].reset();
        $("#addSec2Modal").modal('show');
    });

    /* $('#edit_sec3').click(function () {
         $("#editSec3Modal").modal('show');
     });*/

    $('#add_sec3').click(function () {
        $("#frm_addsec3")[0].reset();
        $("#addSec3Modal").modal('show');
    });



    $('#frm_sec1').submit(function (event) {
        event.preventDefault();

        var thisform = $(this);
        var actionEndpoint = thisform.attr("action");
        var httpMethod = thisform.attr("method");
        var form = thisform[0];
        var formData = new FormData(form);
        //var formData = $('#frm_sec1').serialize();

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
                    thisform.find("#img_ced").hide();
                    thisform.find(".imgced").text("Cambiar");
                    thisform.find("#img_con").hide();
                    thisform.find(".imgcon").text("Cambiar");
                }

            },
            errors: function (errorData) {
                console.log("error")
                console.log(errorData)
            }

        });

    });



    $('#frm_addsec2').submit(function (event) {

        event.preventDefault();

        var thisform = $(this);
        var actionEndpoint = thisform.attr("action");
        var httpMethod = thisform.attr("method");
        //var formData = $('#frm_addsec2').serialize();
        var form = $(this)[0];

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
                $("#addSec2Modal").modal('hide');
                location.reload();
            },
            errors: function (errorData) {
                console.log("error")
                console.log(errorData)
            }
        });
    });


    $('#frm_addsec3').submit(function (event) {

        event.preventDefault();

        var thisform = $(this);
        var actionEndpoint = thisform.attr("action");
        var httpMethod = thisform.attr("method");
        var formData = $('#frm_addsec3').serialize();
        $.ajax({
            cache: false,
            url: actionEndpoint,
            method: httpMethod,
            data: formData,
            success: function (data) {
                console.log("success")
                console.log(data)
                $("#addSec3Modal").modal('hide');
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
