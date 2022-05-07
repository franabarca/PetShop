$(document).ready(function() {


    $("#btnenviar").click(function(){
        var nombre = $("#nombre").val();
        var mail = $("#mail").val();
        var mensaje = $("#mensaje").val();

        if (nombre == ""){
            $("#mensaje1").fadeIn();
            return false;
        }else{
            $("#mensaje1").fadeOut();
        }

        if (mail == ""){
            $("#mensaje2").fadeIn();
            return false;
        }else{
            $("#mensaje2").fadeOut();
        }

        if (mensaje == ""){
            $("#mensaje3").fadeIn();
            return false;
        }else{
            $("#mensaje3").fadeOut();
        }

    });

    $("#btnquienes").click(function(){
        $("#parrafo").toggle(2000);
        return false;
    })

    $("#btnquienes").click(function(){
        $("#imagen").toggle(2000);
        return false;
    })
    

  });