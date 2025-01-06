const copy_text = function(text) {
    // Create a temporary textarea to copy text
    const tempTextarea = document.createElement("textarea");
    tempTextarea.value = text; // Get text from the <p> element
    document.body.appendChild(tempTextarea); // Append to the DOM

    // Select and copy the text
    tempTextarea.select();
    document.execCommand('copy');

    // Remove the temporary textarea
    document.body.removeChild(tempTextarea);
    delete tempTextarea;

	alert("Copied Command to Clipboard.\nThanks for installing Quartz Engine!")
}

const site_api = "https://formidable-vitia-bloodhavenstudios-038c64f8.koyeb.app/api";
const downloadsEndpoint = site_api + "/downloads";
const uploadsEndpoint = site_api + "/uploads";

const start_download = function(type) {
	if (type === "pip") {
		copy_text("pip install quartz")
	} else if (type === "pip+git") {
		copy_text("pip install git+https://github.com/BloodhavenStudios/QuartzEngine")
	} else {}
	updateStat(downloadsEndpoint, 1)
}

function autoFetchNumbers(interval = 5000) {
    async function fetchStats() {
		if (document.getElementById("downloads-count") && document.getElementById("uploads-count")) {
			try {
				const downloadsResponse = await fetch(downloadsEndpoint);
				const uploadsResponse = await fetch(uploadsEndpoint);

				if (downloadsResponse.ok && uploadsResponse.ok) {
					const downloadsData = await downloadsResponse.json();
					const uploadsData = await uploadsResponse.json();

					// Update the UI
					document.getElementById("downloads-count").textContent = downloadsData.downloads || 0;
					document.getElementById("uploads-count").textContent = uploadsData.uploads || 0;
				} else {
					console.error("Failed to fetch stats:", downloadsResponse, uploadsResponse);
				}
			} catch (error) {
				console.error("Error fetching stats:", error);
			}
		} else {
			console.warn(`Element not found.`);
		}
    }

    fetchStats();
    setInterval(fetchStats, interval);
}

async function updateStat(endpoint, operation) {
    try {
        const response = await fetch(endpoint, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ operation }),
        });

        if (response.ok) {
            const data = await response.json();
            console.log(data.message || "Operation successful");
        } else {
            console.error("Failed to update stat:", await response.json());
        }
    } catch (error) {
        console.error("Error updating stat:", error);
    }
}

autoFetchNumbers(5000);

document.addEventListener("DOMContentLoaded", () => {
    const downloadButtons = [
        { id: "download-1", type: "git" },
        { id: "download-2", type: "pip" },
        { id: "download-3", type: "pip+git" }
    ];

    downloadButtons.forEach(({ id, type }) => {
        const button = document.getElementById(id);
        if (button) {
            button.addEventListener("click", () => {
                start_download(type);
            });
        } else {
            console.warn(`Element with ID "${id}" not found.`);
        }
    });
});

setTimeout(() => {
	
	const path = window.location.pathname;
	
	const add_selected = function(id) {
		document.getElementById(id).classList.add("selected");
	}
	
	switch (path) {
		case "/QuartzEngine/":
			add_selected("topnav-home")
			break;
		case "/QuartzEngine/about":
			add_selected("topnav-about")
			break;
		case "/QuartzEngine/releases":
			add_selected("topnav-releases")
			break;
		case "/QuartzEngine/docs":
			add_selected("topnav-docs")
			break;
		case "/QuartzEngine/samples":
			add_selected("topnav-samples")
			break;
		case "/QuartzEngine/made-with-quartz":
			add_selected("topnav-quartz")
			break;
		default:
			break;
	}

	console.log("wait complete.");
}, 500);