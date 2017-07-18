<?php
//func_num_args(); // zählt args die einer funktion mitgegeben werden

//func_get_arg(); //  zieht arg nach index

//func_get_args(); // zieht alle args

?>

<!DOCTYPE html><html><head><meta charset = "UTF-8"></head>
<body>
<?php 
$x1 = 10;

function recFunc($x){
    $x = $x / 2;
    if ($x > 0.4){
        echo "$x<br>";
        recFunc($x);
    }
}

recFunc($x1);
?>
</body></html>