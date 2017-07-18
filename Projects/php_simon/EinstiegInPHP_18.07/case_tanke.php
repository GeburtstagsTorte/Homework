<!DOCTYPE html><html><head><meta charset = "UTF-8"></head>
<body>
<p> Tanke +</p>
<p> Bei  >100  l gibt es 2% Rabatt!</p>
<form action = "case_tanke.php" method = "post">
	<p><input name = "liter"> Anzahl in Liter</p>
	<p><input name = "sort"> Sorte (S oder N)</p>
	<p><input type = "submit" name = "sumbit"> <input type = "reset"></p>
</form>

<?php
$liter = doubleval($_POST["liter"]);
$sort = $_POST["sort"];
$rabatt = 0.98;

function realLiter($liter, $rabatt){
    if ($liter > 100){
        return $liter * $rabatt;
    }
    else {
        return $liter;
    }
}

$realLiter = realLiter($liter, $rabatt);

switch($sort){
    case "S":
        echo "Sie kaufen $liter S zum Preis von ". $realLiter*1.35;
	    break;
    case "N":
        echo "Sie kaufen $liter N zum Preis von ". $realLiter*1.40;
        break;
    default:
        echo "Willkommen bei der Tanke... Entweder S oder N !";
}
?>
</body></html>