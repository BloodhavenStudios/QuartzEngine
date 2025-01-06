fetch("assets/navbar")
	.then(response => response.text())
	.then(html => {
		document.getElementById("topnav").innerHTML = html;
	})
	.catch(error => {
		console.error("Error loading navbar:", error);
	});