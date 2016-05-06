function Buy(itemname) {
alert("Called function to buy item");
    var item = itemname;
    alert(item);

     var obj = new XMLHttpRequest();
        obj.open("POST", "/buy", true);



        obj.send(JSON.stringify({item: item}));
        obj.onreadystatechange = function () {
            if (obj.readyState == 4 && obj.status == 200) {
                alert("Successfully called server");
            }
}};