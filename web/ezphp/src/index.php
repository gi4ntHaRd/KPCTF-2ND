<?php
highlight_file(__FILE__);
$func=$_GET["func"]??"var_dump";
$args=$_GET["args"]??["Hack Me!"];
function waf($str){
    if(preg_match('/call|system|exec|popen|file|passthru|open|eval|map|include|require|filter|assert|env|preg|ini|read|write|rename|show|sort|func|curl|copy|dir|get|proc|ld/i',$str)){
        return false;
    }
    return true;
}
if(waf($func)){
    call_user_func_array($func,$args);
}else{
    echo "try again";
}