Feature: Flying Tractor Altitude Management
	 As a Tractor Operator
	 I want Altitude Management
	 So I can operate my Flying Tractor safely

	 Scenario: Velocity Affects Altitude
	 	   Given a Flying Tractor
		   When I operate at the minimum forward speed
		   Then the Flying Tractor will rise to the minimum safe altitude