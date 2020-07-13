
const app = new Vue({
    el: '#app',
    data: {
      errors: [],
      name: null,
      age: null,
      movie: null
    },
    methods:{ 
        sendResponse: function(){
            axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
            axios.defaults.xsrfCookieName = "csrftoken"
            axios.post(save_response, {
                data: {
                    data: formToJson()
                }
            })
        .then(function(res) {
        if(res.status==201) {
            mensaje.innerHTML = 'El nuevo Post ha sido almacenado con id: ' + res.data.id;
        }
        })
        .catch(function(err) {
            console.log(err);
        })
        .then(function() {
        });
            }
        }
    })


  function formToJson(){
    var formElement = document.getElementsByTagName("form")[0],
        inputElements = formElement.getElementsByTagName("input"),
        jsonObject = {};
    for(var i = 0; i < inputElements.length; i++){
        var inputElement = inputElements[i];
        jsonObject[inputElement.name] = inputElement.value;

    }
    inputElements = formElement.getElementsByTagName("select")
    for(var i = 0; i < inputElements.length; i++){
        var inputElement = inputElements[i];
        jsonObject[inputElement.name] = inputElement.value;

    }
    return JSON.stringify(jsonObject);

    {}
}