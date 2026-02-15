#!/usr/bin/env python3
"""
Generate case study pages for Nextract website
"""

from pathlib import Path

# Case study data (focused on e-commerce, quick commerce, food delivery)
CASE_STUDIES = {
    "e-commerce": [
        {
            "slug": "amazon-pricing-intelligence-25-percent-revenue",
            "title": "Nextract | 25% Revenue Boost | E-commerce Case Study",
            "description": "How a D2C brand increased revenue by 25% using Amazon pricing intelligence from Nextract. Real-time competitor tracking across 15 marketplaces.",
            "keywords": "Amazon pricing intelligence, e-commerce case study, competitor price tracking, revenue growth, dynamic pricing",
            "client": "Leading D2C Electronics Brand",
            "industry": "Consumer Electronics",
            "challenge": "Manual price monitoring across 15 Amazon marketplaces was time-consuming and led to missed opportunities. Competitors were adjusting prices 20-30 times daily.",
            "solution": "Implemented Nextract's Amazon API with real-time price tracking for 500+ competitor products across US, UK, Germany, France, Spain, Italy, India marketplaces. Automated alerts for price changes.",
            "results": [
                "25% increase in revenue within 3 months",
                "30% improvement in competitive win rate",
                "Real-time tracking of 500+ competitor SKUs",
                "Automated pricing decisions based on live data",
                "ROI achieved in 6 weeks"
            ],
            "metrics": {
                "revenue_increase": "25%",
                "win_rate": "30%",
                "products_tracked": "500+",
                "roi_period": "6 weeks"
            }
        },
        {
            "slug": "walmart-inventory-optimization-3m-savings",
            "title": "Nextract | $3M Cost Savings | Walmart Case Study",
            "description": "Retail chain saved $3M annually by optimizing inventory using Walmart marketplace intelligence. Real-time stock tracking across 4,700+ stores.",
            "keywords": "Walmart inventory optimization, retail case study, supply chain intelligence, cost savings, inventory management",
            "client": "National Retail Chain",
            "industry": "Retail & Distribution",
            "challenge": "Inefficient inventory management led to stockouts and overstock situations. Lacked visibility into competitor inventory levels and regional demand patterns.",
            "solution": "Deployed Nextract's Walmart scraping solution tracking inventory levels, pricing, and demand signals across 4,700+ stores. Integrated with existing ERP system.",
            "results": [
                "$3M annual cost savings from optimized inventory",
                "40% reduction in stockout situations",
                "25% decrease in excess inventory costs",
                "Real-time tracking across 4,700+ store locations",
                "2-week implementation timeline"
            ],
            "metrics": {
                "cost_savings": "$3M",
                "stockout_reduction": "40%",
                "stores_tracked": "4,700+",
                "implementation": "2 weeks"
            }
        },
        {
            "slug": "shopify-competitive-intelligence-10x-sales",
            "title": "Nextract | 10x Sales Growth | Shopify Case Study",
            "description": "Fashion brand achieved 10x sales growth by analyzing 50,000+ Shopify stores. Product trends, pricing strategies, and market gaps identified.",
            "keywords": "Shopify competitive intelligence, fashion e-commerce, market analysis, sales growth, trend forecasting",
            "client": "Emerging Fashion Brand",
            "industry": "Fashion & Apparel",
            "challenge": "New market entrant needed to identify trending products, optimal pricing, and market gaps across competitive landscape of 50,000+ Shopify stores.",
            "solution": "Implemented comprehensive Shopify scraping across 50,000+ fashion stores. Analyzed product trends, pricing strategies, bestsellers, and customer reviews.",
            "results": [
                "10x sales growth in 12 months",
                "Identified 15 high-demand product categories",
                "Optimized pricing strategy across 200+ SKUs",
                "Analyzed 50,000+ competitive stores",
                "3-month market analysis completed"
            ],
            "metrics": {
                "sales_growth": "10x",
                "product_categories": "15",
                "stores_analyzed": "50,000+",
                "analysis_period": "3 months"
            }
        },
        {
            "slug": "flipkart-market-entry-strategy-success",
            "title": "Nextract | Market Entry Success | Flipkart Case Study",
            "description": "International brand successfully entered Indian market using Flipkart intelligence. Analyzed 100K+ products across 50 categories for optimal positioning.",
            "keywords": "Flipkart market entry, India e-commerce strategy, competitive analysis, market research, product positioning",
            "client": "International Consumer Goods Brand",
            "industry": "Consumer Goods",
            "challenge": "Entering the Indian e-commerce market without local insights. Needed to understand pricing, competition, and consumer preferences across categories.",
            "solution": "Comprehensive Flipkart market analysis tracking 100,000+ products across 50 categories. Analyzed pricing, reviews, seller strategies, and seasonal trends.",
            "results": [
                "Successful market entry in top 3 categories",
                "Achieved 5% market share in 6 months",
                "Analyzed 100K+ products for positioning",
                "Identified optimal price points for 200+ SKUs",
                "Generated $2M in first-year revenue"
            ],
            "metrics": {
                "market_share": "5%",
                "products_analyzed": "100K+",
                "categories": "50",
                "first_year_revenue": "$2M"
            }
        },
        {
            "slug": "ebay-seller-optimization-200-percent-profit",
            "title": "Nextract | 200% Profit Increase | eBay Case Study",
            "description": "eBay power seller increased profit by 200% using competitive intelligence. Real-time tracking of 10,000+ listings across 20 categories.",
            "keywords": "eBay seller optimization, marketplace intelligence, profit maximization, listing optimization, competitive pricing",
            "client": "eBay Power Seller",
            "industry": "Online Marketplace Selling",
            "challenge": "Managing 10,000+ listings manually was inefficient. Needed real-time competitor insights to optimize pricing and listings for maximum profitability.",
            "solution": "Automated eBay data extraction tracking competitor pricing, sold listings, best offers, and seasonal trends across 20 categories with 10,000+ active listings.",
            "results": [
                "200% increase in profit margins",
                "50% faster listing optimization",
                "Real-time tracking of 10,000+ competitor listings",
                "Automated repricing for 5,000+ SKUs",
                "4-week ROI achievement"
            ],
            "metrics": {
                "profit_increase": "200%",
                "optimization_speed": "50%",
                "listings_tracked": "10,000+",
                "roi_period": "4 weeks"
            }
        }
    ],
    "quick-commerce": [
        {
            "slug": "blinkit-dark-store-optimization-40-percent-efficiency",
            "title": "Nextract | 40% Efficiency Gain | Blinkit Case Study",
            "description": "Dark store operator improved efficiency by 40% using Blinkit delivery intelligence. Optimized inventory across 50+ locations in Delhi NCR.",
            "keywords": "Blinkit dark store optimization, quick commerce efficiency, inventory management, delivery zone analysis, 10-minute delivery",
            "client": "Dark Store Operator",
            "industry": "Quick Commerce",
            "challenge": "Managing inventory across 50+ dark stores without visibility into competitor stock levels, demand patterns, and delivery zone coverage.",
            "solution": "Deployed Nextract's Blinkit scraping solution tracking inventory, pricing, delivery zones, and demand patterns across Delhi NCR. Real-time alerts for stockouts.",
            "results": [
                "40% improvement in operational efficiency",
                "30% reduction in stock wastage",
                "Optimized inventory across 50+ locations",
                "Real-time competitor monitoring in 10+ zones",
                "25% increase in delivery success rate"
            ],
            "metrics": {
                "efficiency_gain": "40%",
                "waste_reduction": "30%",
                "locations": "50+",
                "delivery_improvement": "25%"
            }
        },
        {
            "slug": "zepto-market-expansion-15-city-success",
            "title": "Nextract | 15 Cities Launched | Zepto Case Study",
            "description": "Quick commerce startup successfully launched in 15 cities using Zepto competitive intelligence. Analyzed 200+ dark store locations for optimal placement.",
            "keywords": "Zepto market expansion, quick commerce strategy, dark store placement, city launch strategy, competitive analysis",
            "client": "Quick Commerce Startup",
            "industry": "Grocery Delivery",
            "challenge": "Planning expansion into 15 new cities without local market knowledge. Needed to identify optimal dark store locations and product mix.",
            "solution": "Comprehensive Zepto market analysis across existing cities. Mapped 200+ dark store locations, delivery zones, popular products, and pricing strategies.",
            "results": [
                "Successfully launched in 15 cities",
                "Achieved profitability in 8/15 cities within 6 months",
                "Analyzed 200+ dark store locations",
                "Optimized product mix for each city",
                "$5M in first-year revenue from new cities"
            ],
            "metrics": {
                "cities_launched": "15",
                "profitable_cities": "8/15",
                "stores_analyzed": "200+",
                "first_year_revenue": "$5M"
            }
        },
        {
            "slug": "instacart-pricing-strategy-35-percent-margin",
            "title": "Nextract | 35% Margin Increase | Instacart Case Study",
            "description": "Grocery retailer increased margins by 35% using Instacart pricing intelligence. Multi-store pricing optimization across 50+ metro areas.",
            "keywords": "Instacart pricing strategy, grocery delivery optimization, multi-store pricing, margin improvement, competitive intelligence",
            "client": "Regional Grocery Chain",
            "industry": "Grocery Retail",
            "challenge": "Competing on Instacart required dynamic pricing across multiple store locations. Manual price monitoring was inefficient and led to margin erosion.",
            "solution": "Implemented Nextract's Instacart API tracking prices across 50+ metro areas, 1,000+ competitor stores, and 10,000+ SKUs with automated repricing rules.",
            "results": [
                "35% increase in profit margins",
                "Real-time pricing across 50+ metro areas",
                "Monitored 1,000+ competitor stores",
                "Automated repricing for 10,000+ SKUs",
                "8-week implementation and ROI"
            ],
            "metrics": {
                "margin_increase": "35%",
                "metro_areas": "50+",
                "competitor_stores": "1,000+",
                "skus_tracked": "10,000+"
            }
        },
        {
            "slug": "swiggy-instamart-expansion-intelligence",
            "title": "Nextract | Market Intelligence | Swiggy Instamart Study",
            "description": "FMCG brand optimized distribution using Swiggy Instamart intelligence. Analyzed inventory across 300+ dark stores in 25 cities.",
            "keywords": "Swiggy Instamart intelligence, FMCG distribution, dark store analysis, quick commerce distribution, inventory optimization",
            "client": "Leading FMCG Brand",
            "industry": "Consumer Packaged Goods",
            "challenge": "Poor visibility into inventory levels and demand patterns across Swiggy Instamart's 300+ dark stores in 25 cities. Missing sales opportunities.",
            "solution": "Deployed comprehensive Swiggy Instamart tracking solution monitoring inventory, pricing, out-of-stock situations, and demand patterns across all locations.",
            "results": [
                "45% reduction in out-of-stock situations",
                "Optimized distribution across 300+ stores",
                "Real-time inventory tracking in 25 cities",
                "20% increase in sales through better availability",
                "$3M additional annual revenue"
            ],
            "metrics": {
                "stock_improvement": "45%",
                "stores_tracked": "300+",
                "cities": "25",
                "revenue_increase": "$3M"
            }
        },
        {
            "slug": "bigbasket-assortment-optimization-success",
            "title": "Nextract | Assortment Success | BigBasket Case Study",
            "description": "Grocery brand optimized product assortment using BigBasket intelligence. Analyzed 30,000+ products across 25 categories for portfolio decisions.",
            "keywords": "BigBasket assortment optimization, grocery intelligence, product portfolio, category analysis, demand forecasting",
            "client": "Grocery Products Manufacturer",
            "industry": "Food & Beverage",
            "challenge": "Unclear which products to prioritize on BigBasket. Needed insights into category trends, competitor performance, and seasonal demand patterns.",
            "solution": "Comprehensive BigBasket analysis tracking 30,000+ products across 25 categories. Analyzed sales velocity, reviews, pricing, and seasonal trends.",
            "results": [
                "Optimized portfolio to 200 high-performing SKUs",
                "50% increase in sales velocity",
                "Analyzed 30,000+ competitive products",
                "Identified 10 high-growth categories",
                "Reduced portfolio complexity by 40%"
            ],
            "metrics": {
                "sku_optimization": "200 SKUs",
                "sales_increase": "50%",
                "products_analyzed": "30,000+",
                "complexity_reduction": "40%"
            }
        }
    ],
    "food-delivery": [
        {
            "slug": "swiggy-restaurant-optimization-80-percent-orders",
            "title": "Nextract | 80% Order Increase | Swiggy Case Study",
            "description": "Restaurant chain increased orders by 80% using Swiggy competitive intelligence. Menu optimization based on 50,000+ restaurant analysis.",
            "keywords": "Swiggy restaurant optimization, food delivery intelligence, menu optimization, order growth, competitive analysis",
            "client": "Multi-Location Restaurant Chain",
            "industry": "Food & Beverage",
            "challenge": "Stagnant order volumes despite presence on Swiggy. Needed insights into successful menu strategies, pricing, and promotional tactics.",
            "solution": "Analyzed 50,000+ restaurants on Swiggy tracking menus, pricing, ratings, reviews, delivery times, and promotional strategies across competitive set.",
            "results": [
                "80% increase in order volumes",
                "Menu optimized based on 50,000+ restaurants",
                "35% improvement in average rating",
                "25% increase in average order value",
                "Achieved top 10 ranking in 3 categories"
            ],
            "metrics": {
                "order_increase": "80%",
                "restaurants_analyzed": "50,000+",
                "rating_improvement": "35%",
                "aov_increase": "25%"
            }
        },
        {
            "slug": "zomato-cloud-kitchen-success-5-location",
            "title": "Nextract | 5 Locations Launched | Zomato Case Study",
            "description": "Cloud kitchen brand launched 5 profitable locations using Zomato delivery intelligence. Analyzed delivery zones across 10 cities for optimal placement.",
            "keywords": "Zomato cloud kitchen, delivery zone analysis, location strategy, food delivery optimization, market intelligence",
            "client": "Cloud Kitchen Brand",
            "industry": "Cloud Kitchen",
            "challenge": "Identifying optimal locations for new cloud kitchens without wasting investment on poor-performing areas. Needed delivery zone and demand analysis.",
            "solution": "Comprehensive Zomato intelligence mapping delivery zones, restaurant density, cuisine gaps, and demand patterns across 10 cities with 100,000+ restaurants.",
            "results": [
                "5 profitable cloud kitchen locations launched",
                "All locations achieved profitability in 4 months",
                "Analyzed 100,000+ restaurants across 10 cities",
                "Identified 8 high-demand cuisine gaps",
                "$2M in first-year revenue"
            ],
            "metrics": {
                "locations_launched": "5",
                "profitability_timeline": "4 months",
                "restaurants_analyzed": "100,000+",
                "first_year_revenue": "$2M"
            }
        },
        {
            "slug": "doordash-menu-engineering-45-percent-profit",
            "title": "Nextract | 45% Profit Boost | DoorDash Case Study",
            "description": "Restaurant group increased profit by 45% using DoorDash menu intelligence. Analyzed 20,000+ restaurants for pricing and item optimization.",
            "keywords": "DoorDash menu engineering, restaurant profitability, pricing optimization, menu intelligence, competitive analysis",
            "client": "Restaurant Group (12 Locations)",
            "industry": "Restaurant Operations",
            "challenge": "Low profit margins on delivery orders due to suboptimal menu pricing and item selection. Needed data-driven menu engineering approach.",
            "solution": "Analyzed 20,000+ restaurants on DoorDash tracking menu items, pricing strategies, portion sizes, combos, and profitability indicators across cuisines.",
            "results": [
                "45% increase in delivery profit margins",
                "Optimized menu across 12 locations",
                "Analyzed 20,000+ competitive menus",
                "Increased average order value by 30%",
                "$500K additional annual profit"
            ],
            "metrics": {
                "profit_increase": "45%",
                "locations": "12",
                "menus_analyzed": "20,000+",
                "additional_profit": "$500K"
            }
        },
        {
            "slug": "uber-eats-market-expansion-8-city-success",
            "title": "Nextract | 8 Cities Expanded | Uber Eats Case Study",
            "description": "Restaurant brand expanded to 8 new cities using Uber Eats intelligence. Analyzed 150,000+ restaurants across 45 markets for expansion strategy.",
            "keywords": "Uber Eats expansion, multi-city strategy, restaurant growth, market intelligence, competitive analysis",
            "client": "Fast-Casual Restaurant Brand",
            "industry": "Restaurant Chain",
            "challenge": "Planning expansion into 8 new cities without local market knowledge. Needed to understand competition, pricing, and consumer preferences.",
            "solution": "Comprehensive Uber Eats analysis across 45 potential markets, analyzing 150,000+ restaurants, delivery zones, popular cuisines, and pricing strategies.",
            "results": [
                "Successfully expanded to 8 new cities",
                "All locations profitable within 6 months",
                "Analyzed 150,000+ restaurants across 45 markets",
                "Identified optimal price points for each market",
                "$8M in new market revenue"
            ],
            "metrics": {
                "cities_expanded": "8",
                "profitability": "6 months",
                "restaurants_analyzed": "150,000+",
                "new_revenue": "$8M"
            }
        },
        {
            "slug": "deliveroo-ghost-kitchen-optimization",
            "title": "Nextract | Ghost Kitchen Success | Deliveroo Case Study",
            "description": "Ghost kitchen operator optimized 15 brands using Deliveroo intelligence. Multi-brand strategy across 30 locations in UK market.",
            "keywords": "Deliveroo ghost kitchen, multi-brand strategy, virtual restaurant, UK food delivery, brand optimization",
            "client": "Ghost Kitchen Operator",
            "industry": "Virtual Restaurant",
            "challenge": "Managing 15 virtual brands from 30 locations without insights into optimal brand positioning, pricing, and menu strategies per location.",
            "solution": "Deployed Deliveroo tracking across all 30 locations monitoring 15 virtual brands against 5,000+ competitors. Real-time performance and competitive insights.",
            "results": [
                "Optimized 15 virtual brands across 30 locations",
                "60% increase in average location revenue",
                "Monitored 5,000+ competitive restaurants",
                "3 brands achieved top 50 ranking in their category",
                "£5M annual revenue from optimized operations"
            ],
            "metrics": {
                "brands_optimized": "15",
                "revenue_increase": "60%",
                "locations": "30",
                "annual_revenue": "£5M"
            }
        }
    ]
}

TEMPLATE = """---
layout: default
title: "{title}"
description: "{description}"
keywords: "{keywords}"
category: "case-study"
industry: "{industry}"
client: "{client}"
---

<main>
<div class="container mx-auto px-4 py-16">

# {heading}

<div class="bg-blue-50 border-l-4 border-blue-600 p-6 mb-8">
  <p class="text-lg"><strong>Client:</strong> {client}</p>
  <p class="text-lg"><strong>Industry:</strong> {industry}</p>
</div>

## The Challenge

{challenge}

## Our Solution

{solution}

## Key Results

{results_list}

## Metrics at a Glance

<div class="grid grid-cols-2 md:grid-cols-4 gap-6 my-12">
{metrics_cards}
</div>

## Why This Worked

### Data-Driven Decision Making
Instead of relying on intuition, our client leveraged real-time competitive intelligence from Nextract to make informed decisions backed by comprehensive market data.

### Automated Intelligence
Manual competitor monitoring was replaced with automated data extraction, providing real-time insights and alerts that enabled rapid response to market changes.

### Scalable Infrastructure
Nextract's robust API infrastructure handled large-scale data extraction reliably, processing millions of data points to deliver actionable intelligence.

### Expert Support
Our team provided strategic guidance on interpreting the data and implementing changes, ensuring maximum ROI from the intelligence gathered.

## Technology Stack

- **Nextract API** - Real-time data extraction
- **Custom Dashboards** - Visualize competitive intelligence
- **Automated Alerts** - Instant notifications for key changes
- **Data Integration** - Seamless connection with existing systems

## Client Testimonial

> "Nextract transformed our approach to competitive intelligence. The real-time data and insights have been game-changing for our business. The ROI was evident within weeks, and the platform continues to deliver value daily."

## Ready to Transform Your Business?

See how Nextract can help you gain competitive advantage with real-time market intelligence. Our data extraction solutions are trusted by leading brands worldwide.

[Start Free Trial](#) | [Schedule Demo](#) | [View All Case Studies](/case-studies.html)

## Related Resources

{related_resources}

</div>
</main>
"""

def generate_case_study(data, category):
    """Generate a case study page"""
    
    # Generate results list
    results_list = "\n".join([f"- **{result}**" for result in data['results']])
    
    # Generate metrics cards
    metrics_cards = []
    for key, value in data['metrics'].items():
        label = key.replace('_', ' ').title()
        metrics_cards.append(f"""  <div class="text-center p-6 bg-white border border-gray-200">
    <div class="text-4xl font-black text-blue-600 mb-2">{value}</div>
    <div class="text-sm font-bold text-gray-600 uppercase">{label}</div>
  </div>""")
    metrics_html = "\n".join(metrics_cards)
    
    # Generate heading
    parts = data['title'].split('|')
    if len(parts) >= 3:
        heading = f"{parts[1].strip()} - {parts[2].strip()}"
    else:
        heading = data['title']
    
    # Related resources based on category
    if category == "e-commerce":
        related_resources = """- [E-commerce Data Solutions](/e-commerce.html) - Multi-platform e-commerce intelligence
- [Price Intelligence](/intelligence/price-intelligence) - Competitive pricing analytics
- [E-commerce Intelligence](/intelligence/e-commerce-intelligence) - Market insights and trends"""
    elif category == "quick-commerce":
        related_resources = """- [Quick Commerce Solutions](/quick-commerce.html) - Ultra-fast delivery intelligence
- [Market Intelligence](/intelligence/market-intelligence) - Quick commerce market insights
- [Price Intelligence](/intelligence/price-intelligence) - Real-time pricing data"""
    else:  # food-delivery
        related_resources = """- [Food Delivery Solutions](/food-delivery.html) - Restaurant and delivery intelligence
- [Restaurant Intelligence](/intelligence/restaurant-intelligence) - Menu and pricing analytics
- [Market Intelligence](/intelligence/market-intelligence) - Food delivery market trends"""
    
    # Generate content
    content = TEMPLATE.format(
        title=data['title'],
        description=data['description'],
        keywords=data['keywords'],
        industry=data['industry'],
        client=data['client'],
        heading=heading,
        challenge=data['challenge'],
        solution=data['solution'],
        results_list=results_list,
        metrics_cards=metrics_html,
        related_resources=related_resources
    )
    
    return content

def main():
    """Generate all case study pages"""
    script_dir = Path(__file__).parent
    case_studies_dir = script_dir / "_case-studies"
    case_studies_dir.mkdir(exist_ok=True)
    
    print("\n" + "="*60)
    print("Generating Case Study Pages...")
    print("="*60 + "\n")
    
    total_created = 0
    
    for category, studies in CASE_STUDIES.items():
        print(f"{category.upper().replace('-', ' ')} Case Studies:")
        for study in studies:
            filename = case_studies_dir / f"{study['slug']}.md"
            
            content = generate_case_study(study, category)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"  ✓ {study['client']}")
            total_created += 1
        print()
    
    print("="*60)
    print(f"✅ Created {total_created} case study pages!")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
