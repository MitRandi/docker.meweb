function refresh_container() {
    window.location = "http://141.8.194.114:8888"
}

function post(path, params, method) {
    method = method || "post"; // Set method to post by default if not specified.

    var form = document.createElement("form");
    form.setAttribute("method", method);
    form.setAttribute("action", path);

    for(var key in params) {
        if(params.hasOwnProperty(key)) {
            var hiddenField = document.createElement("input");
            hiddenField.setAttribute("type", "hidden");
            hiddenField.setAttribute("name", key);
            hiddenField.setAttribute("value", params[key]);

            form.appendChild(hiddenField);
         }
    }

    document.body.appendChild(form);
    form.submit();
}

function select_container()
{
    var container_id = ""
    var containers_radio_checker = document.getElementsByName("container");
    for(var k = 0; k < containers_radio_checker.length; k++){
        if(containers_radio_checker[k].checked){
            container_id =  containers_radio_checker[k].value
            return container_id
        }
    }
}

function start_container()
{
    var container_id = select_container()
    post('/', {action: 'start', cid: container_id});
}

function stop_container()
{
    var container_id = select_container()
    post('/', {action: 'stop', cid: container_id});
}
