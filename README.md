# WhenShouldIGoTest
A website that takes a business location and outputs the best time and day to visit. The project required HTML, CSS, Python, and Flask. We also used the BestTime API.

The input page features a image as a background with an input box for location. We used Google's autocomplete API for the input box, so we could get an accurate address. 
Once the user clicks the submit button, a POST request is sent using Flask that takes the location and sends it to the Python file. 
The Python file uses the location and finds the best time using the BestTime API. The result is sent back using Flask. 
This result is sent to the output page where it is displayed.
