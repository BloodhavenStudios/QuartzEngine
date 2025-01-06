fetch("/QuartzEngine/assets/topnav")
	.then(response => response.text())
	.then(html => {
		document.getElementById("topnav").innerHTML = html;
	})
	.catch(error => {
		console.error("Error loading navbar:", error);
	});

fetch("/QuartzEngine/assets/footer")
	.then(response => response.text())
	.then(html => {
		document.getElementById("footer").innerHTML = html;
	})
	.catch(error => {
		console.error("Error loading footer:", error);
	});