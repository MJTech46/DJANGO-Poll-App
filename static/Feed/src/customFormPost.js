//for form submition
function postForm(formId, url) {
    const form = document.getElementById(formId);
    if (!form) {
        console.error('Form not found!');
        return;
    }
    const formData = new FormData(form);  // Create a FormData object from the form
    fetch(url, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())  // Parse the JSON response
    .then(data => {
        console.log('Success:', data);  // Handle the response data
        //for displaying alerts
        const alertDiv = document.getElementById(`alert-${formId}`);
        const alertHTML = `
            <div class="alert alert-success alert-dismissible fade show " role="alert">
                <strong>Your response was recorded.</strong>
                <br>
                Press 'Vote' button again to save changes if any.
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        `;
        alertDiv.innerHTML = alertHTML;
    })
    .catch(error => {
        console.error('Error:', error);  // Handle any errors
    });
}

//for setting EventListener for all form
const allForms = document.querySelectorAll("form")
allForms.forEach(function(form){
    form.addEventListener('submit', function(event) {
        event.preventDefault();  // Prevent the default form submission
        postForm(form.id, form.action);
    });
});
