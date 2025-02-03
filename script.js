document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("feedbackForm").addEventListener("submit", function (e) {
        e.preventDefault(); // Prevent default form submission behavior

        // Collect form data
        let formData = new FormData();
        formData.append("name", document.getElementById("name").value);
        formData.append("roll", document.getElementById("roll").value);
        formData.append("feedback", document.querySelector('input[name="feedback"]:checked')?.value || "No response");
        formData.append("message", document.getElementById("message").value);

        // Google Apps Script Web App URL
        const scriptURL = "https://script.google.com/macros/s/AKfycbx6kyqzADScbWdnkjF54XiZFN2v_5Js2KLNiqxdJrvJxfbuoFr3Q5_TjlbU6y4KVV2_/exec";

        // Send data to Google Sheets
        fetch(scriptURL, {
            method: "POST",
            body: formData
        })
        .then(response => response.text())
        .then(data => {
            alert("Form submitted successfully!");
            document.getElementById("feedbackForm").reset();
        })
        .catch(error => {
            console.error("Error:", error);
            alert("There was an error submitting the form.");
        });
    });
});
