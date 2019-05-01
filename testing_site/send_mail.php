<?php
	if(isset($_POST['subscribe']))
	{
		//$to = 'admin@mandyaclinic.web44.net';
		$to = 'bmritt@gmail.com';
		$from = $_POST['email'];
		$subject = 'Regarding Appointment Details';
		$message = 'Your appointment is booked for 3.00pm';
		mail($to,$subject,$message,"From:".$from);
		echo "Mail Sent. Thank you " . $first_name . ", we will contact you shortly.";
	}
?>
