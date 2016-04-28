# Final project


* Flask-OAuth/openID or Flask-Login - login, if necessary. could just use guest accounts
* Flask-paypal - payment
* Flask-WTF - select size, color, price
 * filter by: illustration, digital, nature, photography, landscape, abstract, painting


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


##### Pages
1. index
 * title
 * carousel - pictures of what's been drawn
 * sign in
2. discover
 * brings you to a page of more of artwork
3. item-view
 * all info from the "item" table
 * "buy"
4. checkout/confirmation
