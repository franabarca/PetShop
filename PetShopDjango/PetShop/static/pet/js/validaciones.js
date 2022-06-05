$(document).ready(function() {

//index
    $("#btnenviar").click(function(){
        var nombre = $("#nombre").val();
        var mail = $("#mail").val();
        var mensaje = $("#mensaje").val();
        var monto = $("monto").val();
        var noValido = / /;

        if (nombre == ""){
            $("#mensaje1").fadeIn();
            return false;
        }else{
            $("#mensaje1").fadeOut();
            if (mail == ""){
                $("#mensaje2").fadeIn();
                return false;
            }else{
                $("#mensaje2").fadeOut();
                if (mensaje == ""){
                    $("#mensaje3").fadeIn();
                    return false;
                }else{
                    $("#mensaje3").fadeOut();
                    
                        if($("#mail").val().indexOf('@', 0) == -1 || $("#mail").val().indexOf('.', 0) == -1) {
                            $("#mensaje4").fadeIn();
                            return false;
                        }else{
                            $("#mensaje4").fadeOut();
                        
                                if (mensaje.length<15){
                                    $("#mensaje6").fadeIn();
                                    return false;
                                }else{
                                    $("#mensaje6").fadeOut();

                                    if (mensaje.length>150){
                                        $("#mensaje7").fadeIn();
                                        return false;
                                    }else{
                                        $("#mensaje7").fadeOut();

                                       
                                            
                                            if(noValido.test(nombre)){ 
                                                $("#mensaje5").fadeOut();
                                                alert('Su mensague ha sido enviado correctamente.');   
                                            }
                                            else{
                                                $("#mensaje5").fadeIn();
                                            return false;
                                            }
                                           
                                    }
                                }
                        }
            }
        }
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
    


    //index2
    $("#btnenviar2").click(function(){
        var nombre = $("#nombre").val();
        var mail = $("#mail").val();
        var monto = $("#monto").val();
        var noValido = / /;

        if (nombre == ""){
            $("#mensaje1").fadeIn();
            return false;
        }else{
            $("#mensaje1").fadeOut();
            if (mail == ""){
                $("#mensaje2").fadeIn();
                return false;
            }else{
                $("#mensaje2").fadeOut();
                    
                        if($("#mail").val().indexOf('@', 0) == -1 || $("#mail").val().indexOf('.', 0) == -1) {
                            $("#mensaje4").fadeIn();
                            return false;
                        }else{
                            $("#mensaje4").fadeOut();

                            if(monto == ""){
                                $("#mensaje9").fadeIn();
                            return false;
                            }else{
                                $("#mensaje9").fadeOut();
                                if(monto>300000){
                                    $("#mensaje8").fadeIn();
                                    return false;
                                   }else{
                                    $("#mensaje8").fadeOut();
                                    if(monto<1000){
                                        $("#mensaje10").fadeIn();
                                        return false;
                                    }else{
                                        $("#mensaje10").fadeOut();
                                        if(noValido.test(nombre)){ 
                                            $("#mensaje5").fadeOut();
                                            alert('Su donacion a sido enviado correctamente.');   
                                        }
                                        else{
                                            $("#mensaje5").fadeIn();
                                        return false;
                                        }
                                    }
                                       
                                    
                                   }   
                            }
                        

                                    
                            
                        }
            
        }
    }

    });


  });
  
