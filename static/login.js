// function submit_func()
// {
//     var usrname = document.getElementById("username").value;
//     var pword = document.getElementById("password").value;
//     if(usrn.length>=4 & pword.length>=8)
//     {
//         document.getElementById("login_form").submit();
//     }
//     else
//     {
//         alert("Please match the criteria !");    
//     }
// }
function password()
{
    var x = document.getElementById("password");
    var y = document.getElementById("eye_open_pwd");
    var z = document.getElementById("eye_closed_pwd");
    if (x.type ==='password'){
        x.type = "text";
        y.style.display = "block";
        z.style.display = "none";
    }
    else{
        x.type = "password";
        y.style.display = "none";
        z.style.display = "block";
    }
}