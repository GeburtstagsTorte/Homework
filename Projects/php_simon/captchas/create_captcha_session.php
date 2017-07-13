<!DOCTYPE html><html><head><meta charset = "UTF-8"></head>
<body>

<?php
function checkInput(){
    
    $pdo2 = new PDO('mysql:host=localhost;dbname=test', 'root', '');
    $sql = "SELECT code FROM session WHERE id = 0";
    $correct_code = $pdo2->query($sql)->fetch();
    $eingabe = $_POST["eingabe"];

    if (doubleval($eingabe) != $correct_code['code']){
        echo "<br>put the captcha in! are you a robot?<br> try again!<br>";
        include 'randomizeimageandcode.php';
    }
    if (doubleval($eingabe) == $correct_code['code']){
        echo "<br>you are not a robot";
    }
}

checkInput();
?>
</body></html>