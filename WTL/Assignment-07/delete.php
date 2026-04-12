<?php
include 'config.php';

$id = $_GET['id'];

$sql = "DELETE FROM students WHERE id=$id";

if ($conn->query($sql) === TRUE) {
    echo "Deleted successfully!";
}

header("Location: index.php");
?>
