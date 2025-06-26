# Importing required libraries:
import re  # For using regular expressions (e.g., extracting price digits)!
import requests  # To send HTTP requests to Amazon!
from bs4 import BeautifulSoup as bs  # To parse and extract data from HTML pages!

# Setting up headers to mimic a real browser request so Amazon doesn’t block it!
headers = {
    # Some optional headers are commented out, not required unless needed!
    #'authority': 'www.amazon.in',
    'method': 'GET',
    'scheme': 'https',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 ...',  # Browser identity string!
    'accept': 'text/html,application/xhtml+xml,...',  # Accepted content types!
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.amazon.in/',  # Referrer page!
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    # 'cookie': '',  # Can be added if Amazon blocks access!
}

# Main class to extract product information from Amazon product page!
class extractAmazon:
    def __init__(self, url):
        # Save the URL and fetch the page content (soup)!
        self.url = url
        self.soup = self.getSoup()

    def getSoup(self):
        # Try sending a GET request and parse the HTML with BeautifulSoup!
        try:
            response = requests.get(self.url, headers=headers)
            response.raise_for_status()  # Raises an error if status is not 200!
            return bs(response.content, "lxml")
        except requests.RequestException as e:
            print(f"Request Failure Detected! {e}")
            return None

    def getTitle(self):
        # Extract product title using its unique span id!
        tag = self.soup.select_one("span#productTitle")
        return tag.get_text(strip=True) if tag else ""

    def getAvailability(self):
        # Get availability status (e.g., "In stock" or "Currently unavailable")!
        if not self.soup:
            return ""
        tag = self.soup.select_one("#availability span")
        return tag.get_text(strip=True) if tag else ""

    def getOriginalPrice(self):
        # Get the original price before discount, if available!
        if not self.soup:
            return ""
        selectors = [
            "#priceblock_strikeprice",
            "span.a-text-price > span.a-offscreen",
            "span.a-price.a-text-price span.a-offscreen",
        ]
        for sel in selectors:
            tag = self.soup.select_one(sel)
        # Extract only numbers and decimals using regex!
        if tag:
            return re.sub(r"[^\d.]", "", tag.get_text(strip=True))
        return ""

    def getDiscountPercent(self):
        # Calculate and return discount percentage if both prices are available!
        try:
            current_price = float(self.getPrice())
            original_price = float(self.getOriginalPrice())
            if original_price > current_price:
                discount = ((original_price - current_price) / original_price) * 100
                return round(discount, 2)
        except:
            pass
        return 0.0

    def getPrice(self):
        # Get the current (final) product price!
        selectors = [
            "#priceblock_ourprice",
            "#corePriceDisplay_desktop_feature_div span.a-price-whole",
            "#corePrice_desktop span.a-offscreen"
        ]
        for sel in selectors:
            tag = self.soup.select_one(sel)
            if tag:
                return tag.get_text(strip=True).replace(",", "").replace("₹", "")
        return ""

    def getBrand(self):
        # Extract brand or manufacturer name!
        if not self.soup:
            return ""
        tag = self.soup.select_one("#bylineInfo")
        return tag.get_text(strip=True) if tag else ""

    def getImages(self):
        # Get the main image of the product!
        img = self.soup.select_one("div#imgTagWrapperId img")
        return [img['src']] if img and 'src' in img.attrs else []

    def getRating(self):
        # Extract star rating (e.g., "4.3 out of 5 stars")!
        tag = self.soup.select_one("span.a-icon-alt")
        return tag.get_text(strip=True) if tag else ""

    def getReviewCount(self):
        # Get the total number of customer reviews!
        tag = self.soup.select_one("span#acrCustomerReviewText")
        return tag.get_text(strip=True) if tag else ""

    def hasDeal(self, get_regular_price=False):
        # Check if there's a deal (like Lightning Deal, etc.)!
        deal_span = self.soup.select_one("#dealBadgeSupportingText")
        if get_regular_price:
            tag = self.soup.select_one("#corePrice_feature_div span.a-price-whole")
            return tag.get_text(strip=True) if tag else bool(deal_span)
        return bool(deal_span)

    def getCategory(self):
        # Extract the category trail (e.g., Electronics > Laptops)!
        if not self.soup:
            return []
        breadcrumb = self.soup.select("ul.a-unordered-list.a-horizontal.a-size-small li span.a-list-item")
        return [crumb.get_text(strip=True) for crumb in breadcrumb if crumb.get_text(strip=True)]

    def getFeatures(self):
        # Return a list of bullet points from the features section!
        if not self.soup:
            return []
        ul = self.soup.select_one("#feature-bullets ul")
        return [li.get_text(strip=True) for li in ul.select("li") if li.get_text(strip=True)] if ul else []

    def getSoldBy(self):
        # Return the name of the seller!
        if not self.soup:
            return ""
        tag = self.soup.select_one("#sellerProfileTriggerId")
        return tag.get_text(strip=True) if tag else ""

    def getDescription(self):
        # Get product description from one of several possible places!
        if not self.soup:
            return ""
        tag = self.soup.select_one("#productDescription p")
        if tag and tag.get_text(strip=True):
            return tag.get_text(strip=True)
        tag = self.soup.select_one("#productDescription")
        if tag and tag.get_text(strip=True):
            return tag.get_text(strip=True)
        # If no description found, fallback to first 2 feature bullet points!
        bullets = self.getFeatures()
        if bullets:
            return " ".join(bullets[:2])
        return ""
