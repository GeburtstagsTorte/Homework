<!DOCTYPE html><html><head><meta charset = "UTF-8"></head>
<body>
<form action = "rechner_ausgabe.php" method = "post" target = "ausgabe">
	<p><input name = "zahl1"> Zahl 1</p>
	<p><input name = "zahl2"> Zahl 2</p>
	<select name = "rechenart">
	<option value = "add" selected = "selected"> Addition</option>
	<option value = "sub"> Subtraktion</option>
	<option value = "mul"> Multiplikation</option>
	<option value = "div"> Division</option>
	</select>
	<p><input type = "submit" name = "sent" value = "Berechnen"> <input type = "reset"></p>
</form>
</body></html>