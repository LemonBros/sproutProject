function myFunction() {
    document.getElementById("demo").innerHTML = "Hello World";
}
function addItem(){
    const userAction = async () => {
        document.getElementById("demo").innerHTML = "Hello World";
        var seed_id = {{ product.id }};
        var qtyElt = document.querySelectorAll('[aria-label="quantity"]')[0];
        var quantity = parseInt(qtyElt.options[qtyElt.selectedIndex].text, 10); 
        if(quantity > 0) {
            const response = await fetch(`{{url_for('add_to_cart')}}?seed_id=${seed_id}&quantity=${quantity}`, {
                //const response = await fetch(`{{url_for('add_to_cart')}}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            const myJson = await response.json(); //extract JSON from the http response
            // do something with myJson
            document.getElementById("demo").innerHTML = myJson["reply"];
        }
    }
    userAction()
}