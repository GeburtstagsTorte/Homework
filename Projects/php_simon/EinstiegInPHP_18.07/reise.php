<!DOCTYPE html><html><head><meta charset = 'UTF-8'></head><body>
<form action = "reise.php" method = 'post'>
<h2>Reiseziel- und Hotelwahl</h2>
<h4>Reiseziel</h4>
<p>
<input type="radio" name="rziel" value="Baia Mare" checked="checked"> Baia Mare<br>
<input type="radio" name="rziel" value="Aix en Provence"> Aix en Provence<br>
<input type="radio" name="rziel" value="Via Roma"> Via Roma<br>
</p>
<h4>Hotel</h4>
<p>
<select name = 'hotel'>
<option value = "Hotel Baia" selected="selected"> Hotel Baia</option>
<option value = "Hotel Aix"> Hotel Aix</option>
<option value = "Hotel Roma"> Hotel Via</option>
</select>
</p>
<p><input type = 'submit'> </p>
</form>
<?php 
$rziel = $_POST['rziel'];
$hotel = $_POST['hotel'];
echo "Es geht also ins $hotel in $rziel!";
?>
</body></html>

