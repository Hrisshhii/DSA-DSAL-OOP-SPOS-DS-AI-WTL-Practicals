<?php
include 'config.php';

$id = $_GET['id'];

$result = $conn->query("SELECT * FROM students WHERE id=$id");
$row = $result->fetch_assoc();

if (isset($_POST['update'])) {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $course = $_POST['course'];

    $sql = "UPDATE students 
            SET name='$name', email='$email', course='$course' 
            WHERE id=$id";

    if ($conn->query($sql) === TRUE) {
        echo "Updated successfully!";
    }
}
?>

<form method="POST">
    Name: <input type="text" name="name" value="<?php echo $row['name']; ?>"><br>
    Email: <input type="email" name="email" value="<?php echo $row['email']; ?>"><br>
    Course: <input type="text" name="course" value="<?php echo $row['course']; ?>"><br>
    <button type="submit" name="update">Update</button>
</form>
