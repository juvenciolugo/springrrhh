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



function edit_idioma(id) {
  $.ajax({
    cache: false,
    url: "/lst-idioma",
    method: "GET",
    data: { "id": id },
    success: function (data) {
      if (data.status == "OK") {
        $("#frm_secdos_edit_idiomas .form-control").limpiaerrors();
        $('#idi_id').val(data.id);
        $('#frm_secdos_edit_idiomas .modal-body').find("#id_idioma").val(data.idioma);
        $('#frm_secdos_edit_idiomas .modal-body').find("#id_idioma_porcentaje").val(data.porcentaje);
        $("#editIdiomaModal").modal('show');
      }
    }
  });
};

function del_estudio(id) {
  $.ajax({
    cache: false,
    url: "/del-estudio",
    method: "GET",
    data: { "id": id },
    success: function (data) {
      if (data.form_is_valid) {
        $("#table_estudios tbody").html(data.html_estudios_lista);
        $("#table_estudios").show();

        $("#myModalLabel").text("¡Estudio eliminado!");
        $("#miModal .modal-body").html("Puedes seguir agregando o guardar sección y continuar");
        $("#miModal").modal('show');
      } else {

        $("<span class='error'>" + data.error + "</span>").insertAfter(elem);
      }
    }
  });
};

function edit_estudio(id) {
  $.ajax({
    cache: false,
    //url: actionEndpoint,
    url: "/lst-estudio",
    method: "GET",
    //data: formData,
    data: { "id": id },
    success: function (data) {
      if (data.status == "OK") {
        $("#frm_secdos_edit_estudios .form-control").limpiaerrors();
        $('#est_id').val(data.id);
        $('#frm_secdos_edit_estudios .modal-body').find("#id_estudios_tipo").val(data.tipo);
        $('#frm_secdos_edit_estudios .modal-body').find("#id_estudios_escuela").val(data.escuela);
        $('#frm_secdos_edit_estudios .modal-body').find("#id_estudios_nombre").val(data.nombre);
        $('#frm_secdos_edit_estudios .modal-body').find("#id_estudios_annios").val(data.annios);
        $('#frm_secdos_edit_estudios .modal-body').find("#id_estudios_inicio").val(data.inicio);
        $('#frm_secdos_edit_estudios .modal-body').find("#id_estudios_termino").val(data.termino);
        $('#frm_secdos_edit_estudios .modal-body').find("#id_estudios_documento").val(data.documento);
        $('#frm_secdos_edit_estudios .modal-body').find("#id_estudios_tesis").val(data.tesis);
        $('#frm_secdos_edit_estudios .modal-body').find("#id_estudios_forma").val(data.forma);
        $('#frm_secdos_edit_estudios .modal-body').find("#id_estudios_cedula").val(data.cedula);
        $("#editEstudioModal").modal('show');
      }
    }
  });
};

function del_otroestudio(id) {
  $.ajax({
    cache: false,
    url: "/del-otroestudio",
    method: "GET",
    data: { "id": id },
    success: function (data) {
      if (data.form_is_valid) {
        $("#table_estudiosotros tbody").html(data.html_estudiosotros_lista);
        $("#table_estudiosotros").show();

        $("#myModalLabel").text("¡Estudio eliminado!");
        $("#miModal .modal-body").html("Puedes seguir agregando o guardar sección y continuar");
        $("#miModal").modal('show');
      } else {

        $("<span class='error'>" + data.error + "</span>").insertAfter(elem);
      }
    }
  });
};

function edit_estudiootro(id) {
  $.ajax({
    cache: false,
    //url: actionEndpoint,
    url: "/lst-otroestudio",
    method: "GET",
    //data: formData,
    data: { "id": id },
    success: function (data) {
      if (data.status == "OK") {
        $("#frm_secdos_edit_estudiosotro .form-control").limpiaerrors();
        $('#estotro_id').val(data.id);
        $('#frm_secdos_edit_estudiosotro .modal-body').find("#id_estudios_tipo").val(data.tipo);
        $('#frm_secdos_edit_estudiosotro .modal-body').find("#id_estudios_nombre").val(data.nombre);
        $('#frm_secdos_edit_estudiosotro .modal-body').find("#id_estudios_inicio").val(data.inicio);
        $('#frm_secdos_edit_estudiosotro .modal-body').find("#id_estudios_termino").val(data.termino);
        $('#frm_secdos_edit_estudiosotro .modal-body').find("#id_estudios_documento").val(data.documento);
        $("#editEstudiootroModal").modal('show');
      }
    }
  });
};

function del_hijo(id) {
  $.ajax({
    cache: false,
    url: "/del-hijo",
    method: "GET",
    data: { "id": id },
    success: function (data) {
      if (data.form_is_valid) {
        $("#table_hijos tbody").html(data.html_hijos_lista);
        $("#table_hijos").show();

        $("#myModalLabel").text("¡Hijo eliminado!");
        $("#miModal .modal-body").html("Puedes seguir agregando o guardar sección y continuar");
        $("#miModal").modal('show');
      } else {

        $("<span class='error'>" + data.error + "</span>").insertAfter(elem);
      }
    }
  });
};

function edit_hijo(id) {
  $.ajax({
    cache: false,
    //url: actionEndpoint,
    url: "/lst-hijo",
    method: "GET",
    //data: formData,
    data: { "id": id },
    success: function (data) {
      if (data.status == "OK") {
        $("#frm_sectres_edit_hijos .form-control").limpiaerrors();
        $('#hijo_id').val(data.id);
        $('#frm_sectres_edit_hijos .modal-body').find("#id_hijo_nombre").val(data.nombre);
        $('#frm_sectres_edit_hijos .modal-body').find("#id_hijo_edad").val(data.edad);
        $('#frm_sectres_edit_hijos .modal-body').find("#id_hijo_ocupacion").val(data.ocupacion);
        $("#editHijoModal").modal('show');
      }
    }
  });
};

function del_hermano(id) {
  $.ajax({
    cache: false,
    url: "/del-hermano",
    method: "GET",
    data: { "id": id },
    success: function (data) {
      if (data.form_is_valid) {
        $("#table_hermanos tbody").html(data.html_hermanos_lista);
        $("#table_hermanos").show();

        $("#myModalLabel").text("¡Hermano eliminado!");
        $("#miModal .modal-body").html("Puedes seguir agregando o guardar sección y continuar");
        $("#miModal").modal('show');
      } else {

        $("<span class='error'>" + data.error + "</span>").insertAfter(elem);
      }
    }
  });
};

function edit_hermano(id) {
  $.ajax({
    cache: false,
    //url: actionEndpoint,
    url: "/lst-hermano",
    method: "GET",
    //data: formData,
    data: { "id": id },
    success: function (data) {
      if (data.status == "OK") {
        $("#frm_sectres_edit_hermanos .form-control").limpiaerrors();
        $('#hermano_id').val(data.id);
        $('#frm_sectres_edit_hermanos .modal-body').find("#id_hermano_nombre").val(data.nombre);
        $('#frm_sectres_edit_hermanos .modal-body').find("#id_hermano_edad").val(data.edad);
        $('#frm_sectres_edit_hermanos .modal-body').find("#id_hermano_ocupacion").val(data.ocupacion);
        $("#editHermanoModal").modal('show');
      }
    }
  });
};

function del_experiencia(id) {
  $.ajax({
    cache: false,
    url: "/del-experiencia",
    method: "GET",
    data: { "id": id },
    success: function (data) {
      if (data.form_is_valid) {
        $("#table_exp tbody").html(data.html_experiencias_lista);
        $("#table_exp").show();

        $("#myModalLabel").text("¡Experiencia eliminada!");
        $("#miModal .modal-body").html("Puedes seguir agregando o guardar sección y continuar");
        $("#miModal").modal('show');
      } else {

        $("<span class='error'>" + data.error + "</span>").insertAfter(elem);
      }
    }
  });
};

function cambia_formato(fec) {
  if (fec) {
    fec = fec.substring(0, 10);
    fec2 = fec.substring(8, 10) + '/' + fec.substring(5, 7) + '/' + fec.substring(0, 4);
    return fec2;
  }
  return ""
}

function edit_experiencia(id) {
  $.ajax({
    cache: false,
    //url: actionEndpoint,
    url: "/lst-experiencia",
    method: "GET",
    //data: formData,
    data: { "id": id },
    success: function (data) {
      if (data.status == "OK") {
        $("#frm_seccinco_edit_exp .form-control").limpiaerrors();
        $('#exp_id').val(data.id);
        $('#frm_seccinco_edit_exp .modal-body').find("#id_empresa_nombre").val(data.nombre);
        $('#frm_seccinco_edit_exp .modal-body').find("#id_empresa_direccion").val(data.direccion);
        $('#frm_seccinco_edit_exp .modal-body').find("#id_empresa_tel").val(data.telefono);
        $('#frm_seccinco_edit_exp .modal-body').find("#id_empresa_giro").val(data.giro);
        $('#frm_seccinco_edit_exp .modal-body').find("#id_empresa_nombre_jefe").val(data.jefe);
        $('#frm_seccinco_edit_exp .modal-body').find("#id_empresa_jefe_puesto").val(data.puesto);
        $('#frm_seccinco_edit_exp .modal-body').find("#id_empresa_fecha_ingreso").val(cambia_formato(data.ingreso));
        $('#frm_seccinco_edit_exp .modal-body').find("#id_empresa_salario_inicio").val(data.salario_inicial);

        $('#frm_seccinco_edit_exp .modal-body').find("#id_empresa_salario_final").val(data.salario_final);
        $('#frm_seccinco_edit_exp .modal-body').find("#id_empresa_puesto_ultimo").val(data.puesto_ultimo);
        $('#frm_seccinco_edit_exp .modal-body').find("#id_empresa_puesto_ultimo_tiempo").val(data.puesto_ultimo_tiempo);
        $('#frm_seccinco_edit_exp .modal-body').find("#id_empresa_puesto_ultimo_depto").val(data.depto_ultimo);
        $('#frm_seccinco_edit_exp .modal-body').find("#id_empresa_puesto_anterior").val(data.puesto_anterior);
        $('#frm_seccinco_edit_exp .modal-body').find("#id_empresa_puesto_anterior_tiempo").val(data.puesto_anterior_tiempo);
        $('#frm_seccinco_edit_exp .modal-body').find("#id_empresa_puesto_anterior_depto").val(data.depto_anterior);
        $('#frm_seccinco_edit_exp .modal-body').find("#id_experiencia_supervision").val(data.exp_supervision);
        if (data.exp_supervision == 'No')
          $('#frm_seccinco_edit_exp .modal-body').find("#id_experiencia_supervision_num").attr('disabled', 'disabled');
        $('#frm_seccinco_edit_exp .modal-body').find("#id_experiencia_supervision_num").val(data.num_supervision);
        if (data.empresa_actual == 'Si') {
          //$('#frm_seccinco_edit_exp .modal-body').find("#id_separacion_motivo").attr('readonly', 'readonly');
          //$('#frm_seccinco_edit_exp .modal-body').find("#id_empresa_fecha_separacion").attr('readonly', 'readonly');
          $("#div_sp2").hide();
          $("#div_fs2").hide();
          $('#frm_seccinco_edit_exp .modal-body').find("#id_separacion_motivo").attr("required", false);
          $('#frm_seccinco_edit_exp .modal-body').find("#id_empresa_fecha_separacion").attr("required", false);
        }
        else {
          //$('#frm_seccinco_edit_exp .modal-body').find("#id_separacion_motivo").removeAttr("readonly");
          //$('#frm_seccinco_edit_exp .modal-body').find("#id_empresa_fecha_separacion").removeAttr("readonly");
          $("#div_sp2").show();
          $("#div_fs2").show();
          $('#frm_seccinco_edit_exp .modal-body').find("#id_separacion_motivo").attr("required", true);
          $('#frm_seccinco_edit_exp .modal-body').find("#id_empresa_fecha_separacion").attr("required", true);
          //$(".exp2 #id_empresa_actual").val("No");
        }
        $('#frm_seccinco_edit_exp .modal-body').find("#id_separacion_motivo").val(data.motivo);
        $('#frm_seccinco_edit_exp .modal-body').find("#id_empresa_fecha_separacion").val(cambia_formato(data.separacion));
        $("#editExpModal").modal('show');
      }
    }
  });
};

function del_referencia(id) {
  $.ajax({
    cache: false,
    url: "/del-referencia",
    method: "GET",
    data: { "id": id },
    success: function (data) {
      if (data.form_is_valid) {
        $("#table_ref tbody").html(data.html_referencias_lista);
        $("#table_ref").show();

        $("#myModalLabel").text("¡Referencia eliminada!");
        $("#miModal .modal-body").html("Puedes seguir agregando o guardar sección y continuar");
        $("#miModal").modal('show');
      } else {

        $("<span class='error'>" + data.error + "</span>").insertAfter(elem);
      }
    }
  });
};

function edit_referencia(id) {
  $.ajax({
    cache: false,
    //url: actionEndpoint,
    url: "/lst-referencia",
    method: "GET",
    //data: formData,
    data: { "id": id },
    success: function (data) {
      if (data.status == "OK") {
        $("#frm_secseis_edit_ref .form-control").limpiaerrors();
        $('#ref_id').val(data.id);
        $('#frm_secseis_edit_ref .modal-body').find("#id_referencia_nombre").val(data.nombre);
        $('#frm_secseis_edit_ref .modal-body').find("#id_referencia_domicilio").val(data.domicilio);
        $('#frm_secseis_edit_ref .modal-body').find("#id_referencia_tel").val(data.telefono);
        $('#frm_secseis_edit_ref .modal-body').find("#id_referencia_ocupacion").val(data.ocupacion);
        $('#frm_secseis_edit_ref .modal-body').find("#id_referencia_annios_conocer").val(data.annios);
        $("#editRefModal").modal('show');
      }
    }
  });
};



function ValidaRfc(rfcStr) {
  var strCorrecta;
  rfc = rfcStr.toUpperCase();
  strCorrecta = rfcStr;
  if (rfcStr.length == 12) {
    var valid = '^(([A-Z]|[a-z]){3})([0-9]{6})((([A-Z]|[a-z]|[0-9]){3}))';
  } else {
    var valid = '^(([A-Z]|[a-z]|\s){1})(([A-Z]|[a-z]){3})([0-9]{6})((([A-Z]|[a-z]|[0-9]){3}))';
  }
  var validRfc = new RegExp(valid);
  var matchArray = strCorrecta.match(validRfc);
  padre = $("#id_rfc").parent();
  msg = padre.find(".error");
  if (msg.length > 0)
    msg.remove();
  if (matchArray == null) {
    //alert('Formato incorrecto');
    $("<span class='error'> Formato incorrecto </span>").insertAfter("#id_rfc");
    //$("#id_rfc").val("");
    $("#id_rfc").focus();
    //botones_f();
    return false;
  }
  else {
    //alert('Cadena correcta:' + strCorrecta);

    $("#id_rfc").val(rfc);
    return true;
  }
};



function digitoVerificador(curp17) {
  //Fuente https://consultas.curp.gob.mx/CurpSP/
  var diccionario = "0123456789ABCDEFGHIJKLMNÑOPQRSTUVWXYZ",
    lngSuma = 0.0,
    lngDigito = 0.0;
  for (var i = 0; i < 17; i++)
    lngSuma = lngSuma + diccionario.indexOf(curp17.charAt(i)) * (18 - i);
  lngDigito = 10 - lngSuma % 10;
  if (lngDigito == 10) return 0;
  return lngDigito;
};

function ValidaCURP(curp) {
  curp = curp.toUpperCase();
  var re = /^([A-Z][AEIOUX][A-Z]{2}\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])[HM](?:AS|B[CS]|C[CLMSH]|D[FG]|G[TR]|HG|JC|M[CNS]|N[ETL]|OC|PL|Q[TR]|S[PLR]|T[CSL]|VZ|YN|ZS)[B-DF-HJ-NP-TV-Z]{3}[A-Z\d])(\d)$/,
    validado = curp.match(re);
  padre = $("#id_curp").parent();
  msg = padre.find(".error");
  if (msg.length > 0)
    msg.remove();
  if (!validado) {  //Coincide con el formato general?
    //$("#id_curp").focus();
    //alert('Formato incorrecto');
    $("<span class='error'> Formato incorrecto </span>").insertAfter("#id_curp");
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



function soloNumeros(e) {
  key = e.keyCode || e.which;
  tecla = String.fromCharCode(key).toLowerCase();
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
    return false;
  }
};
function soloLetras(e) {
  key = e.keyCode || e.which;
  tecla = String.fromCharCode(key).toLowerCase();
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
    return false;
  }
};

function soloLetrasyNumeros(e) {
  key = e.keyCode || e.which;
  tecla = String.fromCharCode(key).toLowerCase();
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
};

function ValidaEmail(elem) {
  var input = elem.val();
  var pattern = /^\b[A-Z0-9._%-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b$/i
  if (!pattern.test(input)) {
    return false;
  }
  return true;
};
////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//var status_con="{{ status_con }}";
function anularBotonDerecho(e) {


  if (navigator.appName == 'Netscape'
    && (e.which == 3 || e.which == 2)) {
    alert(sMensaje);
    return false;
  } else if (navigator.appName == 'Microsoft Internet Explorer'
    && (event.button == 2)) {
    alert(sMensaje);
  }
}
$(document).ready(function () {
  
  if (localStorage['aviso']=='True'){
      //localStorage.removeItem("aviso");
  }
  else{
    $("#myModalLabel").text("¡Aviso!");
    $("#miModal .modal-body").html("No puedes capturar la solicitud sin antes aceptar el aviso de privacidad");
    $("#miModal").modal('show');
    setTimeout(function () {
      window.location.href = "/candidato/";
    }, 3000);
    event.preventDefault();

  }
    
  

  //document.onmousedown = anularBotonDerecho;
  //document.oncontextmenu = new Function("return false");


  var form_valid = "false";
  var status_con = document.getElementById("status_con").innerHTML;
  //var con_id = document.getElementById("id_con_id").innerHTML;
  var con_id = $("#id_con_id").val();
  var status = 5;
  var msg_fec = "hola";


  if (status_con == 'True') {
    $("#frm_secuno :input").each(function () {
      if ($(this).val() != '') {
        if ($(this).attr('id') != 'id_edad')
          $(this).removeAttr("disabled");
      }
    });
    $("#frm_secdos :input").each(function () {
      if ((($(this).attr('id') == 'id_primaria_documento') && ($("#id_primaria_annios").val() != '')) ||
        (($(this).attr('id') == 'id_secundaria_documento') && ($("#id_secundaria_annios").val() != '')) ||
        (($(this).attr('id') == 'id_preparatoria_documento') && ($("#id_preparatoria_annios").val() != '')) ||
        (($(this).attr('id') == 'id_tecnica_documento') && ($("#id_tecnica_annios").val() != '')))
        $(this).removeAttr("disabled");
      else if (($(this).val() != '') && ($(this).attr('id') != 'id_primaria_documento') &&
        ($(this).attr('id') != 'id_secundaria_documento') &&
        ($(this).attr('id') != 'id_preparatoria_documento') &&
        ($(this).attr('id') != 'id_tecnica_documento'))
        $(this).removeAttr("disabled");
    });


    $("#frm_seccuatro :input").each(function () {
      if ($(this).val() != '') {
        $(this).removeAttr("disabled");
      }
    });
    //alert(con_id);
    $("#con_id").val(con_id);
    $("#candId2").val(con_id);
    $("#candId2_idi").val(con_id);
    $("#candId_editidioma").val(con_id);
    $("#candId2_est").val(con_id);
    $("#candId2_estotro").val(con_id);

    $("#candId3").val(con_id);
    $("#candId3_hijo").val(con_id);
    $("#candId_edithijo").val(con_id);
    $("#candId3_hermano").val(con_id);
    $("#candId_edithermano").val(con_id);
    $("#candId4").val(con_id);
    $("#candId5").val(con_id);
    $("#candId6").val(con_id);
    $("#pnl_sec2").toggle(500);
    $("#pnl_sec3").toggle(500);
    $("#pnl_sec4").toggle(500);
    $("#pnl_sec5").toggle(500);
    $("#pnl_sec6").toggle(500);


  };

  $("#id_tipo_licencia").change(function () {
    if ($(this).val() == 5) {
      $("#id_licencia").val("")
      $("#nlic").hide();
    }
    else
      $("#nlic").show();
  });

  $(".exp #id_empresa_actual").change(function () {
    if ($(".exp #id_empresa_actual").val() == "Si") {
      $("#div_sp").hide();
      $("#div_fs").hide();
      $('#frm_seccinco_add_exp .modal-body').find("#id_separacion_motivo").attr("required", false);
      $('#frm_seccinco_add_exp .modal-body').find("#id_empresa_fecha_separacion").attr("required", false);
      $('#frm_seccinco_add_exp .modal-body').find("#id_separacion_motivo").val("");
      $('#frm_seccinco_add_exp .modal-body').find("#id_empresa_fecha_separacion").val("");
    } else {
      $("#div_sp").show();
      $("#div_fs").show();
      $('#frm_seccinco_add_exp .modal-body').find("#id_separacion_motivo").attr("required", true);
      $('#frm_seccinco_add_exp .modal-body').find("#id_empresa_fecha_separacion").attr("required", true);
    }
  });

  $(".exp2 #id_empresa_actual").change(function () {
    if ($(".exp2 #id_empresa_actual").val() == "Si") {
      $("#div_sp2").hide();
      $("#div_fs2").hide();
      $('#frm_seccinco_edit_exp .modal-body').find("#id_separacion_motivo").attr("required", false);
      $('#frm_seccinco_edit_exp .modal-body').find("#id_empresa_fecha_separacion").attr("required", false);
      $('#frm_seccinco_edit_exp .modal-body').find("#id_separacion_motivo").val("");
      $('#frm_seccinco_edit_exp .modal-body').find("#id_empresa_fecha_separacion").val("");
    } else {
      $("#div_sp2").show();
      $("#div_fs2").show();
      $('#frm_seccinco_edit_exp .modal-body').find("#id_separacion_motivo").attr("required", true);
      $('#frm_seccinco_edit_exp .modal-body').find("#id_empresa_fecha_separacion").attr("required", true);
    }
  });



  $("#id_email_personal").change(function (e) {
    //e.preventDefault();
    padre = $(this).parent().parent();
    msg = padre.find(".error");
    if (msg.length > 0)
      msg.remove();
    if ($(this).val() != '') {
      if (!ValidaEmail($(this))) {
        $("<span class='error'> Esto no es correo  </span>").insertAfter("#email");
        $(this).focus();
      };
    }
  });




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
      del_idioma(id);
    else if (reg == "HIJO")
      del_hijo(id);
    else if (reg == "HERMANO")
      del_hermano(id);
    else if (reg == "EXP")
      del_experiencia(id);
    else if (reg == "REF")
      del_referencia(id);
    else if (reg == "ESTUDIO")
      del_estudio(id);
    else if (reg == "ESTUDIOOTRO")
      del_otroestudio(id);

  });

  function del_idioma(id) {
    //abir modal y confirmar

    $.ajax({
      cache: false,
      url: "/del-idioma",
      method: "GET",
      data: { "id": id },
      success: function (data) {
        if (data.form_is_valid) {
          $("#table_idiomas tbody").html(data.html_idiomas_lista);
          $("#table_idiomas").show();

          $("#myModalLabel").text("¡Idioma eliminado!");
          $("#miModal .modal-body").html("Puedes seguir agregando o guardar sección y continuar");
          $("#miModal").modal('show');
        } else {

          $("<span class='error'>" + data.error + "</span>").insertAfter(elem);
        }
      }
    });

  };

  // calendarios
  $('.input-group.date.normal').datepicker({
    language: "es",
    todayBtn: "linked",
    keyboardNavigation: false,
    forceParse: false,
    calendarWeeks: true,
    dateFormat: 'dd/mm/yy',
    autoclose: true
  });

  $('.input-group.date.inicio , .input-group.date.termino').datepicker({
    format: "yyyy",
    viewMode: "years",
    minViewMode: "years",
    autoclose: true,
    enableOnReadonly: false

  });

  $(".sololetras").keypress(function (e) {
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

  $("#id_idioma_porcentaje").keypress(function (e) {
    key = e.keyCode || e.which;
    tecla = String.fromCharCode(key).toLowerCase();
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
      //alert("tecla no permitida");
      return false;
    } else {
      valor = tecla + $("#id_idioma_porcentaje").val();
      valor = parseInt(valor);
      if (valor > 100) {
        padre = $(this).parent();
        msg = padre.find(".error");
        if (msg.length > 0)
          msg.remove();
        $(this).val("");
        $("<span class='error'> Porcentaje mayor a 100 </span>").insertAfter($(this));
        return false;
      }

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
    if (hoy < fechaFormulario) {
      msg_fec = "Fecha posterior a la actual";
      //$("#id_edad").val("");
      //botones_f();
      return false;
    } else {
      //alert("es menor");
      return true;
    }

  };

  $(".year").change(function (e) {
    e.preventDefault();
    padre = $(this).parent();
    msg = padre.find(".error");
    if (msg.length > 0)
      msg.remove();
    if (!annio_mayor($(this).val())) {
      $(this).focus();
      $("<span class='error'>" + msg_fec + "</span>").insertAfter($(this));
    }

  });

  function annio_mayor(dtVal) {
    msg_fec = ""
    //investigar si es mayor al año actual
    var hoy = new Date();
    if (hoy.getFullYear() < dtVal) {
      msg_fec = "Año posterior a la actual";
      return false;
    } else {
      //alert("es menor");
      return true;
    }

  };

  function fecha_menor(dtVal) {
    msg_fec = ""
    //investigar si es menor a la actual
    var hoy = new Date();
    //var fechaFormulario = dtVal;
    // Comparamos solo las fechas => no las horas!!
    hoy.setHours(0, 0, 0, 0);  // Lo iniciamos a 00:00 horas
    //convertir a fecha
    var annio = dtVal.substring(6, 10);
    var mes = dtVal.substring(3, 5);
    var dia = dtVal.substring(0, 2);
    var fechaFormulario = new Date(annio, mes - 1, dia);
    if (hoy > fechaFormulario) {
      msg_fec = "Fecha anterior a la actual";
      //$("#id_edad").val("");
      //botones_f();
      return false;
    } else {
      //alert("es mayor");
      return true;
    }

  };


  $("#id_fecha_nac").change(function (e) {
    e.preventDefault();
    var dtVal = $("#id_fecha_nac").val();
    if (true) {
      padre = $(this).parent();
      msg = padre.find(".error");
      if (msg.length > 0)
        msg.remove();
      //botones_t();
      //verifica si tiene formato válido
      if (ValidateDate(dtVal)) {
        //console.log("verifico Validate true");
        //si tiene formato válido verifica si no es mayor a la fecha actual,
        //if ( (elem.attr('id')!= "id_fecha_disponible")&&(elem.attr('id')!= "id_estudia_termino") ){     
        if (fecha_mayor(dtVal)) {

          //verificar si e smayo de edad
          var edad = obten_edad($("#id_fecha_nac").val());
          $("#id_edad").val(edad);

          if (edad >= 15) {
            $("#id_edad").val(edad);
          } else {
            $("<span class='error'> Debe ser mayor de 14 años</span>").insertAfter($(this));
            //botones_f();
          }
        } else {
          // console.log("entro a false");
          $("#id_fecha_nac").focus();
          $("<span class='error'>" + msg_fec + "</span>").insertAfter($(this));
          //botones_f();
        }
      } else {
        //console.log("verifico Validate false");
        $("<span class='error'>" + msg_fec + "</span>").insertAfter($(this));
        //$(this).focus();
        //botones_f();
      }
    }
  });

  $("#id_fecha_nac").on("close", function () {
    this.focus();
  });
  $(".year").on("close", function () {
    this.focus();
  });




  $("#fec_ter,#fec_dis").change(function (e) {
    var dtVal = $(this).val();
    padre = $(this).parent();
    msg = padre.find(".error");
    if (msg.length > 0)
      msg.remove();
    //botones_t();
    if (ValidateDate(dtVal)) {
      if (fecha_menor(dtVal)) {

      } else {
        $("<span class='error'>" + msg_fec + "</span>").insertAfter($(this));
        //botones_f();
      }
    } else {
      //console.log("verifico Validate false");
      $("<span class='error'>" + msg_fec + "</span>").insertAfter($(this));
      //botones_f();
    }
  });

  $("#id_empresa_fecha_ingreso,#id_empresa_fecha_separacion").change(function (e) {
    var dtVal = $(this).val();
    padre = $(this).parent();
    msg = padre.find(".error");
    if (msg.length > 0)
      msg.remove();
    //botones_t();
    if (ValidateDate(dtVal)) {
      if (fecha_mayor(dtVal)) {

      } else {
        $("<span class='error'>" + msg_fec + "</span>").insertAfter($(this));
        //botones_f();
      }
    } else {
      //console.log("verifico Validate false");
      $("<span class='error'>" + msg_fec + "</span>").insertAfter($(this));
      //botones_f();
    }
  });


  $(':input').on('drop', function (event) {
    event.preventDefault();
  });

  $(":input").on('paste', function (e) {
    e.preventDefault();
  });

  $(":input").on('copy', function (e) {
    e.preventDefault();
  });

  $(":input").on('change', function (e) {
    if (($(this).attr('id') != "fec_ter") && ($(this).attr('id') != "fec_dis") && ($(this).attr('id') != "id_fecha_nac") && (!$(this).hasClass('inicio')) && (!$(this).hasClass('termino')) && ($(this).attr('id') != "id_empresa_fecha_ingreso") && ($(this).attr('id') != "id_empresa_fecha_separacion") &&
      ($(this).attr('id') != "id_primaria_inicio") && ($(this).attr('id') != "id_primaria_termino") &&
      ($(this).attr('id') != "id_secundaria_inicio") && ($(this).attr('id') != "id_secundaria_termino") &&
      ($(this).attr('id') != "id_preparatoria_inicio") && ($(this).attr('id') != "id_preparatoria_termino") &&
      ($(this).attr('id') != "id_tecnica_inicio") && ($(this).attr('id') != "id_tecnica_termino") &&
      ($(this).attr('id') != "id_estudios_inicio") && ($(this).attr('id') != "id_estudios_termino")) {
      padre = $(this).parent();
      msg = padre.find(".error");
      if (msg.length > 0)
        msg.remove();
      e.preventDefault();
    }

  });

  function requeridos_uno(id) {
    var myArr = ['id_fuente_recluta', 'id_puesto_solicitado', 'id_sueldo_deseado', 'id_nombre', 'id_apellido_paterno', 'id_apellido_materno',
      'id_edad', 'id_fecha_nac', 'id_lugar_nac', 'id_pais_nacimiento', 'id_cel', 'id_tipo', 'id_calle', 'id_num_ext',
      'id_calle_uno', 'id_calle_dos', 'id_cp', 'id_colonia', 'id_referencia', 'id_trayectoria_de_casa',
      'id_tipo_licencia'];
    if (myArr.includes(id)) {
      return true;
    }
    else
      return false;
  }

  $.fn.getValidationUno = function () {
    var message = "";
    var name = "";
    form_valid = "true";
    this.each(function () {
      name = this.id;
      //if ((this.checkValidity() == false) &&  (requeridos(this.attr('id')))) {
      if ((requeridos_uno(this.id)) && (this.value == '')) {
        padre = $("#" + name).parent();
        msg = padre.find(".error");
        if (msg.length > 0)
          msg.remove();
        form_valid = "false";
        $("<span class='error'>" + "Completa este campo" + "</span>").insertAfter($("#" + name));
        $("#" + name).focus();
        return false;
      } else {//campo valido
        if ((name == "id_fecha_nac") || (name == "id_curp") || (name == "id_rfc") || (name == "id_email_personal")) {
          if (name != "id_email_personal") {
            padre = $("#" + name).parent();
            msg = padre.find(".error");
            if (msg.length > 0) {//si existe error en fecha curp o rfc
              form_valid = "false";
              $("#" + name).focus();
              return false;
            }
          } else {
            padre = $("#" + name).parent().parent();
            msg = padre.find(".error");
            if (msg.length > 0) {//si existe error en email
              form_valid = "false";
              $("#" + name).focus();
              return false;
            }

          }
        }

      }
    })
  };

  $("#btn_sec1").click(function () {
    $("#frm_secuno .form-control").getValidationUno();
    if (form_valid == "true")
      $("#frm_secuno").submit();
  });



  $('#frm_secuno').submit(function (event) {
    event.preventDefault();
    var thisform = $(this);
    var actionEndpoint = thisform.attr("action");
    var httpMethod = thisform.attr("method");
    var formData = $('#frm_secuno').serialize();


    $.ajax({
      cache: false,
      url: actionEndpoint,
      method: httpMethod,
      data: formData,
      success: function (data) {
        if (data.result == "OK") {
          //alert(data.id);
          status = 1;
          $("#id_n").val(data.id);
          $("#candId2").val(data.id);
          $("#candId2_idi").val(data.id);
          $("#candId2_est").val(data.id);
          $("#candId2_estotro").val(data.id);
          $("#candId_editidioma").val(data.id);


          $("#candId3").val(data.id);
          $("#candId3_hijo").val(data.id);
          $("#candId3_hermano").val(data.id);
          $("#candId4").val(data.id);
          $("#candId5").val(data.id);
          $("#candId6").val(data.id);
          //$("#ok").show().fadeOut(5000);
          $("#myModalLabel").text("¡Sección datos personales guardada!");
          $("#miModal .modal-body").html("Por favor continúa con la siguiente sección");
          $("#miModal").modal('show');
          $("#pnl_sec2").show();
          //$("#pnl_sec1").toggle(500);

          //$("#btn_sec1").hide();
          //$("#btn_sec1_act").show();
          // $("#add_PerModal").modal('hide');
          // location.reload();
        } else if (data.result == "passerror") {
          // $("#pass").show().fadeOut(3000);
        } else if (data.result == "user_existe") {
          // $("#user_existe").show().fadeOut(3000);
        } else if (data.result == "email_existe") {
          // $("#email_existe").show().fadeOut(3000); 
        } else if (data.result == 'errores') {
          //alert(data.message);
          $("#p_msg").text(data.message);
          $("#p_msg").show();

        }
        console.log("success")
        console.log(data)

      },
      errors: function (errorData) {
        console.log("error")
        console.log(errorData)
      }

    });

  });



  $.fn.getValidationDos = function () {
    var message = "";
    var name = "";
    form_valid = "true";
    this.each(function () {
      name = this.id;
      if (this.checkValidity() == false) {
        padre = $("#" + name).parent();
        msg = padre.find(".error");
        if (msg.length > 0)
          msg.remove();
        form_valid = "false";
        $("<span class='error'>" + "Completa este campo" + "</span>").insertAfter($("#" + name));
        $("#" + name).focus();
        return false;
      } else {//campo valido
        //.input-group.date .inicio

        /*if( ($("#"+name).hasClass('inicio'))||($("#"+name).hasClass('termino'))){
          padre=$("#"+name).parent();
          msg=padre.find(".error");
          if ( msg.length > 0 ){//si existe error en fecha dejar
            form_valid="false";
            $("#"+name).focus();
            return false;
          }
        }*/

      }
    })
  };

  $("#btn_sec2").click(function () {
    $("#frm_secdos .form-control").getValidationDos();
    if (form_valid == "true")
      $("#frm_secdos").submit();
  });

  $('#frm_secdos').submit(function (event) {
    //$("#p_msg2").hide();
    event.preventDefault();
    var thisform = $("#frm_secdos");
    var actionEndpoint = thisform.attr("action");
    var httpMethod = thisform.attr("method");
    var formData = $(thisform).serialize();

    $.ajax({
      cache: false,
      url: actionEndpoint,
      method: httpMethod,
      data: formData,
      success: function (data) {
        if (data.result == "OK") {
          status = 2;
          // $("#ok2").show().fadeOut(5000);
          $("#myModalLabel").text("¡Sección antecedentes académicos guardada!");
          $("#miModal .modal-body").html("Por favor continúa con la siguiente sección");
          $("#miModal").modal('show');
          $("#pnl_sec3").show();
          //$("#pnl_sec2").toggle(500);

          //$("#btn_sec2").hide();
          //$("#btn_sec2_act").show();
          // $("#add_PerModal").modal('hide');
          // location.reload();
        } else if (data.result == "passerror") {
          // $("#pass").show().fadeOut(3000);
        } else if (data.result == "user_existe") {
          // $("#user_existe").show().fadeOut(3000);
        } else if (data.result == "email_existe") {
          // $("#email_existe").show().fadeOut(3000); 
        } else if (data.result == 'errores') {
          //alert(data.message);
          $("#p_msg2").text(data.message);
          $("#p_msg2").show();
        }
        console.log("success")
        console.log(data)
      },
      errors: function (errorData) {
        console.log("error")
        console.log(errorData)
      }
    });

  });

  $.fn.getValidationTres = function () {
    var message = "";
    var name = "";
    form_valid = "true";
    this.each(function () {
      name = this.id;
      if (this.checkValidity() == false) {
        padre = $("#" + name).parent();
        msg = padre.find(".error");
        if (msg.length > 0)
          msg.remove();
        form_valid = "false";
        $("<span class='error'>" + "Completa este campo" + "</span>").insertAfter($("#" + name));
        $("#" + name).focus();
        return false;
      } else {//campo valido
        //.input-group.date .inicio

        if (($("#" + name).hasClass('inicio')) || ($("#" + name).hasClass('termino'))) {
          padre = $("#" + name).parent();
          msg = padre.find(".error");
          if (msg.length > 0) {//si existe error en fecha dejar
            form_valid = "false";
            $("#" + name).focus();
            return false;
          }
        }

      }
    })
  };


  $("#btn_sec3").click(function (event) {
    // $("#p_msg3").hide();
    event.preventDefault();
    var thisform = $("#frm_sectres");
    var actionEndpoint = thisform.attr("action");
    var httpMethod = thisform.attr("method");
    var formData = $('#frm_sectres').serialize();


    $.ajax({
      cache: false,
      url: actionEndpoint,
      method: httpMethod,
      data: formData,
      success: function (data) {
        if (data.result == "OK") {
          status = 3;
          //$("#ok3").show().fadeOut(5000);
          $("#myModalLabel").text("¡Sección datos familiares guardada!");
          $("#miModal .modal-body").html("Por favor continúa con la siguiente sección");
          $("#miModal").modal('show');
          $("#pnl_sec4").show();
          //$("#pnl_sec3").toggle(500);

          //$("#btn_sec3").hide();
          //$("#btn_sec3_act").show();
          // $("#add_PerModal").modal('hide');
          // location.reload();
        } else if (data.result == "passerror") {
          // $("#pass").show().fadeOut(3000);
        } else if (data.result == "user_existe") {
          // $("#user_existe").show().fadeOut(3000);
        } else if (data.result == "email_existe") {
          // $("#email_existe").show().fadeOut(3000); 
        } else if (data.result == 'errores') {
          //alert(data.message);
          $("#p_msg3").text(data.message);
          $("#p_msg3").show();

        }
        console.log("success")
        console.log(data)
      },
      errors: function (errorData) {
        console.log("error")
        console.log(errorData)
      }
    });
  });



  $.fn.getValidationCuatro = function () {
    var message = "";
    var name = "";
    form_valid = "true";
    this.each(function () {
      name = this.id;
      if (this.checkValidity() == false) {
        padre = $("#" + name).parent();
        msg = padre.find(".error");
        if (msg.length > 0)
          msg.remove();
        form_valid = "false";
        $("<span class='error'>" + "Completa este campo" + "</span>").insertAfter($("#" + name));
        $("#" + name).focus();
        return false;
      } else {//campo valido
        if ((name == "fec_dis")) {
          padre = $("#" + name).parent();
          msg = padre.find(".error");
          if (msg.length > 0) {//si existe error en fecha dejar
            form_valid = "false";
            $("#" + name).focus();
            return false;
          }
        }

      }
    })
  };

  $("#btn_sec4").click(function () {
    $("#frm_seccuatro .form-control").getValidationCuatro();
    if (form_valid == "true")
      $("#frm_seccuatro").submit();
  });

  $('#frm_seccuatro').submit(function (event) {
    //$("#p_msg4").hide();
    event.preventDefault();
    var thisform = $(this);
    var actionEndpoint = thisform.attr("action");
    var httpMethod = thisform.attr("method");
    var formData = $('#frm_seccuatro').serialize();


    $.ajax({
      cache: false,
      url: actionEndpoint,
      method: httpMethod,
      data: formData,
      success: function (data) {
        if (data.result == "OK") {
          status = 4;
          //$("#ok4").show().fadeOut(5000);
          $("#myModalLabel").text("¡Sección datos generales guardada!");
          $("#miModal .modal-body").html("Por favor continúa con la siguiente sección");
          $("#miModal").modal('show');
          $("#pnl_sec5").show();
          // $("#pnl_sec4").toggle(500);

          // $("#btn_sec4").hide();
          // $("#btn_sec4_act").show();
          // $("#add_PerModal").modal('hide');
          // location.reload();
        } else if (data.result == "passerror") {
          // $("#pass").show().fadeOut(3000);
        } else if (data.result == "user_existe") {
          // $("#user_existe").show().fadeOut(3000);
        } else if (data.result == "email_existe") {
          // $("#email_existe").show().fadeOut(3000); 
        } else if (data.result == 'errores') {
          //alert(data.message);
          $("#p_msg4").text(data.message);
          $("#p_msg4").show();

        }
        console.log("success")
        console.log(data)

      },
      errors: function (errorData) {
        console.log("error")
        console.log(errorData)
      }

    });

  });

  $('#agregar_hijo').click(function () {
    elem = $('#frm_sectres_hijos .modal-body').find("#id_hijo_nombre");
    padre = elem.parent();
    msg = padre.find(".error");
    if (msg.length > 0)
      msg.remove();
    $("#frm_sectres_hijos .form-control").limpiaerrors();
    $("#frm_sectres_hijos")[0].reset();
    $("#addHijoModal").modal('show');
  });

  $.fn.getValidationeditHijo = function () {
    var message = "";
    var name = "";
    form_valid = "true";
    this.each(function () {
      name = this.id;
      if (this.checkValidity() == false) {
        elem = "#frm_sectres_edit_hijos #" + name;
        padre = $(elem).parent();
        msg = padre.find(".error");
        if (msg.length > 0)
          msg.remove();
        form_valid = "false";
        //elem="#frm_sectres_edit_hijos #"+name;
        $("<span class='error'>" + "Completa este campo" + "</span>").insertAfter($(elem));
        $(elem).focus();
        return false;
      } else {//campo valido

      }
    })
  };

  $("#btn_edit_hijo").click(function () {
    $("#frm_sectres_edit_hijos .form-control").getValidationeditHijo();
    if (form_valid == "true")
      $("#frm_sectres_edit_hijos").submit();
  });


  //Seccion 3 editar HIJO

  $('#frm_sectres_edit_hijos').submit(function (event) {
    elem = $('#frm_sectres_edit_hijos .modal-body').find("#id_hijo_nombre");
    padre = elem.parent();
    msg = padre.find(".error");
    if (msg.length > 0)
      msg.remove();
    event.preventDefault();
    var thisform = $(this);
    var actionEndpoint = thisform.attr("action");
    var httpMethod = thisform.attr("method");
    var formData = $('#frm_sectres_edit_hijos').serialize();

    //////Llamado AJAX
    $.ajax({
      cache: false,
      url: actionEndpoint,
      method: httpMethod,
      data: formData,
      success: function (data) {
        if (data.form_is_valid) {
          //var idi_id=data.id
          $("#editHijoModal").modal('hide');
          $("#table_hijos tbody").html(data.html_hijos_lista);
          $("#table_hijos").show();
          $("#myModalLabel").text("¡Hijo actualizado!");
          $("#miModal .modal-body").html("Puedes seguir agregando o guardar sección y continuar");
          $("#miModal").modal('show');
        } else {

          $("<span class='error'>" + data.error + "</span>").insertAfter(elem);
        }

      }
    });

  });

  $.fn.getValidationHijo = function () {
    var message = "";
    var name = "";
    form_valid = "true";
    this.each(function () {
      name = this.id;
      if (this.checkValidity() == false) {
        elem = "#frm_sectres_hijos #" + name;
        padre = $(elem).parent();
        msg = padre.find(".error");
        if (msg.length > 0)
          msg.remove();
        form_valid = "false";
        //elem="#frm_sectres_hijos #"+name;
        $("<span class='error'>" + "Completa este campo" + "</span>").insertAfter($(elem));
        $(elem).focus();
        return false;
      } else {//campo valido

      }
    })
  };

  $("#btn_add_hijo").click(function () {
    $("#frm_sectres_hijos .form-control").getValidationHijo();
    if (form_valid == "true")
      $("#frm_sectres_hijos").submit();
  });

  //agregar hijo
  $('#frm_sectres_hijos').submit(function (event) {
    elem = $('#frm_sectres_hijos .modal-body').find("#id_hijo_nombre");
    padre = elem.parent();
    msg = padre.find(".error");
    if (msg.length > 0)
      msg.remove();
    //$("#p_msg5").hide();
    event.preventDefault();
    var thisform = $(this);
    var actionEndpoint = thisform.attr("action");
    var httpMethod = thisform.attr("method");
    var formData = $('#frm_sectres_hijos').serialize();

    nom = $("#id_hijo_nombre").val()

    pat = $("#id_hijo_apellido_paterno").val()

    mat = $("#id_hijo_apellido_materno").val()

    ///////Llamado AJAX
    $.ajax({
      cache: false,
      url: actionEndpoint,
      method: httpMethod,
      data: formData,
      success: function (data) {
        if (data.form_is_valid) {
          $("#addHijoModal").modal('hide');
          $("#table_hijos tbody").html(data.html_hijos_lista);
          $("#table_hijos").show();
          //alert("Hijo Guardado");
          $("#myModalLabel").text("¡Hijo agregado!");
          $("#miModal .modal-body").html("Puedes seguir agregando o guardar sección y continuar");
          $("#miModal").modal('show');
        } else {
          $("<span class='error'>" + data.error + "</span>").insertAfter(elem);
        }

      }
    });

  });

  $('#agregar_hermano').click(function () {
    elem = $('#frm_sectres_hermanos .modal-body').find("#id_hermano_nombre");
    padre = elem.parent();
    msg = padre.find(".error");
    if (msg.length > 0)
      msg.remove();
    $("#frm_sectres_hermanos .form-control").limpiaerrors();
    $("#frm_sectres_hermanos")[0].reset();
    $("#addHermanoModal").modal('show');
  });

  $.fn.getValidationeditHer = function () {
    var message = "";
    var name = "";
    form_valid = "true";
    this.each(function () {
      name = this.id;
      if (this.checkValidity() == false) {
        elem = "#frm_sectres_edit_hermanos #" + name;
        padre = $(elem).parent();
        msg = padre.find(".error");
        if (msg.length > 0)
          msg.remove();
        form_valid = "false";
        //elem="#frm_sectres_edit_hermanos #"+name;
        $("<span class='error'>" + "Completa este campo" + "</span>").insertAfter($(elem));
        $(elem).focus();
        return false;
      } else {//campo valido

      }
    })
  };

  $("#btn_edit_her").click(function () {
    $("#frm_sectres_edit_hermanos .form-control").getValidationeditHer();
    if (form_valid == "true")
      $("#frm_sectres_edit_hermanos").submit();
  });

  //Seccion 3 editar HERMANO

  $('#frm_sectres_edit_hermanos').submit(function (event) {
    elem = $('#frm_sectres_edit_hermanos .modal-body').find("#id_hermano_nombre");
    padre = elem.parent();
    msg = padre.find(".error");
    if (msg.length > 0)
      msg.remove();
    event.preventDefault();
    var thisform = $(this);
    var actionEndpoint = thisform.attr("action");
    var httpMethod = thisform.attr("method");
    var formData = $('#frm_sectres_edit_hermanos').serialize();

    //////Llamado AJAX
    $.ajax({
      cache: false,
      url: actionEndpoint,
      method: httpMethod,
      data: formData,
      success: function (data) {
        if (data.form_is_valid) {
          //var idi_id=data.id
          $("#editHermanoModal").modal('hide');
          $("#table_hermanos tbody").html(data.html_hermanos_lista);
          $("#table_hermanos").show();
          $("#myModalLabel").text("¡Hermano actualizado!");
          $("#miModal .modal-body").html("Puedes seguir agregando o guardar sección y continuar");
          $("#miModal").modal('show');
        } else {

          $("<span class='error'>" + data.error + "</span>").insertAfter(elem);
        }

      }
    });

  });

  $.fn.getValidationHermano = function () {
    var message = "";
    var name = "";
    form_valid = "true";
    this.each(function () {
      name = this.id;
      if (this.checkValidity() == false) {
        elem = "#frm_sectres_hermanos #" + name;
        padre = $(elem).parent();
        msg = padre.find(".error");
        if (msg.length > 0)
          msg.remove();
        form_valid = "false";
        //elem="#frm_sectres_hermanos #"+name;
        $("<span class='error'>" + "Completa este campo" + "</span>").insertAfter($(elem));
        $(elem).focus();
        return false;
      } else {//campo valido

      }
    })
  };

  $("#btn_add_hermano").click(function () {
    $("#frm_sectres_hermanos .form-control").getValidationHermano();
    if (form_valid == "true")
      $("#frm_sectres_hermanos").submit();
  });


  //agregar hermano
  $('#frm_sectres_hermanos').submit(function (event) {
    elem = $('#frm_sectres_hermanos .modal-body').find("#id_hermano_nombre");
    padre = elem.parent();
    msg = padre.find(".error");
    if (msg.length > 0)
      msg.remove();
    //$("#p_msg5").hide();
    event.preventDefault();
    var thisform = $(this);
    var actionEndpoint = thisform.attr("action");
    var httpMethod = thisform.attr("method");
    var formData = $('#frm_sectres_hermanos').serialize();
    ///Llamado AJAX
    $.ajax({
      cache: false,
      url: actionEndpoint,
      method: httpMethod,
      data: formData,
      success: function (data) {
        if (data.form_is_valid) {
          $("#addHermanoModal").modal('hide');
          $("#table_hermanos tbody").html(data.html_hermanos_lista);
          $("#table_hermanos").show();
          //alert("Hermano guardado");
          $("#myModalLabel").text("¡Hermano agregado!");
          $("#miModal .modal-body").html("Puedes seguir agregando o guardar sección y continuar");
          $("#miModal").modal('show');
        } else {
          $("<span class='error'>" + data.error + "</span>").insertAfter(elem);
        }
      }
    });

  });
  ////
  $('#agregar_idioma').click(function () {
    elem = $('#frm_secdos_idiomas .modal-body').find("#id_idioma");
    padre = elem.parent();
    msg = padre.find(".error");
    if (msg.length > 0)
      msg.remove();
    $("#frm_secdos_idiomas .form-control").limpiaerrors();
    $("#frm_secdos_idiomas")[0].reset();
    $("#addIdiomaModal").modal('show');
  });

  $.fn.getValidationeditIdi = function () {
    var message = "";
    var name = "";
    form_valid = "true";
    this.each(function () {
      name = this.id;
      if (this.checkValidity() == false) {
        elem = "#frm_secdos_edit_idiomas #" + name;
        padre = $(elem).parent();
        msg = padre.find(".error");
        if (msg.length > 0)
          msg.remove();
        form_valid = "false";
        //elem="#frm_secdos_edit_idiomas #"+name;
        $("<span class='error'>" + "Completa este campo" + "</span>").insertAfter($(elem));
        $(elem).focus();
        return false;
      } else {//campo valido

      }
    })
  };

  $("#btn_edit_idi").click(function () {
    $("#frm_secdos_edit_idiomas .form-control").getValidationeditIdi();
    if (form_valid == "true")
      $("#frm_secdos_edit_idiomas").submit();
  });


  //Seccion 2 editar IDIOMA

  $('#frm_secdos_edit_idiomas').submit(function (event) {
    elem = $('#frm_secdos_edit_idiomas .modal-body').find("#id_idioma");
    padre = elem.parent();
    msg = padre.find(".error");
    if (msg.length > 0)
      msg.remove();
    event.preventDefault();
    var thisform = $(this);
    var actionEndpoint = thisform.attr("action");
    var httpMethod = thisform.attr("method");
    var formData = $('#frm_secdos_edit_idiomas').serialize();

    //////Llamado AJAX
    $.ajax({
      cache: false,
      url: actionEndpoint,
      method: httpMethod,
      data: formData,
      success: function (data) {
        if (data.form_is_valid) {
          //var idi_id=data.id
          $("#editIdiomaModal").modal('hide');
          $("#table_idiomas tbody").html(data.html_idiomas_lista);
          $("#table_idiomas").show();
          $("#myModalLabel").text("¡Idioma actualizado!");
          $("#miModal .modal-body").html("Puedes seguir agregando o guardar sección y continuar");
          $("#miModal").modal('show');
        } else {

          $("<span class='error'>" + data.error + "</span>").insertAfter(elem);
        }

      }
    });

  });

  $.fn.getValidationIdioma = function () {
    var message = "";
    var name = "";
    form_valid = "true";
    this.each(function () {
      name = this.id;
      if (this.checkValidity() == false) {
        elem = "#frm_secdos_idiomas #" + name;
        padre = $(elem).parent();
        msg = padre.find(".error");
        if (msg.length > 0)
          msg.remove();
        form_valid = "false";
        //elem="#frm_secdos_idiomas #"+name;
        $("<span class='error'>" + "Completa este campo" + "</span>").insertAfter($(elem));
        $(elem).focus();
        return false;
      } else {//campo valido
        if ((name == "id_idioma_porcentaje")) {
          padre = $("#" + name).parent();
          msg = padre.find(".error");
          if (msg.length > 0) {//si existe error en porcentaje dejar
            form_valid = "false";
            $("#" + name).focus();
            return false;
          }
        }

      }
    })
  };



  $("#btn_add_idioma").click(function () {
    $("#frm_secdos_idiomas .form-control").getValidationIdioma();
    if (form_valid == "true")
      $("#frm_secdos_idiomas").submit();
  });
  //Seccion 2 agregar IDIOMA
  $('#frm_secdos_idiomas').submit(function (event) {
    elem = $('#frm_secdos_idiomas .modal-body').find("#id_idioma");
    padre = elem.parent();
    msg = padre.find(".error");
    if (msg.length > 0)
      msg.remove();
    //$("#p_msg5").hide();
    event.preventDefault();
    var thisform = $(this);
    var actionEndpoint = thisform.attr("action");
    var httpMethod = thisform.attr("method");
    var formData = $('#frm_secdos_idiomas').serialize();
    //alert("entro");

    //var idioma=$("#id_idioma").val();

    // var porcentaje=$("#id_idioma_porcentaje").val();

    //////Llamado AJAX
    $.ajax({
      cache: false,
      url: actionEndpoint,
      method: httpMethod,
      data: formData,
      success: function (data) {
        if (data.form_is_valid) {
          //var idi_id=data.id
          $("#addIdiomaModal").modal('hide');
          $("#table_idiomas tbody").html(data.html_idiomas_lista);
          $("#table_idiomas").show();
          //idi_id=5;
          //alert("Idioma Agregado");
          $("#myModalLabel").text("¡Idioma guardado!");
          $("#miModal .modal-body").html("Puedes seguir agregando o guardar sección y continuar");
          $("#miModal").modal('show');
        } else {

          $("<span class='error'>" + data.error + "</span>").insertAfter(elem);
        }

      }
    });

  });

  ///
  //Seccion 5 salto a seccion 6
  $("#btn_sec5").click(function (event) {
    event.preventDefault();
    status = 5;
    //$("#ok5").show().fadeOut(5000);
    $("#myModalLabel").text("¡Sección experiencia laboral guardada!");
    $("#miModal .modal-body").html("Puedes seguir agregando o guardar sección y continuar");
    $("#miModal").modal('show');
    $("#pnl_sec6").show();
    //$("#pnl_sec5").toggle(500);

    //$("#btn_sec5").hide();
    // $("#btn_sec5_act").show();


  });

  $('#agregar_estudiootro').click(function () {
    $("#frm_secdos_addestudiosOtro .form-control").limpiaerrors();
    $("#frm_secdos_addestudiosOtro")[0].reset();
    $("#addEstudioOtroModal").modal('show');
  });

  $.fn.getValidationEstOtro = function () {
    var message = "";
    var name = "";
    form_valid = "true";
    this.each(function () {
      name = this.id;
      if (this.checkValidity() == false) {
        elem = "#frm_secdos_addestudios #" + name;
        padre = $(elem).parent();
        msg = padre.find(".error");
        if (msg.length > 0)
          msg.remove();
        form_valid = "false";
        //elem="#frm_secdos_addestudios #"+name;
        $("<span class='error'>" + "Completa este campo" + "</span>").insertAfter($(elem));
        $(elem).focus();
        return false;
      } else {//campo valido
        if ((name == "id_estudios_inicio") || (name == "id_estudios_termino")) {
          padre = $("#" + name).parent();
          msg = padre.find(".error");
          if (msg.length > 0) {//si existe error en fecha dejar
            form_valid = "false";
            $("#" + name).focus();
            return false;
          }
        }
      }
    })
  };

  $("#btn_add_estudiootro").click(function () {
    $("#frm_secdos_addestudiosOtro .form-control").getValidationEstOtro();
    if (form_valid == "true")
      $("#frm_secdos_addestudiosOtro").submit();
  });

  //Seccion 2 agregar estudiootro

  $('#frm_secdos_addestudiosOtro').submit(function (event) {
    //$("#p_msg5").hide();
    event.preventDefault();
    var thisform = $(this);
    var actionEndpoint = thisform.attr("action");
    var httpMethod = thisform.attr("method");
    var formData = $('#frm_secdos_addestudiosOtro').serialize();

    $.ajax({
      cache: false,
      url: actionEndpoint,
      method: httpMethod,
      data: formData,
      success: function (data) {
        if (data.form_is_valid) {
          $("#addEstudioOtroModal").modal('hide');
          $("#table_estudiosotros tbody").html(data.html_estudiosotros_lista);
          $("#table_estudiosotros").show();
          ///////vaciar inputs
          $("#frm_secdos_addestudiosOtro")[0].reset();
          ///////
          $("#myModalLabel").text("¡Otro estudio agregado!");
          $("#miModal .modal-body").html("Puedes seguir agregando o guardar sección y continuar");
          $("#miModal").modal('show');
        } else if (data.result == "passerror") {
          // $("#pass").show().fadeOut(3000);
        } else if (data.result == "user_existe") {
          // $("#user_existe").show().fadeOut(3000);
        } else if (data.result == "email_existe") {
          // $("#email_existe").show().fadeOut(3000); 
        } else if (data.result == 'errores') {
          alert("Errores al guardar estudio");
        }
        console.log("success")
        console.log(data)
      },
      errors: function (errorData) {
        console.log("error")
        console.log(errorData)
      }

    });

  });

  $.fn.getValidationeditEstOtro = function () {
    var message = "";
    var name = "";
    form_valid = "true";
    this.each(function () {
      name = this.id;
      if (this.checkValidity() == false) {
        elem = "#frm_secdos_edit_estudios #" + name;
        padre = $(elem).parent();
        msg = padre.find(".error");
        if (msg.length > 0)
          msg.remove();
        form_valid = "false";
        //elem="#frm_secdos_edit_estudios #"+name;
        $("<span class='error'>" + "Completa este campo" + "</span>").insertAfter($(elem));
        $(elem).focus();
        return false;
      } else {//campo valido

      }
    })
  };

  $("#btn_edit_estotro").click(function () {
    $("#frm_secdos_edit_estudiosotro .form-control").getValidationeditEstOtro();
    if (form_valid == "true")
      $("#frm_secdos_edit_estudiosotro").submit();
  });

  //Seccion 2 editar ESTUDIOOTRO

  $('#frm_secdos_edit_estudiosotro').submit(function (event) {
    event.preventDefault();
    var thisform = $(this);
    var actionEndpoint = thisform.attr("action");
    var httpMethod = thisform.attr("method");
    var formData = $('#frm_secdos_edit_estudiosotro').serialize();

    //////Llamado AJAX
    $.ajax({
      cache: false,
      url: actionEndpoint,
      method: httpMethod,
      data: formData,
      success: function (data) {
        if (data.form_is_valid) {
          //var idi_id=data.id
          $("#editEstudiootroModal").modal('hide');
          $("#table_estudiosotros tbody").html(data.html_estudiosotros_lista);
          $("#table_estudiosotros").show();
          $("#myModalLabel").text("¡Estudio actualizado!");
          $("#miModal .modal-body").html("Puedes seguir agregando o guardar sección y continuar");
          $("#miModal").modal('show');
        } else {

        }

      }
    });

  });



  ////////////////////////////
  $('#agregar_estudio').click(function () {
    $("#frm_secdos_addestudios .form-control").limpiaerrors();
    $("#frm_secdos_addestudios")[0].reset();
    $("#addEstudioModal").modal('show');
  });



  $.fn.getValidationEst = function () {
    var message = "";
    var name = "";
    form_valid = "true";
    this.each(function () {
      name = this.id;
      if (this.checkValidity() == false) {
        elem = "#frm_secdos_addestudios #" + name;
        padre = $(elem).parent();
        msg = padre.find(".error");
        if (msg.length > 0)
          msg.remove();
        form_valid = "false";
        //elem="#frm_secdos_addestudios #"+name;
        $("<span class='error'>" + "Completa este campo" + "</span>").insertAfter($(elem));
        $(elem).focus();
        return false;
      } else {//campo valido
        if ((name == "id_estudios_inicio") || (name == "id_estudios_termino")) {
          padre = $("#" + name).parent();
          msg = padre.find(".error");
          if (msg.length > 0) {//si existe error en fecha dejar
            form_valid = "false";
            $("#" + name).focus();
            return false;
          }
        }
      }
    })
  };

  $("#btn_add_estudio").click(function () {
    $("#frm_secdos_addestudios .form-control").getValidationEst();
    if (form_valid == "true")
      $("#frm_secdos_addestudios").submit();
  });

  //Seccion 2 agregar estudio

  $('#frm_secdos_addestudios').submit(function (event) {
    //$("#p_msg5").hide();
    event.preventDefault();
    var thisform = $(this);
    var actionEndpoint = thisform.attr("action");
    var httpMethod = thisform.attr("method");
    var formData = $('#frm_secdos_addestudios').serialize();

    $.ajax({
      cache: false,
      url: actionEndpoint,
      method: httpMethod,
      data: formData,
      success: function (data) {
        if (data.form_is_valid) {
          $("#addEstudioModal").modal('hide');
          $("#table_estudios tbody").html(data.html_estudios_lista);
          $("#table_estudios").show();
          ///////vaciar inputs
          $("#frm_secdos_addestudios")[0].reset();
          ///////
          $("#myModalLabel").text("¡Estudio agregado!");
          $("#miModal .modal-body").html("Puedes seguir agregando o guardar sección y continuar");
          $("#miModal").modal('show');
        } else if (data.result == "passerror") {
          // $("#pass").show().fadeOut(3000);
        } else if (data.result == "user_existe") {
          // $("#user_existe").show().fadeOut(3000);
        } else if (data.result == "email_existe") {
          // $("#email_existe").show().fadeOut(3000); 
        } else if (data.result == 'errores') {
          alert("Errores al guardar estudio");
        }
        console.log("success")
        console.log(data)
      },
      errors: function (errorData) {
        console.log("error")
        console.log(errorData)
      }

    });

  });

  $.fn.getValidationeditEst = function () {
    var message = "";
    var name = "";
    form_valid = "true";
    this.each(function () {
      name = this.id;
      if (this.checkValidity() == false) {
        elem = "#frm_secdos_edit_estudios #" + name;
        padre = $(elem).parent();
        msg = padre.find(".error");
        if (msg.length > 0)
          msg.remove();
        form_valid = "false";
        //elem="#frm_secdos_edit_estudios #"+name;
        $("<span class='error'>" + "Completa este campo" + "</span>").insertAfter($(elem));
        $(elem).focus();
        return false;
      } else {//campo valido

      }
    })
  };

  $("#btn_edit_est").click(function () {
    $("#frm_secdos_edit_estudios .form-control").getValidationeditEst();
    if (form_valid == "true")
      $("#frm_secdos_edit_estudios").submit();
  });

  //Seccion 2 editar ESTUDIO

  $('#frm_secdos_edit_estudios').submit(function (event) {
    event.preventDefault();
    var thisform = $(this);
    var actionEndpoint = thisform.attr("action");
    var httpMethod = thisform.attr("method");
    var formData = $('#frm_secdos_edit_estudios').serialize();

    //////Llamado AJAX
    $.ajax({
      cache: false,
      url: actionEndpoint,
      method: httpMethod,
      data: formData,
      success: function (data) {
        if (data.form_is_valid) {
          //var idi_id=data.id
          $("#editEstudioModal").modal('hide');
          $("#table_estudios tbody").html(data.html_estudios_lista);
          $("#table_estudios").show();
          $("#myModalLabel").text("¡Estudio actualizado!");
          $("#miModal .modal-body").html("Puedes seguir agregando o guardar sección y continuar");
          $("#miModal").modal('show');
        } else {

        }

      }
    });

  });

  ///
  $('#agregar_experiencia').click(function () {
    $("#frm_seccinco_add_exp .form-control").limpiaerrors();
    $("#frm_seccinco_add_exp")[0].reset();
    $("#addExpModal").modal('show');
    $('#frm_seccinco_add_exp .modal-body').find("#id_experiencia_supervision_num").attr('disabled', 'disabled');
    $('#frm_seccinco_add_exp .modal-body').find("#id_separacion_motivo").attr("required", false);
    $('#frm_seccinco_add_exp .modal-body').find("#id_empresa_fecha_separacion").attr("required", false);
    $("#div_sp").hide();
    $("#div_fs").hide();
    //$(".exp2 #id_empresa_actual").val("Si");
  });

  $("#btn_sec5_add").click(function () {
    //$("#frm_seccinco .form-control").getValidationCinco();
    //if (form_valid=="true")
    //$("#frm_seccinco").submit();
  });

  $.fn.getValidationExp = function () {
    var message = "";
    var name = "";
    form_valid = "true";
    this.each(function () {
      name = this.id;
      if (this.checkValidity() == false) {
        elem = "#frm_seccinco_add_exp #" + name;
        padre = $(elem).parent();
        msg = padre.find(".error");
        if (msg.length > 0)
          msg.remove();
        form_valid = "false";
        //elem="#frm_seccinco_add_exp #"+name;
        $("<span class='error'>" + "Completa este campo" + "</span>").insertAfter($(elem));
        $(elem).focus();
        return false;
      } else {//campo valido
        if ((name == "id_empresa_fecha_ingreso") || (name == "id_empresa_fecha_separacion")) {
          padre = $("#" + name).parent();
          msg = padre.find(".error");
          if (msg.length > 0) {//si existe error en fecha dejar
            form_valid = "false";
            $("#" + name).focus();
            return false;
          }
        }


      }
    })
  };



  $("#btn_add_experiencia").click(function () {
    $("#frm_seccinco_add_exp .form-control").getValidationExp();
    if (form_valid == "true")
      $("#frm_seccinco_add_exp").submit();
  });

  //Seccion 5 agregar experiencia

  $('#frm_seccinco_add_exp').submit(function (event) {
    //$("#p_msg5").hide();
    event.preventDefault();
    var thisform = $(this);
    var actionEndpoint = thisform.attr("action");
    var httpMethod = thisform.attr("method");
    var formData = $('#frm_seccinco_add_exp').serialize();

    $.ajax({
      cache: false,
      url: actionEndpoint,
      method: httpMethod,
      data: formData,
      success: function (data) {
        if (data.form_is_valid) {
          $("#addExpModal").modal('hide');
          $("#table_exp tbody").html(data.html_experiencias_lista);
          $("#table_exp").show();
          ///////vaciar inputs
          $("#frm_seccinco_add_exp")[0].reset();

          ///////
          //alert("Experiencia Agregada");
          $("#myModalLabel").text("¡Experiencia guardada!");
          $("#miModal .modal-body").html("Puedes seguir agregando o guardar sección y continuar");
          $("#miModal").modal('show');
        } else if (data.result == "passerror") {
          // $("#pass").show().fadeOut(3000);
        } else if (data.result == "user_existe") {
          // $("#user_existe").show().fadeOut(3000);
        } else if (data.result == "email_existe") {
          // $("#email_existe").show().fadeOut(3000); 
        } else if (data.result == 'errores') {
          alert("Errores al guardar experiencia");
        }
        console.log("success")
        console.log(data)
      },
      errors: function (errorData) {
        console.log("error")
        console.log(errorData)
      }

    });

  });

  $.fn.getValidationeditCinco = function () {
    var message = "";
    var name = "";
    form_valid = "true";
    this.each(function () {
      name = this.id;
      elem = "#frm_seccinco_edit_exp #" + name;
      padre = $(elem).parent();
      if (this.checkValidity() == false) {
        msg = padre.find(".error");
        if (msg.length > 0)
          msg.remove();
        form_valid = "false";
        //elem="#frm_seccinco_edit_exp #"+name;
        $("<span class='error'>" + "Completa este campo" + "</span>").insertAfter($(elem));
        $(elem).focus();
        return false;
      } else {//campo valido
        if ((name == "id_empresa_fecha_ingreso") || (name == "id_empresa_fecha_separacion")) {
          msg = padre.find(".error");
          if (msg.length > 0) {//si existe error en fecha dejar
            form_valid = "false";
            $(elem).focus();
            return false;
          }
        }

      }
    })
  };

  $("#btn_edit_sec5").click(function () {
    $("#frm_seccinco_edit_exp .form-control").getValidationeditCinco();
    if (form_valid == "true")
      $("#frm_seccinco_edit_exp").submit();
  });


  //Seccion 5 editar EXPERIENCIA

  $('#frm_seccinco_edit_exp').submit(function (event) {
    event.preventDefault();
    var thisform = $(this);
    var actionEndpoint = thisform.attr("action");
    var httpMethod = thisform.attr("method");
    var formData = $('#frm_seccinco_edit_exp').serialize();

    //////Llamado AJAX
    $.ajax({
      cache: false,
      url: actionEndpoint,
      method: httpMethod,
      data: formData,
      success: function (data) {
        if (data.form_is_valid) {
          //var idi_id=data.id
          $("#editExpModal").modal('hide');
          $("#table_exp tbody").html(data.html_experiencias_lista);
          $("#table_exp").show();
          $("#myModalLabel").text("¡Experiencia actualizada!");
          $("#miModal .modal-body").html("Puedes seguir agregando o guardar sección y continuar");
          $("#miModal").modal('show');
        } else {

          $("<span class='error'>" + data.error + "</span>").insertAfter(elem);
        }

      }
    });

  });
  ///
  $.fn.getValidationRef = function () {
    var message = "";
    var name = "";
    form_valid = "true";
    this.each(function () {
      name = this.id;
      if (this.checkValidity() == false) {
        elem = "#frm_secseis_add_ref #" + name;
        padre = $(elem).parent();
        msg = padre.find(".error");
        if (msg.length > 0)
          msg.remove();
        form_valid = "false";
        //elem="#frm_seccinco_add_exp #"+name;
        $("<span class='error'>" + "Completa este campo" + "</span>").insertAfter($(elem));
        $(elem).focus();
        return false;
      } else {//campo valido
      }
    })
  };



  $("#btn_add_referencia").click(function () {
    $("#frm_secseis_add_ref .form-control").getValidationRef();
    if (form_valid == "true")
      $("#frm_secseis_add_ref").submit();
  });


  $('#agregar_referencia').click(function () {
    $("#frm_secseis_add_ref .form-control").limpiaerrors();
    $("#frm_secseis_add_ref")[0].reset();
    $("#addRefModal").modal('show');
  });
  //Agregar referencia
  $('#frm_secseis_add_ref').submit(function (event) {
    //$("#p_msg6").hide();
    event.preventDefault();
    var thisform = $(this);
    var actionEndpoint = thisform.attr("action");
    var httpMethod = thisform.attr("method");
    var formData = $('#frm_secseis_add_ref').serialize();
    $.ajax({
      cache: false,
      url: actionEndpoint,
      method: httpMethod,
      data: formData,
      success: function (data) {
        if (data.form_is_valid) {
          $("#addRefModal").modal('hide');
          $("#table_ref tbody").html(data.html_referencias_lista);
          $("#table_ref").show();
          ///////vaciar inputs
          $("#frm_secseis_add_ref")[0].reset();

          $("#myModalLabel").text("¡Referencia guardada!");
          $("#miModal .modal-body").html("Puedes seguir agregando o enviar cv");
          $("#miModal").modal('show');
        } else if (data.result == "passerror") {
          // $("#pass").show().fadeOut(3000);
        } else if (data.result == "user_existe") {
          // $("#user_existe").show().fadeOut(3000);
        } else if (data.result == "email_existe") {
          // $("#email_existe").show().fadeOut(3000); 
        } else if (data.result == 'errores') {
          alert("Error al guardar referencia");
        }
        console.log("success")
        console.log(data)
      },
      errors: function (errorData) {
        console.log("error")
        console.log(errorData)
      }
    });
  });

  $.fn.getValidationeditSeis = function () {
    var message = "";
    var name = "";
    form_valid = "true";
    this.each(function () {
      name = this.id;
      if (this.checkValidity() == false) {
        elem = "#frm_secseis_edit_ref #" + name;
        padre = $(elem).parent();
        msg = padre.find(".error");
        if (msg.length > 0)
          msg.remove();
        form_valid = "false";
        //elem="#frm_secseis_edit_ref #"+name;
        $("<span class='error'>" + "Completa este campo" + "</span>").insertAfter($(elem));
        $(elem).focus();
        return false;
      } else {//campo valido

      }
    })
  };

  $("#btn_edit_sec6").click(function () {
    $("#frm_secseis_edit_ref .form-control").getValidationeditSeis();
    if (form_valid == "true")
      $("#frm_secseis_edit_ref").submit();
  });



  //Seccion 6 editar REFERENCIA
  $('#frm_secseis_edit_ref').submit(function (event) {
    event.preventDefault();
    var thisform = $(this);
    var actionEndpoint = thisform.attr("action");
    var httpMethod = thisform.attr("method");
    var formData = $('#frm_secseis_edit_ref').serialize();

    //////Llamado AJAX
    $.ajax({
      cache: false,
      url: actionEndpoint,
      method: httpMethod,
      data: formData,
      success: function (data) {
        if (data.form_is_valid) {
          //var idi_id=data.id
          $("#editRefModal").modal('hide');
          $("#table_ref tbody").html(data.html_referencias_lista);
          $("#table_ref").show();
          $("#myModalLabel").text("¡Referencia actualizada!");
          $("#miModal .modal-body").html("Puedes seguir agregando o guardar sección y continuar");
          $("#miModal").modal('show');
        } else {

          $("<span class='error'>" + data.error + "</span>").insertAfter(elem);
        }

      }
    });

  });

  $("#btn_sec6").click(function (event) {
    //vaciar form
    $(".container form").each(function () {
      $(this).find('input').each(function () {
        $(this).val("");
      });

    });
    //inicializar variables
    status = 0;
    $("#id_n").val("");
    $("#candId2").val("");
    $("#candId2_idi").val("");
    $("#candId2_est").val("");
    $("#candId2_estotro").val("");
    $("#candId_editidioma").val("");
    $("#candId3").val("");
    $("#candId3_hijo").val("");
    $("#candId3_hermano").val("");
    $("#candId4").val("");
    $("#candId5").val("");
    $("#candId6").val("");

    $.ajax({
      cache: false,
      url: '/del-session',
      method: 'GET',
      data: {},
      success: function (data) {
      }
    });
    if (localStorage['aviso']=='True'){
      localStorage.removeItem("aviso");
    }
    $("#myModalLabel").text("¡Última sección!");
    $("#miModal .modal-body").html("Gracias por terminar de llenar su CV, será redireccionado");
    $("#miModal").modal('show');
    setTimeout(function () {
      window.location.href = "/candidato/";
    }, 6000);
    event.preventDefault();

  });
  ///
  $("#id_tipo").change(function (e) {
    if ($("#id_tipo").val() != "Departamento") {
      $("#id_piso").val("");
      $("#id_depto").val("");
      $("#id_piso").attr("disabled", "disabled");
      $("#id_depto").attr("disabled", "disabled");
      $("#id_piso").attr("required", false);
      $("#id_depto").attr("required", false);

    }
    else {
      $("#id_piso").removeAttr("disabled");
      $("#id_depto").removeAttr("disabled");
      $("#id_piso").attr("required", true);
      $("#id_depto").attr("required", true);
    }
    $("#id_calle").focus();
  });

  $("#id_estudia_actualmente").change(function (e) {
    if ($("#id_estudia_actualmente").val() != "Si") {
      $("#frm_secdos .estudia .form-control").limpiaerrors();
      $("#id_estudia_que").val("");
      $("#id_estudia_donde").val("");
      $("#id_estudia_horario").val("");
      $("#fec_ter").val("");
      $("#id_estudia_que").attr("disabled", "disabled");
      $("#id_estudia_donde").attr("disabled", "disabled");
      $("#id_estudia_horario").attr("disabled", "disabled");
      $("#fec_ter").attr("disabled", "disabled");
      $("#id_estudia_que").attr("required", false);
      $("#id_estudia_donde").attr("required", false);
      $("#id_estudia_horario").attr("required", false);
      $("#fec_ter").attr("required", false);

    }
    else {
      $("#id_estudia_que").removeAttr("disabled");
      $("#id_estudia_donde").removeAttr("disabled");
      $("#id_estudia_horario").removeAttr("disabled");
      $("#fec_ter").removeAttr("disabled");
      $("#id_estudia_que").attr("required", true);
      $("#id_estudia_donde").attr("required", true);
      $("#id_estudia_horario").attr("required", true);
      $("#fec_ter").attr("required", true);
      $("#id_estudia_que").focus();
    }
  });

  $("#id_credito_infonavit").change(function (e) {
    if ($("#id_credito_infonavit").val() != "Si") {
      $("#id_pago_infonavit").limpiaerror();
      $("#id_pago_infonavit").val("");
      $("#id_pago_infonavit").attr("disabled", "disabled");
      $("#id_pago_infonavit").attr("required", false);
    }
    else {
      $("#id_pago_infonavit").removeAttr("disabled");
      $("#id_pago_infonavit").attr("required", true);
      $("#id_pago_infonavit").focus();
    }
  });

  $("#id_auto_propio").change(function (e) {
    if ($("#id_auto_propio").val() != "Si") {
      $("#id_auto_marca").limpiaerror();
      $("#id_auto_modelo").limpiaerror();
      $("#id_auto_marca").val("");
      $("#id_auto_modelo").val("");
      $("#id_auto_marca").attr("disabled", "disabled");
      $("#id_auto_modelo").attr("disabled", "disabled");
      $("#id_auto_marca").attr("required", false);
      $("#id_auto_modelo").attr("required", false);
    }
    else {
      $("#id_auto_marca").removeAttr("disabled");
      $("#id_auto_modelo").removeAttr("disabled");
      $("#id_auto_marca").attr("required", true);
      $("#id_auto_modelo").attr("required", true);
      $("#id_auto_marca").focus();
    }
  });

  $("#id_seguro_vida").change(function (e) {
    if ($("#id_seguro_vida").val() != "Si") {
      $("#id_seguro_monto").limpiaerror();
      $("#id_seguro_monto").val("");
      $("#id_seguro_monto").attr("disabled", "disabled");
      $("#id_seguro_monto").attr("required", false);
    }
    else {
      $("#id_seguro_monto").removeAttr("disabled");
      $("#id_seguro_monto").attr("required", true);
      $("#id_seguro_monto").focus();
    }
  });

  $("#id_afianzado").change(function (e) {
    if ($("#id_afianzado").val() != "Si") {
      $("#id_afianzado_monto").limpiaerror();
      $("#id_afianzado_monto").val("");
      $("#id_afianzado_monto").attr("disabled", "disabled");
      $("#id_afianzado_monto").attr("required", false);
    }
    else {
      $("#id_afianzado_monto").removeAttr("disabled");
      $("#id_afianzado_monto").attr("required", true);
      $("#id_afianzado_monto").focus();
    }
  });

  $("#id_afiliado_sindicato").change(function (e) {
    if ($("#id_afiliado_sindicato").val() != "Si") {
      $("#id_sindicato_nombre").limpiaerror();
      $("#id_sindicato_cargo").limpiaerror();
      $("#id_sindicato_nombre").val("");
      $("#id_sindicato_cargo").val("");
      $("#id_sindicato_nombre").attr("disabled", "disabled");
      $("#id_sindicato_cargo").attr("disabled", "disabled");
      $("#id_sindicato_nombre").attr("required", false);
      $("#id_sindicato_cargo").attr("required", false);
    }
    else {
      $("#id_sindicato_nombre").removeAttr("disabled");
      $("#id_sindicato_cargo").removeAttr("disabled");
      $("#id_sindicato_nombre").attr("required", true);
      $("#id_sindicato_cargo").attr("required", true);
      $("#id_sindicato_nombre").focus();
    }
  });

  $("#id_ingreso_extra").change(function (e) {
    if ($("#id_ingreso_extra").val() != "Si") {
      $("#id_ingreso_monto").limpiaerror();
      $("#id_ingreso_fuente").limpiaerror();
      $("#id_ingreso_monto").val("");
      $("#id_ingreso_fuente").val("");
      $("#id_ingreso_monto").attr("disabled", "disabled");
      $("#id_ingreso_fuente").attr("disabled", "disabled");
      $("#id_ingreso_monto").attr("required", false);
      $("#id_ingreso_fuente").attr("required", false);
    }
    else {
      $("#id_ingreso_monto").removeAttr("disabled");
      $("#id_ingreso_fuente").removeAttr("disabled");
      $("#id_ingreso_monto").attr("required", true);
      $("#id_ingreso_fuente").attr("required", true);
      $("#id_ingreso_monto").focus();
    }
  });

  $("#id_labora_conocido").change(function (e) {
    if ($("#id_labora_conocido").val() != "Si") {
      $("#id_conocido_nombre").val("");
      $("#id_conocido_depto").val("");
      $("#id_conocido_nombre").attr("disabled", "disabled");
      $("#id_conocido_depto").attr("disabled", "disabled");
      $("#id_conocido_nombre").attr("required", false);
      $("#id_conocido_depto").attr("required", false);
    }
    else {
      $("#id_conocido_nombre").removeAttr("disabled");
      $("#id_conocido_depto").removeAttr("disabled");
      $("#id_conocido_nombre").attr("required", true);
      $("#id_conocido_depto").attr("required", true);
      $("#id_conocido_nombre").focus();
    }
  });

  $(".exp #id_experiencia_supervision").change(function (e) {
    if ($(this).val() != "Si") {
      $(".numexp #id_experiencia_supervision_num").val("");
      $(".numexp #id_experiencia_supervision_num").attr("disabled", "disabled");
      $(".numexp #id_experiencia_supervision_num").attr("required", false);
    }
    else {
      $(".numexp #id_experiencia_supervision_num").removeAttr("disabled");
      $(".numexp #id_experiencia_supervision_num").attr("required", true);
      $(".numexp #id_experiencia_supervision_num").focus();
    }
  });

  $(".eexp #id_experiencia_supervision").change(function (e) {

    if ($(this).val() != "Si") {
      $(".enumexp #id_experiencia_supervision_num").val("");
      $(".enumexp #id_experiencia_supervision_num").attr("disabled", "disabled");
      $(".enumexp #id_experiencia_supervision_num").attr("required", false);
    }
    else {
      $(".enumexp #id_experiencia_supervision_num").removeAttr("disabled");
      $(".enumexp #id_experiencia_supervision_num").attr("required", true);
      $(".enumexp #id_experiencia_supervision_num").focus();
    }
  });
  ///
  $("#id_rfc").change(function (e) {
    e.preventDefault();
    if ($(this).val())
      ValidaRfc($(this).val());
    else {
      padre = $(this).parent();
      msg = padre.find(".error");
      if (msg.length > 0)
        msg.remove();
    }
  });

  $("#id_curp").change(function (e) {
    e.preventDefault();
    if ($(this).val())
      ValidaCURP($(this).val());
    else {
      padre = $(this).parent();
      msg = padre.find(".error");
      if (msg.length > 0)
        msg.remove();
    }
  });


  $("#id_pais_direc").change(function () {
    if ($(this).val() == "1") {
      $("#esdo").show();
    }
    else
      $("#esdo").hide();
  });

  ///
  $("#id_hijos").change(function () {
    if (document.getElementById('id_hijos_0').checked)
      $("#new_hijo").hide();
    else
      $("#new_hijo").show();
  });
  $("#id_hermanos").change(function () {
    if (document.getElementById('id_hermanos_0').checked)
      $("#new_hermano").hide();
    else
      $("#new_hermano").show();
  });
  ///
  $.fn.limpiaerror = function () {
    padre = $(this).parent();
    msg = padre.find(".error");
    if (msg.length > 0)
      msg.remove();
  };

  $.fn.limpiaerrors = function () {
    this.each(function () {
      padre = $(this).parent();
      msg = padre.find(".error");
      if (msg.length > 0)
        msg.remove();
    })
  };

  $("#id_primaria").change(function (e) {
    e.preventDefault();
    if ($("#id_primaria").val() != "") {
      $("#id_primaria_annios").attr("required", true);
      $("#id_primaria_inicio").attr("required", true);
      $("#id_primaria_termino").attr("required", true);
      $("#id_primaria_documento").attr("required", true);
      $("#id_primaria_annios").removeAttr("disabled");
      $("#id_primaria_inicio").removeAttr("disabled");
      $("#id_primaria_termino").removeAttr("disabled");
      $("#id_primaria_documento").removeAttr("disabled");
      $("#id_primaria_annios").focus();
    } else {
      $("#frm_secdos .primaria .form-control").limpiaerrors();
      $("#id_primaria_annios").attr("required", false);
      $("#id_primaria_inicio").attr("required", false);
      $("#id_primaria_termino").attr("required", false);
      $("#id_primaria_documento").attr("required", false);
      $("#id_primaria_annios").val("");
      $("#id_primaria_inicio").val("");
      $("#id_primaria_termino").val("");
      $("#id_primaria_documento").val("");
      $("#id_primaria_annios").attr("disabled", "disabled");
      $("#id_primaria_inicio").attr("disabled", "disabled");
      $("#id_primaria_termino").attr("disabled", "disabled");
      $("#id_primaria_documento").attr("disabled", "disabled");
    }
  });

  $("#id_secundaria").change(function (e) {
    e.preventDefault();
    if ($("#id_secundaria").val() != "") {
      $("#id_secundaria_annios").attr("required", true);
      $("#id_secundaria_inicio").attr("required", true);
      $("#id_secundaria_termino").attr("required", true);
      $("#id_secundaria_documento").attr("required", true);
      $("#id_secundaria_annios").removeAttr("disabled");
      $("#id_secundaria_inicio").removeAttr("disabled");
      $("#id_secundaria_termino").removeAttr("disabled");
      $("#id_secundaria_documento").removeAttr("disabled");
      $("#id_secundaria_annios").focus();
    } else {
      $("#frm_secdos .secundaria .form-control").limpiaerrors();
      $("#id_secundaria_annios").attr("required", false);
      $("#id_secundaria_inicio").attr("required", false);
      $("#id_secundaria_termino").attr("required", false);
      $("#id_secundaria_documento").attr("required", false);
      $("#id_secundaria_annios").val("");
      $("#id_secundaria_inicio").val("");
      $("#id_secundaria_termino").val("");
      $("#id_secundaria_documento").val("");
      $("#id_secundaria_annios").attr("disabled", "disabled");
      $("#id_secundaria_inicio").attr("disabled", "disabled");
      $("#id_secundaria_termino").attr("disabled", "disabled");
      $("#id_secundaria_documento").attr("disabled", "disabled");
    }
  });

  $("#id_preparatoria").change(function (e) {
    e.preventDefault();
    if ($("#id_preparatoria").val() != "") {
      $("#id_preparatoria_annios").attr("required", true);
      $("#id_preparatoria_inicio").attr("required", true);
      $("#id_preparatoria_termino").attr("required", true);
      $("#id_preparatoria_documento").attr("required", true);
      $("#id_preparatoria_annios").removeAttr("disabled");
      $("#id_preparatoria_inicio").removeAttr("disabled");
      $("#id_preparatoria_termino").removeAttr("disabled");
      $("#id_preparatoria_documento").removeAttr("disabled");
      $("#id_preparatoria_annios").focus();
    } else {
      $("#frm_secdos .preparatoria .form-control").limpiaerrors();
      $("#id_preparatoria_annios").attr("required", false);
      $("#id_preparatoria_inicio").attr("required", false);
      $("#id_preparatoria_termino").attr("required", false);
      $("#id_preparatoria_documento").attr("required", false);
      $("#id_preparatoria_annios").val("");
      $("#id_preparatoria_inicio").val("");
      $("#id_preparatoria_termino").val("");
      $("#id_preparatoria_documento").val("");
      $("#id_preparatoria_annios").attr("disabled", "disabled");
      $("#id_preparatoria_inicio").attr("disabled", "disabled");
      $("#id_preparatoria_termino").attr("disabled", "disabled");
      $("#id_preparatoria_documento").attr("disabled", "disabled");
    }
  });

  $("#id_tecnica").change(function (e) {
    e.preventDefault();
    if ($("#id_tecnica").val() != "") {
      $("#id_tecnica_annios").attr("required", true);
      $("#id_tecnica_inicio").attr("required", true);
      $("#id_tecnica_termino").attr("required", true);
      $("#id_tecnica_documento").attr("required", true);
      $("#id_tecnica_annios").removeAttr("disabled");
      $("#id_tecnica_inicio").removeAttr("disabled");
      $("#id_tecnica_termino").removeAttr("disabled");
      $("#id_tecnica_documento").removeAttr("disabled");
      $("#id_tecnica_annios").focus();
    } else {
      $("#frm_secdos .tecnica .form-control").limpiaerrors();
      $("#id_tecnica_annios").attr("required", false);
      $("#id_tecnica_inicio").attr("required", false);
      $("#id_tecnica_termino").attr("required", false);
      $("#id_tecnica_documento").attr("required", false);
      $("#id_tecnica_annios").val("");
      $("#id_tecnica_inicio").val("");
      $("#id_tecnica_termino").val("");
      $("#id_tecnica_documento").val("");
      $("#id_tecnica_annios").attr("disabled", "disabled");
      $("#id_tecnica_inicio").attr("disabled", "disabled");
      $("#id_tecnica_termino").attr("disabled", "disabled");
      $("#id_tecnica_documento").attr("disabled", "disabled");
    }
  });

  $("#id_profesional").change(function (e) {
    e.preventDefault();
    if ($("#id_profesional").val() != "") {
      $("#id_profesional_annios").attr("required", true);
      $("#id_profesional_inicio").attr("required", true);
      $("#id_profesional_termino").attr("required", true);
      $("#id_profesional_documento").attr("required", true);
      $("#id_carrera").attr("required", true);
      //$("#id_tesis").attr("required", true);
      //$("#id_cedula").attr("required", true);
      $("#id_profesional_annios").removeAttr("disabled");
      $("#id_profesional_inicio").removeAttr("disabled");
      $("#id_profesional_termino").removeAttr("disabled");
      $("#id_profesional_documento").removeAttr("disabled");
      $("#id_carrera").removeAttr("disabled");
      $("#id_tesis").removeAttr("disabled");
      $("#id_profesional_annios").focus();
      //$("#id_cedula").removeAttr("disabled");
    } else {
      $("#frm_secdos .profesional .form-control").limpiaerrors();
      $("#id_profesional_annios").attr("required", false);
      $("#id_profesional_inicio").attr("required", false);
      $("#id_profesional_termino").attr("required", false);
      $("#id_profesional_documento").attr("required", false);
      $("#id_carrera").attr("required", false);
      //$("#id_tesis").attr("required", false);
      //$("#id_cedula").attr("required", false);
      $("#id_profesional_annios").val("");
      $("#id_profesional_inicio").val("");
      $("#id_profesional_termino").val("");
      $("#id_profesional_documento").val("");
      $("#id_carrera").val("");
      $("#id_tesis").val("");
      //$("#id_cedula").val("");
      $("#id_profesional_annios").attr("disabled", "disabled");
      $("#id_profesional_inicio").attr("disabled", "disabled");
      $("#id_profesional_termino").attr("disabled", "disabled");
      $("#id_profesional_documento").attr("disabled", "disabled");
      $("#id_carrera").attr("disabled", "disabled");
      $("#id_tesis").attr("disabled", "disabled");
      $("#id_forma").attr("required", false);
      $("#id_cedula").attr("required", false);

      $("#id_forma").val("");
      $("#id_cedula").val("");

      $("#id_forma").attr("disabled", "disabled");
      $("#id_cedula").attr("disabled", "disabled");
      //$("#id_cedula").attr("disabled", "disabled");
    }
  });

  $("#id_tesis").change(function (e) {
    e.preventDefault();
    if ($("#id_tesis").val() != "") {
      $("#id_forma").attr("required", true);
      $("#id_cedula").attr("required", true);

      $("#id_forma").removeAttr("disabled");
      $("#id_cedula").removeAttr("disabled");
      $("#id_forma").focus();

    } else {
      // $("#frm_secdos .profesional .form-control").limpiaerrors();
      $("#id_forma").attr("required", false);
      $("#id_cedula").attr("required", false);

      $("#id_forma").val("");
      $("#id_cedula").val("");

      $("#id_forma").attr("disabled", "disabled");
      $("#id_cedula").attr("disabled", "disabled");

    }
  });

  $("#id_postgrado").change(function (e) {
    e.preventDefault();
    if ($("#id_postgrado").val() != "") {
      $("#id_postgrado_annios").attr("required", true);
      $("#id_postgrado_inicio").attr("required", true);
      $("#id_postgrado_termino").attr("required", true);
      $("#id_postgrado_documento").attr("required", true);
      $("#id_postgrado_nombre").attr("required", true);
      $("#id_postgrado_annios").removeAttr("disabled");
      $("#id_postgrado_inicio").removeAttr("disabled");
      $("#id_postgrado_termino").removeAttr("disabled");
      $("#id_postgrado_documento").removeAttr("disabled");
      $("#id_postgrado_nombre").removeAttr("disabled");
      $("#id_postgrado_annios").focus();
    } else {
      $("#frm_secdos .postgrado .form-control").limpiaerrors();
      $("#id_postgrado_annios").attr("required", false);
      $("#id_postgrado_inicio").attr("required", false);
      $("#id_postgrado_termino").attr("required", false);
      $("#id_postgrado_documento").attr("required", false);
      $("#id_postgrado_nombre").attr("required", false);
      $("#id_postgrado_annios").val("");
      $("#id_postgrado_inicio").val("");
      $("#id_postgrado_termino").val("");
      $("#id_postgrado_documento").val("");
      $("#id_postgrado_nombre").val("");
      $("#id_postgrado_annios").attr("disabled", "disabled");
      $("#id_postgrado_inicio").attr("disabled", "disabled");
      $("#id_postgrado_termino").attr("disabled", "disabled");
      $("#id_postgrado_documento").attr("disabled", "disabled");
      $("#id_postgrado_nombre").attr("disabled", "disabled");
    }
  });

  $("#id_especialidad").change(function (e) {
    e.preventDefault();
    if ($("#id_especialidad").val() != "") {
      $("#id_especialidad_annios").attr("required", true);
      $("#id_especialidad_inicio").attr("required", true);
      $("#id_especialidad_termino").attr("required", true);
      $("#id_especialidad_documento").attr("required", true);
      $("#id_especialidad_nombre").attr("required", true);
      $("#id_especialidad_annios").removeAttr("disabled");
      $("#id_especialidad_inicio").removeAttr("disabled");
      $("#id_especialidad_termino").removeAttr("disabled");
      $("#id_especialidad_documento").removeAttr("disabled");
      $("#id_especialidad_nombre").removeAttr("disabled");
      $("#id_especialidad_annios").focus();
    } else {
      $("#frm_secdos .especialidad .form-control").limpiaerrors();
      $("#id_especialidad_annios").attr("required", false);
      $("#id_especialidad_inicio").attr("required", false);
      $("#id_especialidad_termino").attr("required", false);
      $("#id_especialidad_documento").attr("required", false);
      $("#id_especialidad_nombre").attr("required", false);
      $("#id_especialidad_annios").val("");
      $("#id_especialidad_inicio").val("");
      $("#id_especialidad_termino").val("");
      $("#id_especialidad_documento").val("");
      $("#id_especialidad_nombre").val("");
      $("#id_especialidad_annios").attr("disabled", "disabled");
      $("#id_especialidad_inicio").attr("disabled", "disabled");
      $("#id_especialidad_termino").attr("disabled", "disabled");
      $("#id_especialidad_documento").attr("disabled", "disabled");
      $("#id_especialidad_nombre").attr("disabled", "disabled");
    }
  });

  ///
  /*
      $(".panel-heading").click(function (e) {
          var hermano = $(this).parent().children(".panel-body");
          hermano.toggle(500);
          e.preventDefault();
      });*/
  /* $(".panel-heading").click(function (e) {
     var hermano = $(this).parent().children(".panel-body");
     if ( (status>=0) && (hermano.attr('id')=="pnl_sec1") ||
          (status>=1) && (hermano.attr('id')=="pnl_sec2") ||
          (status>=2) && (hermano.attr('id')=="pnl_sec3") ||
          (status>=3) && (hermano.attr('id')=="pnl_sec4") ||
          (status>=4) && (hermano.attr('id')=="pnl_sec5") ||
          (status>=5) && (hermano.attr('id')=="pnl_sec6")){
          
          hermano.toggle(500);
          e.preventDefault();
     }
   });*/
  ///

});//fin