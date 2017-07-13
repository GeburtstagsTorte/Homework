<!DOCTYPE html><html><head><meta charset = "UTF-8"></head>
<body>
<form action = "create_captcha_session.php" method = "post">
<p><input name = "eingabe"> CAPTCHA Eingabe</p>
<p><input type = "submit" name = "sumbit"> 
</form>
<?php

function checkInput($eingabe){
    
    $pdo2 = new PDO('mysql:host=localhost;dbname=test', 'root', '');
    $sql = "SELECT code FROM session WHERE id = 0";
    $correct_code = $pdo2->query($sql)->fetch();
    echo doubleval($eingabe);
    
    if (doubleval($eingabe) == $correct_code['code']){
        echo "<br>you are not a robot";
    }
    if (doubleval($eingabe) == 0){
        echo "<br>put the captcha in";
    }
    $eingabe = 0;
}

include 'randomizeimageandcode.php';
$eingabe = $_POST["eingabe"];
checkInput($eingabe);

?>

</body></html>