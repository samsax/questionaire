
$(function () {
    selects = $('.select2')
        for(select in selects){
            $(selects.get(select)).select2()
        }
    $('body').on('DOMNodeInserted', 'select', function () {
        selectDropDown = $(this).select2();
        selectDropDown.on('select2:select', function (e) {
            var event = new Event('change');
            e.target.dispatchEvent(event);
        });
    });

    
});
const app = new Vue({
    el: '#app',
    data: {
      errors: [],
      name: null,
      age: null,
      movie: null,
      jsonObject:null,
      valid:false,
      first:[],
      condition:''
    
    },
    mounted(){
        
    },
    methods:{ 
        onChange:function(event){
            console.log(event.target.value);
        },
        sendResponse: function(){
            formToJson()
            if(this.valid){
            axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
            axios.defaults.xsrfCookieName = "csrftoken"
            axios.post(save_response, {
                data: {
                    data: formToJson()
                }
            })
        .then(function(res) {
            if(res.data.success)
            Swal.fire(
                res.data.message,
                '',
                'success'
              ).then( result => {
                window.location = urlNext
              }
              )
            else
                Swal.fire(
                    res.data.message,
                    '',
                    'error'
                )
        })
        .catch(function(err) {
            Swal.fire(
                'No fue posible guardar las respuestas',
                '',
                'error'
            )
            })
        }
        else{
            Swal.fire(
                'Todas las respuestas son requeridas',
                '',
                'error'
            )
            }
        }
    }
})


  function formToJson(){
    var formElement = document.getElementsByTagName("form")[0],
        inputElements = formElement.getElementsByTagName("input"),
        jsonObject = {};
    for(var i = 0; i < inputElements.length; i++){
        var inputElement = inputElements[i];
        if(inputElement.name!='' & inputElement.name!='csrfmiddlewaretoken' & inputElement.style.display != "none" & inputElement.type !='search'){
            if(inputElement.value!='')
                jsonObject[inputElement.name] = inputElement.value
            else{
                app.valid = false
                return
            }
                
        }
            

    }
    inputElements = formElement.getElementsByTagName("select")
    for(var i = 0; i < inputElements.length; i++){
        var inputElement = inputElements[i];
        if(inputElement.style.display != "none" & inputElement.type != 'search'){
            if(inputElement.multiple){
                selectedOptions = []
                if(inputElement.selectedOptions.length >0){
                    for(var indexOption = 0; indexOption < inputElement.selectedOptions.length; indexOption++)
                    selectedOptions.push(inputElement.selectedOptions[indexOption].value)
                    jsonObject[inputElement.name] = selectedOptions
                }
                else{
                    app.valid = false
                    return
                }
            }else{
                if(inputElement.value!='')
                    jsonObject[inputElement.name] = inputElement.value
                else{
                    app.valid = false
                    return
                }
            }
            }
            
        }
    
    app.valid = true
    app.jsonObject = jsonObject;
    return JSON.stringify(jsonObject);
}
