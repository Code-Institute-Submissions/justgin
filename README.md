<span>
    <img src="static/img/jG.png" width="auto" height="100px">
    <h1>justGin</h1>
</span>


You guessed it. 

We sell gin.

Our shop is going to get bigger, and it's going to get harder to choose. justGin is a project, developed as part of my (William Marjoribanks') fourth and final Milestone within the curriculum at Code Institute, Dublin.

It has been deployed to [Github Pages]() and [Heroku]().

---

## README Document Navigation

* [UX](#ux)
  * [Concept](#concept)
  * [User Stories](#user-stories)
  * [Wireframes](#wireframes)
  * [File Structure](#file-structure)
  * [Design](#design)
    * [Colour Scheme](#colour-scheme)
    * [Typography](#typography)
    * [Imagery](#imagery)
* [Features](#features)
  * [Existing Features](#existing-features)
  * [Future Implementations](#future-implementations)
* [Technologies Used](#technologies)
  * [Languages and Frameworks](#languages-and-frameworks)
  * [Libraries and Programs](#libraries-and-programs)
  * [Code Validation](#code-validation)
* [Testing](#testing)
* [Deployment](#deployment)
    * [Local Deployment](#local-deployment)
    * [Deployment to Heroku](#heroku-deployment)
* [Media](#media)
* [Acknowledgements](#acknowledgements)

---

## UX
### Concept

It's been a really horrid year for everyone this year. Unless of course, you've enjoyed not having to make small talk at work during your half-hour break or commuting every day in the pouring rain - justGin is based in Scotland, so it  <em>always</em> rains. <strong>Always</strong>. 
<br>

But now that society is regaining a slice of freedom by the week, and restrictions aren't as strict. It's time to celebrate - safely and responsibly. And why not with a bottle (or two) of premium artisanal gin? Well justGin, provides their users with a platform to do just that at affordable prices and some advice on pairings and flavour notes.

### User Stories

#### As a Customer

| **As a customer and/or mixologist I would like to** | **So I Can**                            |
| -------------------------------------------------- | --------------------------------------------- |
| Browse products.                                   | Search for new and already tried gins.        |
| Filter products by origin, price, name             | Compare the choices between justGin and other resellers.                                                                                                 |
| Search for Gin using the search bar                | Filter Gin by a descriptive keyword.|
| See details about a product.                       | Make a responsible purchasing decision.       |
| Buy a product from the shop.                       | Enjoy and share it with others.               |
| View my shopping cart before purchasing.           | See a cost breakdown before the purchase.     |
| Update my shopping cart.                           | Make any final decisions before ordering.     |
| Pay via a credit/debit card.                       | Complete a purchase.                          |
| Receive an email confirmation about my order       | To be provided with proof of purchase for any potential issues.|
| Create an account.                                 | To speed up future orders and view past orders.|
| Amend my account details.                          | Be informed about orders and offers by justGin.|
| View my order history                              | be reminded of previous purchases.            |
| See what is new to the store.                      | Try the newest gins to share with others.     |

<br>

#### User Stories for Shop Administrators

| **As an Administrator I would like to**     | **So I Can**                                     |
| ------------------------------------------- | ------------------------------------------------ |
| Add/Update/Remove new/existing products in the store. | Ensuring stock is relevant.            |
| Retrieve customer purchases.                | Complete the order and send the item out to the customer.|
| Mark a product as clearance/sale or new.    | Ensure customers have the best deals to premium quality alchohol, supporting local businesses.             |

### Wireframes

The wireframes created with [Balsamiq]('https://balsamiq.com') at the beginning of the project and used as a reference throughout are situated in a dedicated folder entitled 
['wireframes'](https://github.com/LHBank/justgin/tree/master/wireframes), at project level. It contains screenshot images, for both the Mobile, Tablet, and Desktop viewport screen sizes, due to the use of Bootstrap 4, and the prioritisation on Mobile-first devices.

### Database Structure

<img src="static/img/db_structure.png">

### Design

A custom CSS file, placed within the static folder of justGin, was used in conjunction with [Bootstrap 4](https://getbootstrap.com/docs/4.5/getting-started/introduction/), which served as the main CSS library. [Materialize](https://materializecss.com/) was also used, however only for use of its vast library of icons. [Animate.css](https://animate.style/) was also utilised on the home page or, index.html within the home app, for the entry tagline and shop now button. It wasn't used anywhere else, as I felt it had a bigger impact by being used less. [Animate On Scroll](https://michalsnik.github.io/aos/) was used only on the products page, to show products only as the user scrolled down the page.

### Colour Scheme

As with all online platforms, a consistent colour palette is fundamental to a satisfying user experience. There are different outcomes when using the right colour scheme and with trying to keep a sense of elegance and style within the site, is why this particular colour palette was chosen from [Coolors](https://coolors.co/). Three of the five colours presented were predominantly used.

* 'Copper Crayola' was used throughout for headings, buttons and the ratings feature - which is how a product on the site is graded, by the admin user.

* 'Dark Jungle Green' was used as an alternative to black. 

* 'Peach' was used as an alternative to white. Although dependent on the responsiveness in screen size, #FAFAFA - an off-white - was also used as a more effective contrasting colour.

<div>
    <img src="static/img/palette.png" width="550px" height="100px" alt="Colour Palette">
</div>

The 'update', 'edit' or 'delete' links utilised standard conventions of green, red and blue. These colours were also used against the Toast feature, to demonstrate the success or failure of an item being added or removed from the shopping cart.

<div>
    <img src="static/img/palette2.png" width="550px" height="auto" alt="Colour Palette">
</div>


### Typography

Text content throughout the site was kept to a minimum of two font-families. All headings utilised the Spartan font-familiy from GoogleFonts, and likewise, all links/inputs/paragraph elements used Quicksand, also from GoogleFonts. There were subtle contrasts between the two fonts, yet weren't garish or difficult to read.

### Imagery

The imagery used, had to be of good quality to convey a message that any orders from justGin, were providing only premium brand products. It was also therefore important, that distracting CSS was kept to a minimum and imagery, was simple, relying partly too on the description provided. A simple layout, with minimal pastel colours brought the design, an element of elegance and sophistication.

