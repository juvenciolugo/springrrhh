

function yesnoCheck() {
    if (document.getElementById('inlineRadio1').checked) {
        document.getElementById('visa_1').style.display = 'block';
        $("#id_visa_1").attr("required", true);
        $("#id_vigencia_visa_1").attr("required", true);
        $("#id_vigencia_visa_2").attr("required", false);
        $("#id_vigencia_visa_3").attr("required", false);
        $("#id_vigencia_visa_4").attr("required", false);
        $("#id_vigencia_visa_5").attr("required", false);
        $("#id_visa_2").attr("required", false);
        $("#id_visa_3").attr("required", false);
        $("#id_visa_4").attr("required", false);
        $("#id_visa_5").attr("required", false);
        $("#id_visa_2").val("");
        $("#id_visa_3").val("");
        $("#id_visa_4").val("");
        $("#id_visa_5").val("");
        $("#id_vigencia_visa_2").val("");
        $("#id_vigencia_visa_3").val("");
        $("#id_vigencia_visa_4").val("");
        $("#id_vigencia_visa_5").val("");
        $("#img_vis2").fileinput("clear");
        $("#img_vis3").fileinput("clear");
        $("#img_vis4").fileinput("clear");
        $("#img_vis5").fileinput("clear");
        $("#id_img_visa_1").attr("required", true);
        $("#id_img_visa_2").attr("required", false);
        $("#id_img_visa_3").attr("required", false);
        $("#id_img_visa_4").attr("required", false);
        $("#id_img_visa_5").attr("required", false);
        document.getElementById('visa_2').style.display = 'none';
        document.getElementById('visa_3').style.display = 'none';
        document.getElementById('visa_4').style.display = 'none';
        document.getElementById('visa_5').style.display = 'none';
    }
    else if (document.getElementById('inlineRadio2').checked) {
        document.getElementById('visa_1').style.display = 'block';
        document.getElementById('visa_2').style.display = 'block';
        $("#id_visa_1").attr("required", true);
        $("#id_visa_2").attr("required", true);
        $("#id_visa_3").attr("required", false);
        $("#id_visa_4").attr("required", false);
        $("#id_visa_5").attr("required", false);
        $("#id_vigencia_visa_1").attr("required", true);
        $("#id_vigencia_visa_2").attr("required", true);
        $("#id_vigencia_visa_3").attr("required", false);
        $("#id_vigencia_visa_4").attr("required", false);
        $("#id__vigencia_visa_5").attr("required", false);
        $("#id_visa_3").val("");
        $("#id_visa_4").val("");
        $("#id_visa_5").val("");
        $("#id_vigencia_visa_3").val("");
        $("#id_vigencia_visa_4").val("");
        $("#id_vigencia_visa_5").val("");
        $("#img_vis3").fileinput("clear");
        $("#img_vis4").fileinput("clear");
        $("#img_vis5").fileinput("clear");
        $("#id_img_visa_1").attr("required", true);
        $("#id_img_visa_2").attr("required", true);
        $("#id_img_visa_3").attr("required", false);
        $("#id_img_visa_4").attr("required", false);
        $("#id_img_visa_5").attr("required", false);
        document.getElementById('visa_3').style.display = 'none';
        document.getElementById('visa_4').style.display = 'none';
        document.getElementById('visa_5').style.display = 'none';
    }
    else if (document.getElementById('inlineRadio3').checked) {
        document.getElementById('visa_1').style.display = 'block';
        document.getElementById('visa_2').style.display = 'block';
        document.getElementById('visa_3').style.display = 'block';
        $("#id_visa_1").attr("required", true);
        $("#id_visa_2").attr("required", true);
        $("#id_visa_3").attr("required", true);
        $("#id_visa_4").attr("required", false);
        $("#id_visa_5").attr("required", false);
        $("#id_vigencia_visa_1").attr("required", true);
        $("#id_vigencia_visa_2").attr("required", true);
        $("#id_vigencia_visa_3").attr("required", true);
        $("#id_vigencia_visa_4").attr("required", false);
        $("#id_vigencia_visa_5").attr("required", false);
        $("#id_visa_4").val("");
        $("#id_visa_5").val("");
        $("#id_vigencia_visa_4").val("");
        $("#id_vigencia_visa_5").val("");
        $("#img_vis4").fileinput("clear");
        $("#img_vis5").fileinput("clear");
        $("#id_img_visa_1").attr("required", true);
        $("#id_img_visa_2").attr("required", true);
        $("#id_img_visa_3").attr("required", true);
        $("#id_img_visa_4").attr("required", false);
        $("#id_img_visa_5").attr("required", false);
        document.getElementById('visa_4').style.display = 'none';
        document.getElementById('visa_5').style.display = 'none';
    }
    else if (document.getElementById('inlineRadio4').checked) {
        document.getElementById('visa_1').style.display = 'block';
        document.getElementById('visa_2').style.display = 'block';
        document.getElementById('visa_3').style.display = 'block';
        document.getElementById('visa_4').style.display = 'block';
        $("#id_visa_1").attr("required", true);
        $("#id_visa_2").attr("required", true);
        $("#id_visa_3").attr("required", true);
        $("#id_visa_4").attr("required", true);
        $("#id_visa_5").attr("required", false);
        $("#id_vigencia_visa_1").attr("required", true);
        $("#id_vigencia_visa_2").attr("required", true);
        $("#id_vigencia_visa_3").attr("required", true);
        $("#id_vigencia_visa_4").attr("required", true);
        $("#id_vigencia_visa_5").attr("required", false);
        $("#id_visa_5").val("");
        $("#id_vigencia_visa_5").val("");
        $("#img_vis5").fileinput("clear");
        $("#id_img_visa_1").attr("required", true);
        $("#id_img_visa_2").attr("required", true);
        $("#id_img_visa_3").attr("required", true);
        $("#id_img_visa_4").attr("required", true);
        $("#id_img_visa_5").attr("required", false);
        document.getElementById('visa_5').style.display = 'none';
    }
    else if (document.getElementById('inlineRadio5').checked) {
        document.getElementById('visa_1').style.display = 'block';
        document.getElementById('visa_2').style.display = 'block';
        document.getElementById('visa_3').style.display = 'block';
        document.getElementById('visa_4').style.display = 'block';
        document.getElementById('visa_5').style.display = 'block';
        $("#id_visa_1").attr("required", true);
        $("#id_visa_2").attr("required", true);
        $("#id_visa_3").attr("required", true);
        $("#id_visa_4").attr("required", true);
        $("#id_visa_5").attr("required", true);
        $("#id_vigencia_visa_1").attr("required", true);
        $("#id_vigencia_visa_2").attr("required", true);
        $("#id_vigencia_visa_3").attr("required", true);
        $("#id_vigencia_visa_4").attr("required", true);
        $("#id_vigencia_visa_5").attr("required", true);
        $("#id_img_visa_1").attr("required", true);
        $("#id_img_visa_2").attr("required", true);
        $("#id_img_visa_3").attr("required", true);
        $("#id_img_visa_4").attr("required", true);
        $("#id_img_visa_5").attr("required", true);




    }
    else {
        document.getElementById('visa_1').style.display = 'none';
        document.getElementById('visa_2').style.display = 'none';
        document.getElementById('visa_3').style.display = 'none';
        document.getElementById('visa_4').style.display = 'none';
        document.getElementById('visa_5').style.display = 'none';
        $("#id_visa_1").attr("required", false);
        $("#id_visa_2").attr("required", false);
        $("#id_visa_3").attr("required", false);
        $("#id_visa_4").attr("required", false);
        $("#id_visa_5").attr("required", false);
        $("#id_visa_1").val("");
        $("#id_visa_2").val("");
        $("#id_visa_3").val("");
        $("#id_visa_4").val("");
        $("#id_visa_5").val("");
        $("#id_vigencia_visa_1").val("");
        $("#id_vigencia_visa_2").val("");
        $("#id_vigencia_visa_3").val("");
        $("#id_vigencia_visa_4").val("");
        $("#id_vigencia_visa_5").val("");
        $("#id_vigencia_visa_1").attr("required", false);
        $("#id_vigencia_visa_2").attr("required", false);
        $("#id_vigencia_visa_3").attr("required", false);
        $("#id_vigencia_visa_4").attr("required", false);
        $("#id_vigencia_visa_5").attr("required", false);
        $("#id_img_visa_1").attr("required", false);
        $("#id_img_visa_2").attr("required", false);
        $("#id_img_visa_3").attr("required", false);
        $("#id_img_visa_4").attr("required", false);
        $("#id_img_visa_5").attr("required", false);
        $("#img_vis1").fileinput("clear");
        $("#img_vis2").fileinput("clear");
        $("#img_vis3").fileinput("clear");
        $("#img_vis4").fileinput("clear");
        $("#img_vis5").fileinput("clear");

    }

    if (document.getElementById('inlineRadio8').checked) {
        //$("#licencia").show();
        document.getElementById('licencia').style.display = 'block';
        $("#id_licencia_conducir").attr("required", true);
        $("#id_vigencia_licencia_conducir").attr("required", true);
        $("#id_img_lic_anverso").attr("required", true);
        $("#id_img_lic_reverso").attr("required", true);

    } else {
        document.getElementById('licencia').style.display = 'none';
        $("#id_licencia_conducir").attr("required", false);
        $("#id_vigencia_licencia_conducir").attr("required", false);
        $("#id_img_lic_anverso").attr("required", false);
        $("#id_img_lic_reverso").attr("required", false);
        $("#id_licencia_conducir").val("");
        $("#id_vigencia_licencia_conducir").val("");
        $("#lic_rev").fileinput("clear");
        $("#lic_anv").fileinput("clear");

        //$("#licencia").hide();
    }
};


function ValidaRfc(rfcStr) {
    var strCorrecta;
    rfc=rfcStr.toUpperCase();
    strCorrecta = rfcStr;	
    if (rfcStr.length == 12){
        var valid = '^(([A-Z]|[a-z]){3})([0-9]{6})((([A-Z]|[a-z]|[0-9]){3}))';
    }else{
        var valid = '^(([A-Z]|[a-z]|\s){1})(([A-Z]|[a-z]){3})([0-9]{6})((([A-Z]|[a-z]|[0-9]){3}))';
    }
    var validRfc=new RegExp(valid);
    var matchArray=strCorrecta.match(validRfc);
    padre=$("#id_rfc").parent();
    msg=padre.find(".error");
    if ( msg.length > 0 )
       msg.remove();
    if (matchArray==null) {
        //alert('Formato incorrecto');
        $("<span class='error'> Formato incorrecto </span>").insertAfter("#id_rfc");
        //$("#id_rfc").val("");
        $("#id_rfc").focus();
        //botones_f();
        return false;
    }
    else
    {
        //alert('Cadena correcta:' + strCorrecta);
        
        $("#id_rfc").val(rfc);
        return true;
    }
    };

function ValidaCURP(curp) {
    curp=curp.toUpperCase();
    var re = /^([A-Z][AEIOUX][A-Z]{2}\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])[HM](?:AS|B[CS]|C[CLMSH]|D[FG]|G[TR]|HG|JC|M[CNS]|N[ETL]|OC|PL|Q[TR]|S[PLR]|T[CSL]|VZ|YN|ZS)[B-DF-HJ-NP-TV-Z]{3}[A-Z\d])(\d)$/,
        validado = curp.match(re);
        padre=$("#id_curp").parent();
    msg=padre.find(".error");
    if ( msg.length > 0 )
       msg.remove();
    if (!validado){  //Coincide con el formato general?
      //$("#id_curp").focus();
      //alert('Formato incorrecto');
      $("<span class='error'> Formato incorrecto </span>").insertAfter("#id_curp");
      $("#id_curp").focus();
      //botones_f();
      //$("#id_curp").val("");
      return false;
    } 
    //Validar que coincida el dígito verificador
    if (validado[2] != digitoVerificador(validado[1])) 
      return false;
    
    $("#id_curp").val(curp);
    return true; //Validado
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

    $("#btn_aceptar").click(function (e) {
        padre = $("#id_vigencia_visa_1").parent();
        msg = padre.find(".error");
        if (msg.length > 0) {//si hay error da focus y no submit
            $("#id_vigencia_visa_1").focus();
            e.preventDefault();
        } else {
            padre = $("#id_vigencia_visa_2").parent();
            msg = padre.find(".error");
            if (msg.length > 0) {//si hay error da focus y no submit
                $("#id_vigencia_visa_2").focus();
                e.preventDefault();
            } else {
                padre = $("#id_vigencia_visa_3").parent();
                msg = padre.find(".error");
                if (msg.length > 0) {//si hay error da focus y no submit
                    $("#id_vigencia_visa_3").focus();
                    e.preventDefault();
                }
                else {
                    padre = $("#id_vigencia_visa_4").parent();
                    msg = padre.find(".error");
                    if (msg.length > 0) {//si hay error da focus y no submit
                        $("#id_vigencia_visa_4").focus();
                        e.preventDefault();
                    }
                    else {
                        padre = $("#id_vigencia_visa_5").parent();
                        msg = padre.find(".error");
                        if (msg.length > 0) {//si hay error da focus y no submit
                            $("#id_vigencia_visa_5").focus();
                            e.preventDefault();
                        } else {
                            padre = $("#id_vigencia_licencia_conducir").parent();
                            msg = padre.find(".error");
                            if (msg.length > 0) {//si hay error da focus y no submit
                                $("#id_vigencia_licencia_conducir").focus();
                                e.preventDefault();
                            }else{
                                padre = $("#id_curp").parent();
                                msg = padre.find(".error");
                                if (msg.length > 0) {//si hay error da focus y no submit
                                    $("#id_curp").focus();
                                    e.preventDefault();
                                }else{
                                    padre = $("#id_rfc").parent();
                                    msg = padre.find(".error");
                                    if (msg.length > 0) {//si hay error da focus y no submit
                                        $("#id_rfc").focus();
                                        e.preventDefault();
                                }

                                }

                            }
                        }

                    }
                }
            }
        }
    });



    $("#id_vigencia_licencia_conducir").change(function (e) {
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


    $(".fechas_visa").change(function (e) {
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
    });
    ////////////
    $('form').bind("keypress", function (e) {
        if (e.keyCode == 13) {
            e.preventDefault();
            return false;
        }
    });
    $("#id_rfc").blur(function (e) {
        padre=$(this).parent();
        msg=padre.find(".error");
        if ( msg.length > 0 )
          msg.remove();
        if ($(this).val())
            ValidaRfc($(this).val());
    });
    $("#id_curp").blur(function (e) {
        padre=$(this).parent();
        msg=padre.find(".error");
        if ( msg.length > 0 )
          msg.remove();
        if ($(this).val())
            ValidaCURP($(this).val());
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
                $("<span class='error'> Archivo no válido  </span>").insertAfter(abuelo);
                //abuelo.find('.fileinput-filename').text('');
                this.files[0].name = '';
                this.value = '';

            }
        }


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
