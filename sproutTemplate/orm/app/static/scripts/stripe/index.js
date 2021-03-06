

window.onload = function(){
    const stripe = Stripe('pk_test_51IRpyvJPjBOs8E64pYihjFwFCWL2vMWRyrQfBiZI01KgRUCZi2LBvgK1ek7UQ6Se1dOH4aX1wxlYHD0dYiiXakvh00y11w6iYv');
    const elements = stripe.elements();

    const checkoutButton = document.getElementById('checkout-button');

    checkoutButton.addEventListener('click', function() {
    // Create a new Checkout Session using the server-side endpoint you
    // created in step 3.
    fetch('/create-checkout-session', {
        method: 'POST',
    })
    .then(function(response) {
        console.log("hello");
        return response.json();
    })
    .then(function(session) {
        console.log("hello");
        return stripe.redirectToCheckout({ sessionId: session.id });
    })
    .then(function(result) {
        // If `redirectToCheckout` fails due to a browser or network
        // error, you should display the localized error message to your
        // customer using `error.message`.
        console.log("hello");
        if (result.error) {
        alert(result.error.message);
        }
    })
    .catch(function(error) {
        console.log("hello error");
        console.error('Error:', error);
    });
    });
}