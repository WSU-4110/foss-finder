<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $name = $_POST["name"];
  $developer = $_POST["developer"];
  $description = $_POST["description"];
  $image_url = $_POST["image-url"];
  $categories = implode(", ", $_POST["category"]);

  // Create a new text file
  $file = fopen("submissions.txt", "a");

  // Write the form data to the text file
  fwrite($file, "Software Name: $name\n");
  fwrite($file, "Software Developer: $developer\n");
  fwrite($file, "Software Description: $description\n");
  fwrite($file, "Image Thumbnail URL: $image_url\n");
  fwrite($file, "Software Type: $categories\n");
  fwrite($file, "----------------------------------------\n");

  // Close the file
  fclose($file);
}
?>
