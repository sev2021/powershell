#!/bin/bash

# Set the home page.
echo "<html><body><h3>PAzzure! My name is $(hostname).</h3><h2>PHP <?php ;?></h2></body></html>" | sudo tee -a /var/www/html/index.php
