

function yesnoCheck() {
        
        
    if (document.getElementById('id_SiNo_0').checked) {

        document.getElementById('Si').style.display = 'none';
    }
    else
    {
        document.getElementById('Si').style.display = 'block';
    }

    if (document.getElementById('id_permiso_trabajo').checked) {

       // document.getElementById('id_solicitud_permiso_trabajo').style.display = 'none';
        document.getElementById('id_solicitud_permiso_trabajo').checked = false;
        $("#sol_").hide();
    }
    else
    {
        //document.getElementById('id_solicitud_permiso_trabajo').style.display = 'block';
        $("#sol_").show();
    }


}

    $(document).ready(function(){
        alert("hola");
        function obten_edad(cumpleStr) {
            var hoy = new Date();
            var annio =cumpleStr.substring(6,10);
            var mes =cumpleStr.substring(3,5);
            var dia =cumpleStr.substring(0,2);
            var cumple = new Date(annio,mes-1,dia);
            var edad = hoy.getFullYear() - cumple.getFullYear();
            var m = hoy.getMonth() - cumple.getMonth();
            if (m < 0 || (m === 0 && hoy.getDate() < cumple.getDate())) {
                edad--;
            } 
            return edad;
        };
        $("input[type='file']").change(function(){
            var fileName = this.files[0].name;
            var ext = fileName.split('.').pop();
            var abuelo = $(this).parent().parent();
            //abuelo.find('fileinput-filename').hide();
            switch (ext){
                case 'jpg':
                case 'jpeg':
                case 'png':
                case 'pdf':break;
                default:{
                     alert("Archivo no válido");
                     //abuelo.find('.fileinput-filename').text('');
                     this.files[0].name='';
                     this.value='';
                     
                }
            }
            

        });
        $("#pascheck").change(function(){
            if ($(this).is(":checked"))
                $("#pass_").show();
            else
            $("#pass_").hide();
        });


        $("#id_tipo_documento_identidad").change(function() {
            if ($(this).val()==2){
                $("#pass_").show();
                $("#cedine_").hide();
            }
            else if (($(this).val()==1) || ($(this).val()==3)){
                $("#pass_").hide();
                $("#cedine_").show();
                $("#pascheck").prop("checked",false);
            }

        });
        
        $("#id_fecha_nacimiento").focusout(function() {
            if ($("#id_fecha_nacimiento").val())
               $("#id_edad").val(obten_edad($("#id_fecha_nacimiento").val()));
        });
        $("#id_fecha_nacimiento").change(function() {
            if ($("#id_fecha_nacimiento").val())
               $("#id_edad").val(obten_edad($("#id_fecha_nacimiento").val()));
        });

        $("#id_tipo").change(function(){
            if ($(this).val()=="Casa"){
                $("#piso").val("");
                $("#depto").val("");
                $("#tipo_c").hide();
            }
            else $("#tipo_c").show();
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

        $('.chosen-select').chosen({width: "100%"});


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

