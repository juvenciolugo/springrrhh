$(document).ready(function () {
  $("#emp").addClass("active");


  $("input[type='file']").change(function () {
    var fileName = this.files[0].name;
    var ext = fileName.split('.').pop();
    var abuelo = $(this).parent();
    //var bisabuelo = $(this).parent().parent().parent();
    msg = abuelo.find(".error");
    if (msg.length > 0)
      msg.remove();
    if ($(this).attr("id") == 'id_curriculum') {
      if (ext != 'pdf') {
        $("<span class='error'> Archivo no válido  </span>").insertAfter($(this));
        //abuelo.find('.fileinput-filename').text('');
        this.files[0].name = '';
        this.value = '';
      }

    } else {
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
    }


  });

  //Actualizar docs
  $('#frm_docs').submit(function (e) {
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
          $("#myModalLabel").text("Mensaje");
          $("#miModal .modal-body").html("¡Documentos actualizados!");
          $("#miModal").modal('show');
          setTimeout(function () {
            location.reload();
          }, 3000);
        }
      },
      errors: function (errorData) {
        console.log("error")
        console.log(errorData)
      }
    });
  });

  //Actualizar Estudios pro
  $('form').submit(function (e) {
    alert("Submit");
    e.preventDefault();
    //var formID = $(this).attr("id");
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
          $("#myModalLabel").text("Mensaje");
          $("#miModal .modal-body").html("¡Documentos actualizados!");
          $("#miModal").modal('show');
          setTimeout(function () {
            location.reload();
          }, 3000);
        }
      },
      errors: function (errorData) {
        console.log("error")
        console.log(errorData)
      }
    });
  });

  //Actualizar Estudios pro
  $('#frm_est_pro').submit(function (e) {
    e.preventDefault();
    //var formID = $(this).attr("id");
    var thisform = $(this);
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
          $("#myModalLabel").text("Mensaje");
          $("#miModal .modal-body").html("¡Documentos de estudios profesionales actualizados!");
          $("#miModal").modal('show');
          setTimeout(function () {
            location.reload();
          }, 3000);
        }
      },
      errors: function (errorData) {
        console.log("error")
        console.log(errorData)
      }
    });
  });

  $(".btn_actpro,.btn_actotro").click(function(){
    abuelo=$(this).parent().parent();
    elem=abuelo.find(".comprobante");
    if (elem.val()==''){
    $("#myModalLabel").text("Mensaje");
    $("#miModal .modal-body").html("¡No haz elegido un archivo!");
    $("#miModal").modal('show');
    elem.focus();
    }else{
      $(this).closest('form').submit();
    }

  });
  
  
  $(".imgestotro").click(function (e) {
    e.preventDefault();
    abuelo=$(this).parent().parent();
    ele=abuelo.find(".img_estotro");
    if (!ele.is(":visible")) {
      $(this).text("Cancelar");
      ele.show();
      //$("#img_estpro").show();
    } else {
      $(this).text("Cambiar");
      ele.hide();
      //$("#img_estpro").hide();
    }
  });
  $(".imgestpro").click(function (e) {
    e.preventDefault();
    abuelo=$(this).parent().parent();
    ele=abuelo.find(".img_estpro");
    if (!ele.is(":visible")) {
      $(this).text("Cancelar");
      ele.show();
      //$("#img_estpro").show();
    } else {
      $(this).text("Cambiar");
      ele.hide();
      //$("#img_estpro").hide();
    }
  });
  $(".imgcurri").click(function (e) {
    e.preventDefault();
    if (!$("#img_curri").is(":visible")) {
      $(".imgcurri").text("Cancelar");
      $("#img_curri").show();
    } else {
      $(".imgcurri").text("Cambiar");
      $("#img_curri").hide();
    }
  });

  $(".imginef").click(function (e) {
    e.preventDefault();
    if (!$("#img_frente").is(":visible")) {
      $(".imginef").text("Cancelar");
      $("#img_frente").show();
    } else {
      $(".imginef").text("Cambiar");
      $("#img_frente").hide();
    }
  });
  $(".imginea").click(function (e) {
    e.preventDefault();
    if (!$("#img_atras").is(":visible")) {
      $(".imginea").text("Cancelar");
      $("#img_atras").show();
    } else {
      $(".imginea").text("Cambiar");
      $("#img_atras").hide();
    }
  });

  $(".imgacta").click(function (e) {
    e.preventDefault();
    if (!$("#img_acta").is(":visible")) {
      $(".imgacta").text("Cancelar");
      $("#img_acta").show();
    } else {
      $(".imgacta").text("Cambiar");
      $("#img_acta").hide();
    }
  });

  $(".imgcurp").click(function (e) {
    e.preventDefault();
    if (!$("#img_curp").is(":visible")) {
      $(".imgcurp").text("Cancelar");
      $("#img_curp").show();
    } else {
      $(".imgcurp").text("Cambiar");
      $("#img_curp").hide();
    }
  });
  $(".imgrfc").click(function (e) {
    e.preventDefault();
    if (!$("#img_rfc").is(":visible")) {
      $(".imgrfc").text("Cancelar");
      $("#img_rfc").show();
    } else {
      $(".imgrfc").text("Cambiar");
      $("#img_rfc").hide();
    }
  });
  $(".imgcomp").click(function (e) {
    e.preventDefault();
    if (!$("#img_comp").is(":visible")) {
      $(".imgcomp").text("Cancelar");
      $("#img_comp").show();
    } else {
      $(".imgcomp").text("Cambiar");
      $("#img_comp").hide();
    }
  });

  $(".imgimss").click(function (e) {
    e.preventDefault();
    if (!$("#img_imss").is(":visible")) {
      $(".imgimss").text("Cancelar");
      $("#img_imss").show();
    } else {
      $(".imgimss").text("Cambiar");
      $("#img_imss").hide();
    }
  });
  $(".imgcarta1").click(function (e) {
    e.preventDefault();
    if (!$("#img_carta1").is(":visible")) {
      $(".imgcarta1").text("Cancelar");
      $("#img_carta1").show();
    } else {
      $(".imgcarta1").text("Cambiar");
      $("#img_carta1").hide();
    }
  });
  $(".imgcarta2").click(function (e) {
    e.preventDefault();
    if (!$("#img_carta2").is(":visible")) {
      $(".imgcarta2").text("Cancelar");
      $("#img_carta2").show();
    } else {
      $(".imgcarta2").text("Cambiar");
      $("#img_carta2").hide();
    }
  });
  $(".imgcontrato").click(function (e) {
    e.preventDefault();
    if (!$("#img_contrato").is(":visible")) {
      $(".imgcontrato").text("Cancelar");
      $("#img_contrato").show();
    } else {
      $(".imgcontrato").text("Cambiar");
      $("#img_contrato").hide();
    }
  });

  $(".imginfonavit").click(function (e) {
    e.preventDefault();
    if (!$("#img_infonavit").is(":visible")) {
      $(".imginfonavit").text("Cancelar");
      $("#img_infonavit").show();
    } else {
      $(".imginfonavit").text("Cambiar");
      $("#img_infonavit").hide();
    }
  });

  $(".imgpermiso").click(function (e) {
    e.preventDefault();
    if (!$("#img_permiso").is(":visible")) {
      $(".imgpermiso").text("Cancelar");
      $("#img_permiso").show();
    } else {
      $(".imgpermiso").text("Cambiar");
      $("#img_permiso").hide();
    }
  });

  $(".imgoficio").click(function (e) {
    e.preventDefault();
    if (!$("#img_oficio").is(":visible")) {
      $(".imgoficio").text("Cancelar");
      $("#img_oficio").show();
    } else {
      $(".imgoficio").text("Cambiar");
      $("#img_oficio").hide();
    }
  });
  $(".imgcarta").click(function (e) {
    e.preventDefault();
    if (!$("#img_carta").is(":visible")) {
      $(".imgcarta").text("Cancelar");
      $("#img_carta").show();
    } else {
      $(".imgcarta").text("Cambiar");
      $("#img_carta").hide();
    }
  });
  $(".imgidf").click(function (e) {
    e.preventDefault();
    if (!$("#img_idf").is(":visible")) {
      $(".imgidf").text("Cancelar");
      $("#img_idf").show();
    } else {
      $(".imgidf").text("Cambiar");
      $("#img_idf").hide();
    }
  });
  $(".imgida").click(function (e) {
    e.preventDefault();
    if (!$("#img_ida").is(":visible")) {
      $(".imgida").text("Cancelar");
      $("#img_ida").show();
    } else {
      $(".imgida").text("Cambiar");
      $("#img_ida").hide();
    }
  });



})