#!/usr/bin/env python3
"""
Generate geographic hub pages for Nextract website
"""

from pathlib import Path

# Geographic hub data
GEOGRAPHIC_HUBS = {
    "e-commerce": [
        {
            "country": "USA", "slug": "ecommerce-usa",
            "title": "Nextract | E-commerce USA | Amazon, Walmart, Target",
            "description": "Extract e-commerce data from top USA retailers: Amazon, Walmart, Target, eBay, Best Buy. Real-time product data, pricing intelligence. Start free trial.",
            "keywords": "e-commerce scraping USA, Amazon US data, Walmart scraping, Target API, USA retail data, American e-commerce intelligence",
            "platforms": ["Amazon US", "Walmart", "Target", "eBay US", "Best Buy", "Shopify stores"],
            "cities": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"],
            "stats": "4,700+ Walmart stores, millions of Amazon products, 1,900+ Target locations"
        },
        {
            "country": "India", "slug": "ecommerce-india",
            "title": "Nextract | E-commerce India | Flipkart, Amazon, Myntra",
            "description": "Extract e-commerce data from top Indian platforms: Flipkart, Amazon India, Myntra, Ajio. Real-time product data. Available in all Indian cities. Start free.",
            "keywords": "e-commerce scraping India, Flipkart data, Amazon India API, Myntra scraping, Indian e-commerce data, online shopping India",
            "platforms": ["Flipkart", "Amazon India", "Myntra", "Ajio", "Nykaa"],
            "cities": ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai"],
            "stats": "500M+ internet users, fastest growing e-commerce market, 19,000+ pin codes"
        },
        {
            "country": "UAE", "slug": "ecommerce-uae",
            "title": "Nextract | E-commerce UAE | Noon, Amazon AE, Namshi",
            "description": "Extract e-commerce data from top UAE platforms: Noon, Amazon AE, Namshi. Real-time product data for Dubai, Abu Dhabi. AED pricing. Start free trial.",
            "keywords": "e-commerce scraping UAE, Noon data, Amazon UAE API, Namshi scraping, Dubai e-commerce data, UAE online shopping",
            "platforms": ["Noon", "Amazon AE", "Namshi", "Mumzworld"],
            "cities": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
            "stats": "98% internet penetration, $27B e-commerce market, fastest delivery in Middle East"
        },
    ],
    "quick-commerce": [
        {
            "country": "India", "slug": "quick-commerce-india",
            "title": "Nextract | Quick Commerce India | Blinkit, Zepto, Swiggy",
            "description": "Extract quick commerce data from India: Blinkit, Zepto, Swiggy Instamart, BigBasket. 10-minute delivery intelligence. All major cities. Start free trial.",
            "keywords": "quick commerce India, Blinkit data, Zepto scraping, Swiggy Instamart API, 10-minute delivery India, grocery delivery data India",
            "platforms": ["Blinkit", "Zepto", "Swiggy Instamart", "BigBasket", "Amazon Fresh India"],
            "cities": ["Delhi NCR", "Mumbai", "Bangalore", "Hyderabad", "Pune", "Chennai"],
            "stats": "$3.5B quick commerce market, 10-min delivery, 1,000+ dark stores"
        },
        {
            "country": "USA", "slug": "quick-commerce-usa",
            "title": "Nextract | Quick Commerce USA | Instacart, Gopuff, Amazon",
            "description": "Extract quick commerce data from USA: Instacart, Gopuff, Amazon Fresh, Whole Foods. Real-time grocery delivery intelligence. Start free trial today.",
            "keywords": "quick commerce USA, Instacart data, Gopuff scraping, Amazon Fresh API, grocery delivery USA, instant delivery data",
            "platforms": ["Instacart", "Gopuff", "Amazon Fresh", "Whole Foods", "Kroger Delivery"],
            "cities": ["New York", "Los Angeles", "Chicago", "San Francisco", "Miami"],
            "stats": "$30B+ grocery delivery market, 400+ cities covered, same-day delivery"
        },
        {
            "country": "UAE", "slug": "quick-commerce-uae",
            "title": "Nextract | Quick Commerce UAE | Talabat Mart, Instashop",
            "description": "Extract quick commerce data from UAE: Talabat Mart, Instashop, Careem NOW. Ultra-fast grocery delivery intelligence for Dubai, Abu Dhabi. Start free.",
            "keywords": "quick commerce UAE, Talabat Mart data, Instashop scraping, Careem NOW API, Dubai grocery delivery, UAE quick commerce",
            "platforms": ["Talabat Mart", "Instashop", "Careem NOW", "Noon Minutes"],
            "cities": ["Dubai", "Abu Dhabi", "Sharjah"],
            "stats": "15-minute delivery, $500M market, 100+ dark stores across Emirates"
        },
    ],
    "food-delivery": [
        {
            "country": "India", "slug": "food-delivery-india",
            "title": "Nextract | Food Delivery India | Swiggy, Zomato",
            "description": "Extract food delivery data from India: Swiggy, Zomato. Restaurant menus, prices, reviews. 500+ cities covered. Real-time delivery intelligence. Start free.",
            "keywords": "food delivery India, Swiggy data, Zomato scraping, restaurant data India, Indian food delivery API, menu scraping India",
            "platforms": ["Swiggy", "Zomato", "Swiggy Genie", "Zomato Gold"],
            "cities": ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Pune", "Chennai", "Kolkata"],
            "stats": "$4.2B food delivery market, 500+ cities, 150,000+ restaurant partners"
        },
        {
            "country": "USA", "slug": "food-delivery-usa",
            "title": "Nextract | Food Delivery USA | DoorDash, Uber Eats",
            "description": "Extract food delivery data from USA: DoorDash, Uber Eats, GrubHub. Restaurant menus, prices, delivery zones. 4,000+ cities. Start free trial today.",
            "keywords": "food delivery USA, DoorDash data, Uber Eats scraping, GrubHub API, restaurant data USA, American food delivery",
            "platforms": ["DoorDash", "Uber Eats", "GrubHub", "Postmates"],
            "cities": ["New York", "Los Angeles", "Chicago", "San Francisco", "Miami", "Seattle"],
            "stats": "$45B+ delivery market, 4,000+ cities, 1M+ restaurant partners"
        },
        {
            "country": "UAE", "slug": "food-delivery-uae",
            "title": "Nextract | Food Delivery UAE | Talabat, Deliveroo, Zomato",
            "description": "Extract food delivery data from UAE: Talabat, Deliveroo, Zomato UAE. Restaurant menus, prices. Dubai, Abu Dhabi coverage. Start free trial today.",
            "keywords": "food delivery UAE, Talabat data, Deliveroo UAE scraping, Zomato Dubai API, restaurant data UAE, Dubai food delivery",
            "platforms": ["Talabat", "Deliveroo", "Zomato UAE", "Careem Food"],
            "cities": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
            "stats": "$800M+ delivery market, 30,000+ restaurants, multi-cuisine coverage"
        },
        {
            "country": "UK", "slug": "food-delivery-uk",
            "title": "Nextract | Food Delivery UK | Deliveroo, Just Eat, Uber",
            "description": "Extract food delivery data from UK: Deliveroo, Just Eat, Uber Eats. Restaurant menus, prices. London, Manchester coverage. Start free trial today.",
            "keywords": "food delivery UK, Deliveroo data, Just Eat scraping, Uber Eats UK API, restaurant data UK, British food delivery",
            "platforms": ["Deliveroo", "Just Eat", "Uber Eats UK"],
            "cities": ["London", "Manchester", "Birmingham", "Edinburgh", "Bristol"],
            "stats": "£7B+ delivery market, 1,000+ cities, 100,000+ restaurants"
        },
        {
            "country": "Singapore", "slug": "food-delivery-singapore",
            "title": "Nextract | Food Delivery Singapore | GrabFood, Deliveroo",
            "description": "Extract food delivery data from Singapore: GrabFood, Deliveroo, Foodpanda. Restaurant menus, prices. Island-wide coverage. Start free trial today.",
            "keywords": "food delivery Singapore, GrabFood data, Deliveroo Singapore scraping, Foodpanda API, restaurant data Singapore",
            "platforms": ["GrabFood", "Deliveroo", "Foodpanda"],
            "cities": ["Singapore (island-wide coverage)"],
            "stats": "$1.5B delivery market, 50,000+ restaurants, 5.7M users"
        },
    ]
}

TEMPLATE = """---
layout: default
title: "{title}"
description: "{description}"
keywords: "{keywords}"
category: "{category}"
region: "{country}"
---

<main>

# {category_name} Data Scraping - {country}

{intro}

## Top Platforms in {country}

{platforms_list}

## What We Extract

### For {category_name} in {country}
{what_we_extract}

### Location-Specific Data
- **{currency_label}**: Prices in local currency ({currency})
- **Major Cities**: {cities}
- **Language Support**: {languages}
- **Local Regulations**: Compliant with {country} data protection laws

## Market Intelligence for {country}

{market_stats}

## API Endpoints

```
GET /api/v1/{api_base}/{country_code}/search?q={{query}}
GET /api/v1/{api_base}/{country_code}/trending
GET /api/v1/{api_base}/{country_code}/by-city/{{city}}
GET /api/v1/{api_base}/{country_code}/platform/{{platform}}
GET /api/v1/{api_base}/{country_code}/price-trends
```

## Use Cases for {country} Market

### Market Research
- **Local Trends**: Identify trending products/restaurants in {country}
- **Pricing Strategy**: Understand local pricing dynamics
- **Competition**: Analyze competitor presence and strategy
- **Expansion**: Evaluate market entry opportunities

### Business Intelligence
- **Geographic Analysis**: City-wise performance tracking
- **Demand Patterns**: Local consumer behavior insights
- **Seasonal Trends**: {country}-specific seasonal patterns
- **Platform Performance**: Compare platform market share

### Operations
- **Inventory Planning**: Optimize stock for {country} market
- **Pricing Optimization**: Local currency pricing strategy
- **Delivery Zones**: Map coverage across {country}
- **Partner Selection**: Choose best platforms for {country}

## Technical Specifications

### Coverage
- **Platforms**: {platform_count}+ major platforms
- **Cities**: {city_count}+ cities covered
- **Data Points**: Millions of products/restaurants tracked
- **Update Frequency**: Real-time to hourly updates

### API Performance
- **Response Time**: <200ms average
- **Regional Servers**: {country}-based infrastructure for low latency
- **Rate Limits**: Up to 100 requests/second
- **Uptime**: 99.9% SLA

### Data Quality
- **Accuracy**: 99.5%+ data accuracy
- **Currency**: Automatic {currency} conversion
- **Localization**: {country} address formats, phone numbers
- **Compliance**: {country} data protection regulations

## Code Examples

### Python - {country} Market Data

```python
import nextract

client = nextract.Client(api_key='your_api_key')

# Get trending items in {country}
trending = client.{api_base}.{country_code}.get_trending()
for item in trending:
    print(f"{{item['name']}} - {{item['price']}} {currency}")

# Search by city
results = client.{api_base}.{country_code}.search(
    city='{primary_city}',
    category='popular'
)
```

### Node.js - Multi-Platform Tracking

```javascript
const Nextract = require('nextract');
const client = new Nextract.Client('your_api_key');

// Track across multiple {country} platforms
const platforms = {platforms_array};

for (const platform of platforms) {{
  const data = await client.{api_base}.{country_code}.getPlatform(platform);
  console.log(`${{platform}}: ${{data.item_count}} items`);
}}
```

## {country} Market Insights

{market_insights}

## Supported Platforms

{platform_details}

## Geographic Coverage Details

{geographic_details}

## Compliance & Regulations

### {country} Data Protection
- **Local Laws**: Compliant with {country} data protection legislation
- **Privacy**: Follows {country} privacy regulations
- **Business Compliance**: Adheres to {country} business data usage laws
- **Security**: Data stored in accordance with {country} requirements

### Fair Use
- **Respectful Crawling**: Rate-limited, polite scraping
- **Public Data Only**: Only publicly available data
- **Terms Compliance**: Respects platform terms of service
- **Ethical Practices**: Transparent data collection

## Related Services

{related_services}

## Get Started with {country} Data

Ready to unlock {category_name} intelligence for the {country} market? Start your free trial today and gain competitive advantage with real-time data.

[Start Free Trial](#) | [API Documentation](#) | [Contact Sales](#) | [View Pricing](#)

</main>
"""

def generate_geographic_page(hub_data, category):
    """Generate a geographic hub page from template"""
    
    country = hub_data['country']
    
    # Category-specific content
    if category == "e-commerce":
        category_name = "E-commerce"
        api_base = "ecommerce"
        intro = f"Extract comprehensive e-commerce data from {country}'s leading online retail platforms. Access real-time product data, pricing intelligence, inventory levels, and customer reviews across all major e-commerce marketplaces in {country}."
        what_we_extract = """- **Product Data**: Titles, descriptions, images, specifications
- **Pricing**: Real-time prices, discounts, special offers
- **Reviews**: Customer ratings, review text, sentiment
- **Inventory**: Stock levels, availability by location
- **Sellers**: Seller information, marketplace data"""
        market_insights = f"""### {country} E-commerce Market
- {hub_data['stats']}
- Growing mobile commerce penetration
- Strong preference for express delivery
- Local and international brands mix"""
        
    elif category == "quick-commerce":
        category_name = "Quick Commerce"
        api_base = "quick_commerce"
        intro = f"Extract comprehensive quick commerce and grocery delivery data from {country}'s leading ultra-fast delivery platforms. Access real-time inventory, pricing, delivery zones, and dark store locations across {country}."
        what_we_extract = """- **Grocery Data**: Products, brands, categories, variants
- **Pricing**: Real-time prices, offers, bundle deals
- **Inventory**: Stock levels by dark store location
- **Delivery Zones**: Coverage maps, delivery times
- **Dark Stores**: Locations, service areas, capacity"""
        market_insights = f"""### {country} Quick Commerce Market
- {hub_data['stats']}
- Ultra-fast 10-15 minute delivery
- Dense dark store network in major cities
- Focus on daily essentials and groceries"""
        
    else:  # food-delivery
        category_name = "Food Delivery"
        api_base = "food_delivery"
        intro = f"Extract comprehensive food delivery data from {country}'s leading restaurant aggregators and delivery platforms. Access real-time restaurant data, menus, pricing, reviews, and delivery zone intelligence across {country}."
        what_we_extract = """- **Restaurant Data**: Names, cuisines, locations, ratings
- **Menus**: Dish names, prices, descriptions, categories
- **Reviews**: Customer ratings, review text, photos
- **Delivery Data**: Delivery zones, times, fees
- **Performance**: Order volumes, popularity metrics"""
        market_insights = f"""### {country} Food Delivery Market
- {hub_data['stats']}
- Multi-cuisine availability
- Growing cloud kitchen presence
- Peak demand during evenings and weekends"""
    
    # Generate platform list and details
    platforms_list = "\n".join([f"- **{platform}** - Full data extraction support" for platform in hub_data['platforms']])
    platform_details = "\n\n".join([f"### {platform}\n- Real-time menu/product data\n- Pricing and availability\n- Reviews and ratings" for platform in hub_data['platforms']])
    
    # Currency and language based on country
    currency_map = {
        "USA": ("USD", "$", "English"),
        "India": ("INR", "₹", "English, Hindi, and regional languages"),
        "UAE": ("AED", "AED", "English, Arabic"),
        "UK": ("GBP", "£", "English"),
        "Singapore": ("SGD", "S$", "English, Chinese, Malay, Tamil")
    }
    currency, currency_symbol, languages = currency_map.get(country, ("Local Currency", "", "Multiple languages"))
    
    # Country code for API
    country_code_map = {
        "USA": "us",
        "India": "in",
        "UAE": "ae",
        "UK": "uk",
        "Singapore": "sg"
    }
    country_code = country_code_map.get(country, country.lower())
    
    # Related services
    if category == "e-commerce":
        related_services = f"""- [E-commerce Data Solutions](/e-commerce.html) - Multi-platform e-commerce scraping
- [{hub_data['platforms'][0]} Scraper](/brands/{hub_data['platforms'][0].lower().replace(' ', '-')}-scraper) - Platform-specific data
- [Price Intelligence](/intelligence/price-intelligence) - Competitive pricing analytics"""
    elif category == "quick-commerce":
        related_services = f"""- [Quick Commerce Solutions](/quick-commerce.html) - Multi-platform quick commerce scraping
- [{hub_data['platforms'][0]} Scraper](/brands/{hub_data['platforms'][0].lower().replace(' ', '-')}-scraper) - Platform-specific data
- [Market Intelligence](/intelligence/market-intelligence) - Quick commerce trends"""
    else:
        related_services = f"""- [Food Delivery Solutions](/food-delivery.html) - Multi-platform food delivery scraping
- [{hub_data['platforms'][0]} Scraper](/brands/{hub_data['platforms'][0].lower().replace(' ', '-')}-scraper) - Platform-specific data
- [Restaurant Intelligence](/intelligence/restaurant-intelligence) - Menu and pricing analytics"""
    
    # Cities list
    cities = ", ".join(hub_data['cities'])
    
    # Geographic details
    geographic_details = f"""### Major Cities Covered
{chr(10).join([f"- **{city}** - Full platform coverage, real-time data" for city in hub_data['cities']])}

### Regional Coverage
- All major metropolitan areas
- Tier 2 and Tier 3 cities (where applicable)
- Suburban areas with platform presence
- Rural areas (limited coverage based on platform availability)"""
    
    # Market stats
    market_stats = f"""### Key Statistics
- {hub_data['stats']}
- Platform Coverage: {len(hub_data['platforms'])}+ major platforms
- Cities Tracked: {len(hub_data['cities'])}+ major cities
- Data Updates: Real-time to hourly frequency"""
    
    # Generate page content
    content = TEMPLATE.format(
        title=hub_data['title'],
        description=hub_data['description'],
        keywords=hub_data['keywords'],
        category=category.replace('-', ' ').title(),
        country=country,
        category_name=category_name,
        intro=intro,
        platforms_list=platforms_list,
        what_we_extract=what_we_extract,
        currency_label=currency,
        currency=currency_symbol,
        cities=cities,
        languages=languages,
        market_stats=market_stats,
        api_base=api_base,
        country_code=country_code,
        platform_count=len(hub_data['platforms']),
        city_count=len(hub_data['cities']),
        market_insights=market_insights,
        platform_details=platform_details,
        geographic_details=geographic_details,
        related_services=related_services,
        primary_city=hub_data['cities'][0],
        platforms_array=str([p.lower().replace(' ', '_') for p in hub_data['platforms'][:3]])
    )
    
    return content

def main():
    """Generate all geographic hub pages"""
    script_dir = Path(__file__).parent
    geographic_dir = script_dir / "geographic"
    geographic_dir.mkdir(exist_ok=True)
    
    total_created = 0
    
    for category, hubs in GEOGRAPHIC_HUBS.items():
        print(f"\n{'='*60}")
        print(f"Generating {category.upper()} geographic pages...")
        print(f"{'='*60}")
        
        for hub in hubs:
            filename = geographic_dir / f"{hub['slug']}.html"
            
            content = generate_geographic_page(hub, category)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"  ✓ Created {hub['country']} {category} -> {filename.name}")
            total_created += 1
    
    print(f"\n{'='*60}")
    print(f"✅ Generation complete! Created {total_created} geographic hub pages")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    main()
