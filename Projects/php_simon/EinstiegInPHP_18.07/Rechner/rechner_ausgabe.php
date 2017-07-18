<!DOCTYPE html><html><head><meta charset="utf-8"></head>
<body>
<?php

function execAll(){
    include 'allinone1.php';
    echo $tf2. '$tf2 übermittelt';
    if (isset($tf2)){
        echo "case1";
        if ($tf2==1){
            echo "case2";
            return 1;
        }
        elseif ($tf2==0){
            echo "case3";
            return 0;
        }
    }
    echo "case4";
}

function calcRequest(){
    echo "Processing your calculation...";
    $v1 = doubleval($_POST['zahl1']);
    $v2 = doubleval($_POST['zahl2']);
    switch ($_POST['rechenart']['selected']){ // +- selected?
        case "add":
            echo "<br>Solution: " .$v1 + $v2;
            break;
        case "sub":
            echo "<br>Solution: " .$v1 - $v2;
            break;
        case "mul":
            echo "<br>Solution: " .$v1 * $v2;
            break;
        case "div":
            echo "<br>Solution: " .$v1 / $v2;
            break;
        default:
            echo "<br>Nur Zahlen und keine Buchstaben bitte.";
    }
}

if (isset($_POST['sent'])){
    $tf = execAll();
    echo "case5";
    if ($tf == 1){
        calcRequest();
    }
    elseif ($tf == 0){
        echo "Put the captcha in, please. <br>Afterwards we can show your calculation's solution.";
    }
}
?>
</body></html>