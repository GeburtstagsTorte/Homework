<!DOCTYPE html><html><head><meta charset = "UTF-8"></head><body>
<table border="1">
<?php
$namen = ["Peter", "Markus", "Jens", "Julia", "Monika", "Gerd"];
$alter = ["Peter"=>34, "Markus"=>42, "Jens"=>12, "Julia"=>45, "Monika"=>54, "Gerd"=>34];

/*
echo "<td align ='left'> Name </td>";
echo "<td align ='right'> Alter</td>";
for ($i=0; $i<=count($namen)-1; $i++){
    echo "<tr>";
    echo "<td align ='left'>". $namen[$i]. "</td>";
    echo "<td align ='right'>". $alter[$i]. "</td>";
    echo "</tr>";
*/

/*
$summe = 0;
foreach($alter as $wert){
    $summe += $wert;
}
$mittelwert = $summe / count($alter);
echo "<p>Mittelwert: $mittelwert</p>";
*/

/*
echo "<td align ='left'>  Name </td>";
echo "<td align ='right'> Alter </td>";
foreach($alter as $name=>$age){
    echo "<tr>";
    echo "<td align ='left'>" .$name. "</td>";
    echo "<td align ='right'>" .$age. "</td>";
    echo "</tr>";
}
*/


?>
</table>
</body></html>