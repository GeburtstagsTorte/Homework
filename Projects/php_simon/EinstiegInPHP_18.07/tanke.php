<!DOCTYPE html><html><head><meta charset = "UTF-8"></head>
<body>
<p> Tanke +</p>
<p> Bei  >100  l gibt es 2% Rabatt!</p>
<form action = "tanke.php" method = "post">
	<p><input name = "liter"> Anzahl in Liter</p>
	<p><input name = "sort"> Sorte (S oder N)</p>
	<p><input type = "submit" name = "sumbit"> <input type = "reset"></p>
</form>
<?php
if ($_POST["liter"] != NULL and $_POST["sort"] != NULL){
    $liter = doubleval($_POST["liter"]);
    $sort = $_POST["sort"];
    if ($sort == "S"){
        if ($liter > 100){
            echo "Sie kaufen $liter $sort mit 2% rabatt zum Gesamtpreis von " . ($liter * 1.35 * 0.98);
        }
        else{
            echo "Sie kaufen $liter $sort zum Gesamtpreis von ". (1.35*$liter);
        }
    }
    elseif ($sort == "N"){
        if ($liter > 100){
            echo "Sie kaufen $liter $sort mit 2% rabatt zum Gesamtpreis von " . ($liter * 1.40 * 0.98);
        }
        else{
            echo "Sie kaufen $liter $sort zum Gesamtpreis von ". (1.40*$liter); 
        }
    }
    else{ 
        echo "";
    }
}
?>
</body></html>