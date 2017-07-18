<!DOCTYPE html><html><head><meta charset = "UTF-8"></head>
<body>
<form enctype = "multipart/form-data" action = "uploadfile.php" method = "post">
<?php
if (isset($_POST['sent'])){
    echo $_FILES["upfile"]['name']. " // " .$_FILES["upfile"]['type']. " // " .$_FILES["upfile"]['size'];
    
    // dateiname mit explode()
    $dname = explode(".", $_FILES["upfile"]['name']);
    $ending = $dname[count($dname)-1];
    echo "<br>Dateityp: ". $ending;
}
?>
	<p>Datei: <input name = "upfile" type = "file" size = "25"></p>
	<p><input type = "submit" name = "sent"> <input type = "reset"></p>
</form>
</body></html>