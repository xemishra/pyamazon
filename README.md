<h1 align="center"><b>PyAmazon</b></h1>

<p align="center"><img src="https://graph.org/file/8104985cc47599f76467c-f5774b7caeecabfa56.jpg" alt="PyAmazon" width="700"></p>

<h2 align="center">Effortlessly extract Amazon product data with Python.</h3>

# 📦 About PyAmazon
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
print("🛍️ Title:", x.getTitle())                       # Product title
print("📦 Availability:", x.getAvailability())         # Availability status (e.g., "In stock")
print("🏷️ Brand:", x.getBrand())                       # Brand name
print("🧭 Category:", x.getCategory())                 # Product category / breadcrumb
print("🔹 Features:", x.getFeatures())                 # Bullet points / features
print("💸 Original Price:", x.getOriginalPrice())     # MRP or strike-through price
print("💰 Current Price:", x.getPrice())               # Final/current selling price
print("🔻 Discount Percent:", x.getDiscountPercent()) # Calculated discount percentage
print("📝 Description:", x.getDescription())           # Product description
print("⭐ Rating:", x.getRating())                      # Star rating (e.g., "4.3 out of 5 stars")
print("🏪 Sold By:", x.getSoldBy())                    # Seller information
print("🧮 Review Count:", x.getReviewCount())          # Total number of reviews
print("🖼️ Images:", x.getImages())                     # Product image URLs
print("🔥 Has Deal:", x.getHasDeal())                     # Whether a deal badge is shown
```
