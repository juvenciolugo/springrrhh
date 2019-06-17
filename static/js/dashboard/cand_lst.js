
function env_email(cand_id, user_id) {
  $.ajax({
    cache: false,
    url: "/lst-correo",
    method: "GET",
    data: { "cand_id": cand_id, "user_id": user_id },
    success: function (data) {
      $("#frm_email")[0].reset();
      if (data.status == "OK") {
        //$("#frm_docs .form-control").limpiaerrors();
        //$('#idi_id').val(data.id);
        //$('#frm_email .modal-body').find("#cand_Id").val(data.id);

        $('#frm_email .modal-body').find("#nombre").val(data.user_name);
        $('#frm_email .modal-body').find("#nombre_cand").val(data.cand_name);
        $('#frm_email .modal-body').find("#correo").val(data.user_email);
        $('#frm_email .modal-body').find("#correo_cand").val(data.cand_email);
        //$('#frm_email .modal-body').find("#id_CURP").val();
        $("#env_correo").modal('show');
      }
      else {
        //$('#frm_email .modal-body').find("#cand_Id").val(data.id);
        $("#env_correo").modal('show');
      }
    }
  });
};
function edit_docs(id) {
  $.ajax({
    cache: false,
    url: "/lst-docs",
    method: "GET",
    data: { "id": id },
    success: function (data) {
      $("#frm_docs")[0].reset();
      if (data.status == "OK") {
        //$("#frm_docs .form-control").limpiaerrors();
        //$('#idi_id').val(data.id);

        $('#frm_docs .modal-body').find("#cand_Id").val(data.id);
        $('#frm_docs .modal-body').find("#id_INE").prop("checked", data.INE);
        $('#frm_docs .modal-body').find("#id_Acta").prop("checked", data.Acta);
        $('#frm_docs .modal-body').find("#id_CURP").prop("checked", data.CURP);
        $('#frm_docs .modal-body').find("#id_RFC").prop("checked", data.RFC);
        $('#frm_docs .modal-body').find("#id_Comp_dom").prop("checked", data.Comp_dom);
        $('#frm_docs .modal-body').find("#id_Comp_grado").prop("checked", data.Comp_grado);
        $('#frm_docs .modal-body').find("#id_Comp_cursos").prop("checked", data.Comp_cursos);
        $('#frm_docs .modal-body').find("#id_Comp_permiso").prop("checked", data.Comp_permiso);
        $('#frm_docs .modal-body').find("#id_IMSS").prop("checked", data.IMSS);
        $('#frm_docs .modal-body').find("#id_Cartas").prop("checked", data.Cartas);
        $('#frm_docs .modal-body').find("#id_Esdo_cuenta").prop("checked", data.Esdo_cuenta);
        $('#frm_docs .modal-body').find("#id_Esdo_info").prop("checked", data.Esdo_info);
        $('#frm_docs .modal-body').find("#id_Lic_manejo").prop("checked", data.Lic_manejo);
        $('#frm_docs .modal-body').find("#id_Observaciones").val(data.Observaciones);

        $("#ver_docs").modal('show');
      }
      else {
        //alert(data.id);
        $('#frm_docs .modal-body').find("#cand_Id").val(data.id);
        $("#ver_docs").modal('show');
      }
    }
  });
};
////////////////////////////////////////////
////////////////////////////////////////////
////////////////////////////////////////////
////////////////////////////////////////////
////////////////////////////////////////////
$(document).ready(function () {
  $("#can").addClass("active");
  var msg_fec = "hola";
  

  $(".candrrhh").click(function (e) {
    //e.preventDefault();
    //e.stopPropagation();    
    //var href = $(this).attr('href');
    if (localStorage) {
      localStorage["aviso"] = 'True';
    }
    //document.location.href = href;

  });




  $('#frm_docsw').submit(function (event) {
    event.preventDefault();
    var thisform = $(this);
    var actionEndpoint = thisform.attr("action");
    var httpMethod = thisform.attr("method");
    var formData = $('#frm_docs').serialize();

    //////Llamado AJAX
    $.ajax({
      cache: false,
      url: actionEndpoint,
      method: httpMethod,
      data: formData,
      success: function (data) {
        if (data.form_is_valid) {
          //var idi_id=data.id
          $("#ver_docs").modal('hide');
          $("#myModalLabel").text("Mensaje");
          $("#miModal .modal-body").html("¡Documentos actualizados!");
          $("#miModal").modal('show');
        }

      }
    });

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
    if (reg == "CANDIDATO")
      del_candidato(id);
  });

  function del_candidato(id) {
    $.ajax({
      cache: false,
      url: "/del-candidato",
      method: "GET",
      data: { "id": id },
      success: function (data) {
        if (data.form_is_valid) {
          $("#table_candidatos tbody").html(data.html_candidatos_lista);
          $("#table_candidatos").show();


          $("#myModalLabel").text("Aviso");
          $("#miModal .modal-body").html("¡Candidato eliminado!");
          $("#miModal").modal('show');
        } else {

          $("<span class='error'>" + data.error + "</span>").insertAfter(elem);
        }
      }
    });

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
  $('#fecha_filtro').datepicker({
    language: "es",
    todayBtn: "linked",
    keyboardNavigation: false,
    forceParse: false,
    calendarWeeks: true,
    dateFormat: 'dd/mm/yy',
    autoclose: true
  });

  $("#fecha_filtro").change(function (e) {
    e.preventDefault();
    var dtVal = $("#fecha_filtro").val();
    padre = $(this).parent().parent();
    msg = padre.find(".error");
    if (msg.length > 0)
      msg.remove();
    if (dtVal != '') {
      if (ValidateDate(dtVal)) {
        if (fecha_mayor(dtVal)) {

        } else {
          $("#fecha_filtro").focus();
          $("<span class='error'>" + msg_fec + "</span>").insertAfter($(this).parent());
        }
      }
      else {
        $("#fecha_filtro").focus();
        $("<span class='error'>" + msg_fec + "</span>").insertAfter($(this).parent());
      }
    } else {

    }

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

  $("#btnfiltra").click(function () {
    padre = $(this).parent().parent();
    msg = padre.find(".error");
    if (msg.length > 0)
      msg.remove();
    dato = $("#flt_dato").val();
    if (dato != '') {
      $.ajax({
        cache: false,
        url: "/filtra-cand",
        method: "GET",
        data: { "dato": dato },
        success: function (data) {
          if (data.form_is_valid) {//encontro resultados
            $("#table_candidatos tbody").html(data.html_candidatos_lista);
            $("#table_candidatos").show();
            $("#lstAll").show();

            /*$("#myModalLabel").text("Idioma eliminado!!");
            $("#miModal .modal-body").html("Puedes seguir agregando o guardar sección y continuar");
            $("#miModal").modal('show');*/
          } else {
            $("#myModalLabel").text("No se encontraron resultados!!");
            $("#miModal .modal-body").html("Inténtalo con otra(s) palabra(s)");
            $("#miModal").modal('show');
          }
        }
      });

    } else {
      $("#flt_dato").focus();
      next = $("#flt_dato").next();
      $("<span class='error'><br> Escribe puesto a buscar  </span>").insertAfter(next);

    }

  });

  $("#btnfiltra2").click(function () {
    padre = $(this).parent().parent();
    msg = padre.find(".error");
    if (msg.length > 0)
      msg.remove();
    nom = $("#flt_nom").val();
    pat = $("#flt_pat").val();
    mat = $("#flt_mat").val();
    if (nom != '' || pat != '' || mat != '') {
      $.ajax({
        cache: false,
        url: "/filtra2-cand",
        method: "GET",
        data: { "nom": nom, "pat": pat, "mat": mat },
        success: function (data) {
          if (data.form_is_valid) {//encontro resultados
            $("#table_candidatos tbody").html(data.html_candidatos_lista);
            $("#table_candidatos").show();
            $("#lstAll").show();

          } else {
            $("#myModalLabel").text("No se encontraron resultados!!");
            $("#miModal .modal-body").html("Inténtalo con otra(s) palabra(s)");
            $("#miModal").modal('show');
          }
        }
      });

    } else {
      $("#flt_nom").focus();
      $("<span class='error'><br> Escribe nombre o apellidos a buscar  </span>").insertAfter("#btnfiltra2");

    }

  });

  $("#btnfiltra3").click(function () {
    padre = $(this).parent().parent();
    msg = padre.find(".error");
    if (msg.length > 0)
      msg.remove();
    fec = $("#fecha_filtro").val();

    if (fec != '') {
      $.ajax({
        cache: false,
        url: "/filtra3-cand",
        method: "GET",
        data: { "fec": fec },
        success: function (data) {
          if (data.form_is_valid) {//encontro resultados
            $("#table_candidatos tbody").html(data.html_candidatos_lista);
            $("#table_candidatos").show();
            $("#lstAll").show();

          } else {
            $("#myModalLabel").text("No se encontraron resultados!!");
            $("#miModal .modal-body").html("Inténtalo con otra fecha");
            $("#miModal").modal('show');
          }
        }
      });

    } else {
      $("#fecha_filtro").focus();
      $("<span class='error'><br> Escribe una fecha a buscar  </span>").insertAfter("#btnfiltra3");

    }

  });

  $("#btnAll").click(function () {
    $.ajax({
      cache: false,
      url: "/all-cand",
      method: "GET",
      data: { "dato": dato },
      success: function (data) {
        if (data.form_is_valid) {//encontro resultados
          $("#table_candidatos tbody").html(data.html_candidatos_lista);
          $("#table_candidatos").show();
          $("#lstAll").hide();

          /*$("#myModalLabel").text("Idioma eliminado!!");
          $("#miModal .modal-body").html("Puedes seguir agregando o guardar sección y continuar");
          $("#miModal").modal('show');*/
        } else {
          $("#myModalLabel").text("No se encontraron resultados!!");
          $("#miModal .modal-body").html("Inténtalo con otra(s) palabra(s)");
          $("#miModal").modal('show');
        }
      }
    });



  });

  /*  $("#btnDeleteAll").click(function(){
      var lista = [];
          $.each($("input[name='eliminar[]']:checked"), function(){            
            lista.push($(this).val());
          });
      //alert("entro");
      
//        alert(lista);
      if (!lista.length)
        alert("Vacio");
      else{
        

        /////////////////////////////
        
          // random data
          var param = new FormData(); 
          param.append('id_lst',12);
          //alert(param)
          //data.lastname  = "Snow";
          //var jsonData = JSON.stringify(data);
          //alert(jsonData);
          //let data = 'mydata=foo&excel=bar';
          
          let request = new XMLHttpRequest();
          //var json_upload = "id_lst=" + JSON.stringify({id:"12"});
          var csrfToken = request.getResponseHeader('x-csrf-token'); 
          request.open('POST', '../lstreporte/', true);
          request.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
          request.setRequestHeader('x-csrf-token', csrfToken);  
          //request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
          
          //request.send({ "id_lst[]": lista});
          //request.responseType = 'FormData';
          request.send(param);

      
          request.onload = function (e) {
              if (this.status === 200) {
                  let filename = "";
                  let disposition = request.getResponseHeader('Content-Disposition');
                  // check if filename is given
                  if (disposition && disposition.indexOf('attachment') !== -1) {
                      let filenameRegex = /filename[^;=\n]*=((['"]).*?\2|[^;\n]*)/;
                      let matches = filenameRegex.exec(disposition);
                      if (matches != null && matches[1]) filename = matches[1].replace(/['"]/g, '');
                  }
                  let blob = this.response;
                  if (window.navigator.msSaveOrOpenBlob) {
                      window.navigator.msSaveBlob(blob, filename);
                  }
                  else {
                      let downloadLink = window.document.createElement('a');
                      let contentTypeHeader = request.getResponseHeader("Content-Type");
                      downloadLink.href = window.URL.createObjectURL(new Blob([blob], {type: contentTypeHeader}));
                      downloadLink.download = filename;
                      document.body.appendChild(downloadLink);
                      downloadLink.click();
                      document.body.removeChild(downloadLink);
                  }
              } else {
                  alert('Download failed.')
              }
          };
      

        /////////////////////////////
        $.ajax({
          cache: false,
          url:"/lstreporte/",
          method: "GET",
          data:{"id_lst[]":lista},
          success: function (data) {

          }
        });


      }

        

    });*/





});