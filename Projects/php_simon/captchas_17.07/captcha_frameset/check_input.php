<!DOCTYPE html><html><head><meta charset = "UTF-8"></head>
<body>
<?php
function checkInput(){
    
    $pdo2 = new PDO('mysql:host=localhost;dbname=testdatenbank', 'root', '');
    $sql = "SELECT code FROM session WHERE id = 0";
    $correct_code = $pdo2->query($sql)->fetch();
    $eingabe = doubleval($_POST["eingabe"]);

    if ($eingabe != $correct_code['code']){
        echo "<br>put the captcha in! are you a robot?<br> try again!<br>";
        // include 'create_captcha_session.php';
    }
    if ($eingabe == $correct_code['code']){
        echo "the correct code was " .$correct_code['code'];
        echo "<br>you are not a robot";
    }
}
if (isset($_POST['eingabe'])){
    checkInput();
}
?>
</body></html>