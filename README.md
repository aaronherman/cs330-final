# Final project


* Flask-paypal
* Flask-WTF - used to gather contact information, and receive information for purchase
 * Could be used to select size, color, price or filter by: illustration, digital, nature, photography, landscape, abstract, painting
* Flask-mail - send receipt taken from WTForms

##### database - SqlAlchemy/postgres - 
* item
  * id
  * name
  * price
  * material
  * size
* descriptions
  * id 
  * colors
  * description
  * image
* history
 * how many sold
 * inventory

##### Pages
1. index
 * title
 * carousel - pictures of what's been drawn
2. discover
 * brings you to a page of more of artwork
3. item-view
 * all info from the "item" table
 * "buy"
4. checkout/confirmation





#####Purchase Page######

1. Have a button that calls a js function, passing in the item name
2. The js function will make an xml request back to the server
3. The function will send the name of the item so the server knows which item is being purchased
4. The server will go through the database and get the information for that item
5. It will then render_template "buy.html" and also send any information the page needs (i.e. return render_template("buy.html", information=information)
6. The js function will then render content allowing the user to buy that item
