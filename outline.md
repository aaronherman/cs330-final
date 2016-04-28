# Final project


* Flask-OAuth/openID or Flask-Login - login, if necessary. could just use guest accounts
* Flask-paypal - payment
* Flask-WTF - select size, color, price
 * filter by: illustration, digital, nature, photography, landscape, abstract, painting
* Flask-mail - send receipt

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
* history? for items that aren't originals?
 * how many sold
 * inventory
 * when it'll be back in stock


##### Pages
1. index
 * title
 * carousel - pictures of what's been drawn
 * sign in
2. discover
 * brings you to a page of more of artwork
 * show me: popular, new, random
3. item-view
 * all info from the "item" table
 * "buy"
4. checkout/confirmation
