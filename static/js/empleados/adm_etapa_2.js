
function yesnoCheck() {
    if (document.getElementById('inlineRadio1').checked) {
        document.getElementById('visa_1').style.display = 'block';
        document.getElementById('visa_2').style.display = 'none';
        document.getElementById('visa_3').style.display = 'none';
        document.getElementById('visa_4').style.display = 'none';
        document.getElementById('visa_5').style.display = 'none';
    }
    else if (document.getElementById('inlineRadio2').checked) {
        document.getElementById('visa_1').style.display = 'block';
        document.getElementById('visa_2').style.display = 'block';
        document.getElementById('visa_3').style.display = 'none';
        document.getElementById('visa_4').style.display = 'none';
        document.getElementById('visa_5').style.display = 'none';
    }
    else if (document.getElementById('inlineRadio3').checked) {
        document.getElementById('visa_1').style.display = 'block';
        document.getElementById('visa_2').style.display = 'block';
        document.getElementById('visa_3').style.display = 'block';
        document.getElementById('visa_4').style.display = 'none';
        document.getElementById('visa_5').style.display = 'none';
    }
    else if (document.getElementById('inlineRadio4').checked) {
        document.getElementById('visa_1').style.display = 'block';
        document.getElementById('visa_2').style.display = 'block';
        document.getElementById('visa_3').style.display = 'block';
        document.getElementById('visa_4').style.display = 'block';
        document.getElementById('visa_5').style.display = 'none';
    }
    else if (document.getElementById('inlineRadio5').checked) {
        document.getElementById('visa_1').style.display = 'block';
        document.getElementById('visa_2').style.display = 'block';
        document.getElementById('visa_3').style.display = 'block';
        document.getElementById('visa_4').style.display = 'block';
        document.getElementById('visa_5').style.display = 'block';
    }
    else {
        document.getElementById('visa_1').style.display = 'none';
        document.getElementById('visa_2').style.display = 'none';
        document.getElementById('visa_3').style.display = 'none';
        document.getElementById('visa_4').style.display = 'none';
        document.getElementById('visa_5').style.display = 'none';
    }

    if (document.getElementById('inlineRadio8').checked) {
        document.getElementById('licencia').style.display = 'block';
    } else {
        document.getElementById('licencia').style.display = 'none';
    }
}

function editar_lic(id, fecha, permanente, esdo, licencia) {

    //alert(id);
    $("#licId").val(id);
    $("#id_fecha_vigencia").val(fecha);
    $("#id_permanente").val(permanente);
    $("#id_estado_emision").val(esdo);
    $("#id_licencia").val(licencia);
    $("#editLicModal").modal('show');
};




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
        //alert(formDetails.serialize());
        //llamado ajax
        //var thisform = $(this);
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
                console.log(data)
                if (data == "OK") {
                    $("#ok2").show().fadeOut(3000);

                    $("#btns_2").hide();
                }
            },
            errors: function (errorData) {
                console.log("error")
                console.log(errorData)
            }

        });

    });
    //cambio en curp
    $("#id_imagen_curp").change(function () {
        $("#btns").show();
    });
    //cambio en rfc
    $("#id_imagen_rfc").change(function () {
        $("#btns").show();
    });
    //cambio en sat
    $("#id_imagen_sat").change(function () {
        $("#btns").show();
    });
    //cambio en imss
    $("#id_imagen_imss").change(function () {
        $("#btns").show();
    });
    //cambio en infonavit
    $("#id_imagen_infonavit").change(function () {
        $("#btns").show();
    });
    //cambio en lic rev
    $("#id_img_lic_reverso").change(function () {
        $("#btns").show();
    });
    //cambio en lic anv
    $("#id_img_lic_anverso").change(function () {
        $("#btns").show();
    });
    //cambio en lic anv
    $("#data_2 #id_imagen_visa").change(function () {
        var btn = $(this).parent().parent().parent().find("#btns_2")
        btn.show();


        //$("#btns_2").show();
    });


    //click en cambiar visa
    $("#data_2 .imgvisa").click(function (e) {
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




    //click en cambiar curp
    $(".imgcurp").click(function (e) {

        e.preventDefault();
        if (!$("#img_curp").is(":visible")) {
            //if($("#img_curp").)
            $(this).text("Cancelar");
            $("#img_curp").show();
        }
        else {
            $(this).text("Cambiar");
            $("#img_curp").hide();
        }

    });

    //click en cambiar rfc
    $(".imgrfc").click(function (e) {

        e.preventDefault();
        if (!$("#img_rfc").is(":visible")) {
            $(this).text("Cancelar");
            $("#img_rfc").show();
        }
        else {
            $(this).text("Cambiar");
            $("#img_rfc").hide();
        }

    });
    //click en cambiar sat
    $(".imgsat").click(function (e) {

        e.preventDefault();
        if (!$("#img_sat").is(":visible")) {
            $(this).text("Cancelar");
            $("#img_sat").show();
        }
        else {
            $(this).text("Cambiar");
            $("#img_sat").hide();
        }

    });
    //click en cambiar imss
    $(".imgimss").click(function (e) {

        e.preventDefault();
        if (!$("#img_imss").is(":visible")) {
            $(this).text("Cancelar");
            $("#img_imss").show();
        }
        else {
            $(this).text("Cambiar");
            $("#img_imss").hide();
        }

    });
    //click en cambiar infonavit
    $(".imginfonavit").click(function (e) {

        e.preventDefault();
        if (!$("#img_infonavit").is(":visible")) {
            $(this).text("Cancelar");
            $("#img_infonavit").show();
        }
        else {
            $(this).text("Cambiar");
            $("#img_infonavit").hide();
        }

    });
    //click en cambiar lic anverso
    $(".imglicanv").click(function (e) {
        e.preventDefault();
        if (!$("#img_licanv").is(":visible")) {
            $(this).text("Cancelar");
            $("#img_licanv").show();
        }
        else {
            $(this).text("Cambiar");
            $("#img_licanv").hide();
        }

    });
    //click en cambiar lic reverso
    $(".imglicrev").click(function (e) {
        e.preventDefault();
        if (!$("#img_licrev").is(":visible")) {
            $(this).text("Cancelar");
            $("#img_licrev").show();
        }
        else {
            $(this).text("Cambiar");
            $("#img_licrev").hide();
        }

    });

    // doble click input seccion 1 y 2
    $("#data_1 :input").dblclick(function () {
        $(this).removeAttr("readonly");
    });
    $("form ._paisinput").dblclick(function () {
        var hermano = $(this).parent().children("#id_pais");
        if (hermano) {
            hermano.show();
            $(this).hide();
        }



    });



    //abandonar componente seccion 1 y 2
    $("#data_1 input").blur(function (e) {
        if (!$(this).is("[readonly]")) {
            $(this).val($(this).attr("value"));
            $(this).attr("readonly", "readonly");
        }
    });

    $("#data_2 input").blur(function (e) {
        $("#data_2 .editlbl").show();
        $(this).attr("readonly", "readonly");
        $(this).val($(this).attr("value"));
    });

    //cambio en select seccion 1 y 2
    $("#id_estado_emision_licencia").on("change", function () {
        $("#btns").show();
    });
    //cambio en calendarios seccion 1 
    $("#id_vigencia_licencia_conducir").change(function () {
        $(this).attr("readonly", "readonly");
        $("#btns").show();
    });
    //cambio en permanente
    $("#id_permanente").change(function () {
        $(this).attr("readonly", "readonly");
        $("#btns").show();
    });


    //cambio en calendarios seccion 1 
    $(".form-group select").change(function () {
        var hermano = $(this).next();
        var bisabuelo = $(this).next().next();
        bisabuelo.show();
        //alert($("option:selected",this).text());
        hermano.val($("option:selected", this).text());
        $(this).hide();
        hermano.show();
        //$(this).attr("readonly", "readonly");
        //$("#btns_2").show();
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
    //click en boton cancelar seccion1
    $('#btncanDoc').click(function (e) {
        e.preventDefault();
        $("#frm_doc")[0].reset();
        $("#img_curp").hide();
        $("#img_rfc").hide();
        $("#img_sat").hide();
        $("#img_imss").hide();
        $("#img_infonavit").hide();
        $("#img_licrev").hide();
        $("#img_licanv").hide();
        $(".imgcurp").text("Cambiar");
        $(".imgrfc").text("Cambiar");
        $(".imgsat").text("Cambiar");
        $(".imgimss").text("Cambiar");
        $(".imginfonavit").text("Cambiar");
        $(".imglicanv").text("Cambiar");
        $(".imglicrev").text("Cambiar");
        $("#btns").hide();
    });
    $('#data_2 #btncanVis').click(function (e) {
        e.preventDefault();

        var el = $(this)
        var padre = $(this).parent();
        var abuelo = padre.parent();
        var bisabuelo = abuelo.parent();
        form = el.closest('form').get(0);
        form.reset();
        padre.hide();
        img = bisabuelo.find(".imgvisa");
        img.text("Cambiar");
        im = bisabuelo.find("#img_visa");
        im.hide();

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
    
    $('#btnactDoc').click(function (e) {
        e.preventDefault();
        var thisform = $('#frm_doc');
        var actionEndpoint = thisform.attr("action");
        var httpMethod = thisform.attr("method");
        var form = thisform[0];

        var formData = new FormData(form);
        //var formData = $('#frm_doc').serialize();

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
                }
            },
            errors: function (errorData) {
                console.log("error")
                console.log(errorData)
            }

        });

    });




    //cambio en calendarios seccion 1 y 2
    $("#data_2 #id_fecha_vigencia").change(function () {
        var btn = $(this).parent().parent().find("#btns_2")
        btn.show();
        //$(this).attr("readonly", "readonly");
        //$("#btns").show();
    });


    $('#id_vigencia_licencia_conducir').datepicker({
        language: "es",
        todayBtn: "linked",
        keyboardNavigation: false,
        forceParse: false,
        calendarWeeks: true,
        autoclose: true
    });

    $('.form-group #id_fecha_vigencia').datepicker({
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
