<!DOCTYPE html><html><head><meta charset = "UTF-8"></head>
<body>
<p> N S A! </p>
<form action = "eingabe.php" method = "post">
	<p><input name = "vor"> Vorname</p>
	<p><input name = "nach"> Nachname</p>
	<p><input name = "adress"> Adresse</p>
	<p><input name = "number"> Nummer</p>
	<p><input name = "user"> Username</p>
	<p><input name = "pw"> Password</p>
	<p><input type = "submit"> <input type = "reset"></p>
</form>
<?php
echo "Hallo ". $_POST["vor"]." ". $_POST["nach"];
?>
</body></html>