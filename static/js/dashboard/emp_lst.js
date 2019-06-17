
function env2_email(emp_id, user_id) {
    $.ajax({
        cache: false,
        url: "/lst2-correo",
        method: "GET",
        data: { "emp_id": emp_id, "user_id": user_id },
        success: function (data) {
            $("#frm_email")[0].reset();
            if (data.status == "OK") {
                //$("#frm_docs .form-control").limpiaerrors();
                //$('#idi_id').val(data.id);
                //$('#frm_email .modal-body').find("#cand_Id").val(data.id);
                

                $('#frm_email .modal-body').find("#nombre").val(data.user_name);
                $('#frm_email .modal-body').find("#nombre_emp").val(data.emp_name);
                $('#frm_email .modal-body').find("#correo").val(data.user_email);
                $('#frm_email .modal-body').find("#correo_emp").val(data.emp_email);
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
function edit2_docs(id) {
    $.ajax({
        cache: false,
        url: "/lst2-docs",
        method: "GET",
        data: { "id": id },
        success: function (data) {
            //$('.modal-body').find("#id_INE").attr('readonly','readonly');
            $('.modal-body').find("#id_INE").attr('disabled', 'disabled');
            $('.modal-body').find("#id_Acta").attr('disabled', 'disabled');
            $('.modal-body').find("#id_CURP").attr('disabled', 'disabled');
            $('.modal-body').find("#id_RFC").attr('disabled', 'disabled');
            $('.modal-body').find("#id_Comp_dom").attr('disabled', 'disabled');
            $('.modal-body').find("#id_Comp_grado").attr('disabled', 'disabled');
            $('.modal-body').find("#id_Comp_cursos").attr('disabled', 'disabled');
            $('.modal-body').find("#id_Comp_permiso").attr('disabled', 'disabled');
            $('.modal-body').find("#id_IMSS").attr('disabled', 'disabled');
            $('.modal-body').find("#id_Cartas").attr('disabled', 'disabled');
            $('.modal-body').find("#id_Esdo_cuenta").attr('disabled', 'disabled');
            $('.modal-body').find("#id_Esdo_info").attr('disabled', 'disabled');
            $('.modal-body').find("#id_Lic_manejo").attr('disabled', 'disabled');
            //$('.modal-body').find("#id_Observaciones").attr('disabled','disabled');
            
            if (data.status == "OK") {
                //$("#frm_docs .form-control").limpiaerrors();
                //$('#idi_id').val(data.id);
                $("#status_doc").text(data.et_status);
                $('.modal-body').find("#id_INE").prop("checked", data.INE);
                $('.modal-body').find("#id_Acta").prop("checked", data.Acta);
                $('.modal-body').find("#id_CURP").prop("checked", data.CURP);
                $('.modal-body').find("#id_RFC").prop("checked", data.RFC);
                $('.modal-body').find("#id_Comp_dom").prop("checked", data.Comp_dom);
                $('.modal-body').find("#id_Comp_grado").prop("checked", data.Comp_grado);
                $('.modal-body').find("#id_Comp_cursos").prop("checked", data.Comp_cursos);
                $('.modal-body').find("#id_Comp_permiso").prop("checked", data.Comp_permiso);
                $('.modal-body').find("#id_IMSS").prop("checked", data.IMSS);
                $('.modal-body').find("#id_Cartas").prop("checked", data.Cartas);
                $('.modal-body').find("#id_Esdo_cuenta").prop("checked", data.Esdo_cuenta);
                $('.modal-body').find("#id_Esdo_info").prop("checked", data.Esdo_info);
                $('.modal-body').find("#id_Lic_manejo").prop("checked", data.Lic_manejo);
                //$('.modal-body').find("#id_Observaciones").val(data.Observaciones);

                $("#ver_docs").modal('show');
            }
            else {
                $("#ver_docs").modal('show');
            }
        }
    });
};



function editar_per(id, username, first_name, last_name, email, pas, activo) {
    $("#id").val(id);
    $("#id_username").val(username);
    $("#id_first_name").val(first_name);
    $("#id_last_name").val(last_name);
    $("#id_email").val(email);
    ti = $("#id_tipo_empleado").val();
    if (ti == 1)
        tipo = 3
    else if (ti == 2)
        tipo = 2
    else if (ti == 3)
        tipo = 5
    else if (ti == 4)
        tipo = 4
    else if (ti == 5)
        tipo = 0
    else if (ti == 6)
        tipo = 1
    $("#id_is_admin").val(tipo);

    if (activo == "True")
        $("#id_is_active").val(1);
    else
        $("#id_is_active").val(0);


    $("#editPerModal").modal('show');
};

$(document).ready(function () {
    $("#emp").addClass("active");

   

    $('.modal-body .input-group.date').datepicker({
        language: "es",
        todayBtn: "linked",
        keyboardNavigation: false,
        forceParse: false,
        calendarWeeks: true,
        autoclose: true
    });
    $(".colarrhh").click(function(e){
        e.preventDefault();
        e.stopPropagation();    
        var href = $(this).attr('href');
        
        //investigar si ya capturo su información
        id=$(this).data('id');
        $.ajax({
            cache: false,
            url: "/buscar-cand",
            method: "GET",
            data: { "id": id },
            success: function (data) {
                if (data.form_is_valid!=false) {
                    //generara session para evitar la solicitud del aviso de privacidad
                    if (localStorage) 
                        localStorage["aviso"]= 'True';
                    document.location.href = href;
                }else{
                    $("#myModalLabel2").text("Aviso");
                    $("#miModal .modal-body").html("¡El empleado no ha registrado su información!");
                    $("#miModal").modal('show');

                }
            }
        });
        
        
     }); 

    
    $(".contenido").on("click",".btnDelete",function(e){
        e.preventDefault();
        var id = $(this).data('id');
        var reg = $(this).data('reg');
        $('#myModalDel').data({'id': id,'reg':reg}).modal('show');
       });

       $('#btnDeleteYes').click(function (e) {
        // Preguntar motivos de baja
        e.preventDefault();
        var id = $('#myModalDel').data('id');
        var reg = $('#myModalDel').data('reg');
        $('#myModalDel').modal('hide');
        //frm_baja_emp
        $('#frm_baja_emp #emp_Id').val(id);
        $('#myModalBaja').data({'id': id,'reg':reg}).modal('show');
        //if(reg=="EMPLEADO")
        //  del_candidato(id);
        });

        $('#btndarBaja').click(function (e) {
            var formData = $('#frm_baja_emp').serialize();
            $.ajax({
                cache: false,
                url:"/baja-emp",
                method: "GET",
                data:formData,
                success: function (data) {
                  if (data.form_is_valid){
                    $('#myModalBaja').modal('hide');
                    $("#table_empleados tbody").html(data.html_empleados_lista);
                    $("#table_empleados").show();

                    
                    $("#myModalLabel2").text("Aviso");
                    $("#miModal .modal-body").html("¡El empleado ha sido de baja!");
                    $("#miModal").modal('show');
                  }else{
                    
                   $("<span class='error'>"+"No existe empleado"+"</span>").insertAfter(elem);
                  } 
                }
              });

        });


    $('#agregar_per').click(function () {
        $("#frm_addper")[0].reset();
        $("#add_PerModal").modal('show');
    });

    $('#frm_editper').submit(function (event) {
        event.preventDefault();
        var thisform = $(this);
        var actionEndpoint = thisform.attr("action");
        var httpMethod = thisform.attr("method");
        var formData = $('#frm_editper').serialize();

        $.ajax({
            cache: false,
            url: actionEndpoint,
            method: httpMethod,
            data: formData,
            success: function (data) {
                if (data == "OK") {
                    $("#editPerModal").modal('hide');
                    location.reload();
                } else if (data == "passerror") {
                    $("#pass2").show().fadeOut(3000);
                } else if (data == "user_existe") {
                    $("#user_existe2").show().fadeOut(3000);
                } else if (data == "email_existe") {
                    $("#email_existe2").show().fadeOut(3000);
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

    $('#frm_addper').submit(function (event) {
        $("#p_msg").hide();
        event.preventDefault();
        var thisform = $(this);
        var actionEndpoint = thisform.attr("action");
        var httpMethod = thisform.attr("method");
        var formData = $('#frm_addper').serialize();


        $.ajax({
            cache: false,
            url: actionEndpoint,
            method: httpMethod,
            data: formData,
            success: function (data) {
                if (data.result == "OK") {
                    $("#add_PerModal").modal('hide');
                    location.reload();
                } else if (data.result == "passerror") {
                    $("#pass").show().fadeOut(3000);
                } else if (data.result == "user_existe") {
                    $("#user_existe").show().fadeOut(3000);
                } else if (data.result == "email_existe") {
                    $("#email_existe").show().fadeOut(3000);
                } else if (data.result == 'password2') {
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

});

