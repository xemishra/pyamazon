<h1 align="center"><b>PyAmazon</b></h1>

<p align="center"><img src="https://graph.org/file/8104985cc47599f76467c-f5774b7caeecabfa56.jpg" alt="PyAmazon" width="700"></p>

<h2 align="center">Effortlessly extract Amazon product data with Python.</h3>

# About PyAmazon
PyAmazon is a lightweight yet powerful Python module designed to extract structured product information from Amazon product pages. Whether you're building price trackers, analytics tools, or e-commerce scrapers, PyAmazon offers a clean and reliable interface for accessing titles, pricing, ratings, reviews, availability, images, discounts, and more — all from a single Amazon URL.

Built using requests and BeautifulSoup, the module requires no API key or authentication and is tailored for simplicity, accuracy, and extensibility. It supports Indian and global Amazon domains, making it ideal for both personal and production use.

# Installation
```bash
pip install pyamazon
```

# Example Usage
```python
from pyamazon import extractAmazon  # Import the extractor class

# Create an object with your Amazon product URL
x = extractAmazon("https://amzn.in/d/jbx0FnF")

# Extract and print various details
print("Title:", x.getTitle())                       # Product title
print("Availability:", x.getAvailability())         # Availability status (e.g., "In stock")
print("Brand:", x.getBrand())                       # Brand name
print("Category:", x.getCategory())                 # Product category / breadcrumb
print("Features:", x.getFeatures())                 # Bullet points / features
print("Original Price:", x.getOriginalPrice())     # MRP or strike-through price
print("Current Price:", x.getPrice())               # Final/current selling price
print("Discount Percent:", x.getDiscountPercent()) # Calculated discount percentage
print("Description:", x.getDescription())           # Product description
print("Rating:", x.getRating())                      # Star rating (e.g., "4.3 out of 5 stars")
print("Sold By:", x.getSoldBy())                    # Seller information
print("Review Count:", x.getReviewCount())          # Total number of reviews
print("Images:", x.getImages())                     # Product image URLs
print("Has Deal:", x.getHasDeal())                     # Whether a deal badge is shown
```

# Methods
| Method                             | Description                                                             |
| ---------------------------------- | ----------------------------------------------------------------------- |
| `getTitle()`                       | Returns the product title as a string.                                  |
| `getAvailability()`                | Returns the availability status (e.g., "In stock", "Out of stock").     |
| `getBrand()`                       | Extracts the brand or seller name.                                      |
| `getCategory()`                    | Returns a list of product categories (breadcrumb path).                 |
| `getFeatures()`                    | Returns a list of feature bullet points.                                |
| `getOriginalPrice()`               | Extracts the original MRP or strike-through price.                      |
| `getPrice()`                       | Gets the current/final price.                                           |
| `getDiscountPercent()`             | Calculates and returns the discount percentage.                         |
| `getDescription()`                 | Returns a short description or summary of the product.                  |
| `getRating()`                      | Returns the star rating (e.g., "4.2 out of 5 stars").                   |
| `getReviewCount()`                 | Returns total number of customer reviews.                               |
| `getImages()`                      | Returns a list of product image URLs.                                   |
| `getSoldBy()`                      | Returns the seller or fulfillment info (e.g., "Fulfilled by Amazon").   |
| `getHasDeal()`                     | Checks if a deal is active. Optionally returns regular price if `True`. |

#  Features
- URL-Based Scraping – Extract product data from any Amazon product URL effortlessly.
- Title Extraction – Get the full product title in clean text.
- Price & Discount – Fetch current price, original price (MRP), and auto-calculated discount percentage.
- Availability Status – Know whether a product is in stock or unavailable.
- Product Description – Retrieve the official product description or summary.
- Feature Bullets – Get a list of key product features.
- Ratings & Reviews – Extract average rating and total number of reviews.
- Image URLs – Grab high-resolution product images.
- Brand Name – Detect the brand or seller mentioned on the product page.
- Category Path – Extract the product’s full category hierarchy (breadcrumb).
- Deal Detection – Identify if a product is currently under a deal or promotion.
- Sold By Info – Get the seller name (e.g., "Fulfilled by Amazon").
- Structured Output – Access all product data in a clean Python dict format.
- Multi-domain Friendly – Works on amazon.in, amazon.com, and other country-specific domains.
- Lightweight & No API Key Needed – Pure scraping using requests and BeautifulSoup, no authentication required.

# Disclaimer
This project is intended for educational and personal use only.
PyAmazon is not affiliated with Amazon in any way.
Product data is extracted by parsing publicly available HTML, which may change over time.
If Amazon updates their website structure, some features of this module may stop working.
Please do not use this tool for spamming, scraping at scale, or violating Amazon’s Terms of Service.
Use responsibly, respectfully, and at your own risk.

<h1 align="center">Made with ❤️ by <a href="https://github.com/xemishra">Shivanand Mishra</a></h1>
