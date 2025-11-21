---
layout: default
title: "Grab Taxi Fleet Intelligence"
description: "Real-time pricing and availability data delivered every 15 minutes across 3 major cities for strategic fleet management."
category: "Transportation"
client: "Transportation analytics firm"
---

<main>
    <!-- Hero Section -->
    <section class="min-h-[70vh] flex items-center justify-center relative overflow-hidden bg-white">
        <div class="absolute inset-0 overflow-hidden">
            <div class="absolute top-1/4 left-1/4 w-96 h-96 bg-blue-600/10 blur-[100px] animate-pulse"></div>
            <div class="absolute bottom-1/4 right-1/4 w-96 h-96 bg-orange-600/10 blur-[100px] animate-pulse" style="animation-delay: 1s;"></div>
        </div>
        
        <div class="container mx-auto px-6 max-w-7xl relative z-10">
            <div class="max-w-5xl mx-auto">
                <a href="/case-studies/" class="inline-flex items-center gap-2 text-sm font-semibold text-gray-600 hover:text-blue-600 transition-colors mb-8 group">
                    <span>←</span>
                    <span>Back to Case Studies</span>
                </a>
                
                <div class="text-sm font-bold text-blue-600 uppercase tracking-widest mb-6">{{ page.category }}</div>
                <h1 class="text-5xl md:text-7xl font-black text-gray-900 mb-6 leading-[0.9] tracking-tight">
                    {{ page.title }}
                </h1>
                <p class="text-xl md:text-2xl text-gray-600 mb-8 max-w-3xl font-light leading-relaxed">
                    Real-Time Pricing & Availability Delivered Every 15 Minutes
                </p>
                
                <div class="flex flex-wrap gap-4 items-center">
                    <div class="px-6 py-3 bg-gray-900 text-white font-semibold text-sm">
                        Client: {{ page.client }}
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Content Section -->
    <section class="py-32 bg-white">
        <div class="container mx-auto px-6 max-w-4xl">
            
            <!-- Challenge -->
            <div class="mb-20">
                <div class="text-sm font-bold text-blue-600 uppercase tracking-widest mb-4">The Challenge</div>
                <h2 class="text-4xl font-black text-gray-900 mb-6">Need for Real-Time Fleet Intelligence</h2>
                <p class="text-lg text-gray-600 leading-relaxed mb-6">
                    A transportation analytics firm needed comprehensive, real-time data on Grab Taxi's fleet operations across multiple cities. They required street-level precision data including driver positions, pricing tiers, surge behavior, and availability patterns to help their clients make informed decisions about fleet rebalancing, pricing strategies, and service gap identification.
                </p>
                <p class="text-lg text-gray-600 leading-relaxed">
                    The challenge was capturing this data consistently and reliably at scale, ensuring accuracy and timeliness for strategic decision-making.
                </p>
            </div>

            <!-- Solution -->
            <div class="mb-20">
                <div class="text-sm font-bold text-blue-600 uppercase tracking-widest mb-4">The Solution</div>
                <h2 class="text-4xl font-black text-gray-900 mb-6">Quarterly Updates Every 15 Minutes</h2>
                <p class="text-lg text-gray-600 leading-relaxed mb-8">
                    We built a robust data extraction pipeline that captures <strong class="text-gray-900">96 snapshots per day</strong> (every 15 minutes) across 3 major cities, providing real-time visibility into Grab Taxi's operations with street-level precision.
                </p>
                
                <div class="grid md:grid-cols-2 gap-6 mb-8">
                    <div class="p-8 border border-gray-200 bg-white">
                        <div class="text-3xl font-black text-blue-600 mb-3">96</div>
                        <div class="text-lg font-bold text-gray-900 mb-2">Snapshots Per Day</div>
                        <div class="text-gray-600">Quarterly updates every 15 minutes across 3 major cities</div>
                    </div>
                    <div class="p-8 border border-gray-200 bg-white">
                        <div class="text-3xl font-black text-orange-600 mb-3">Street-Level</div>
                        <div class="text-lg font-bold text-gray-900 mb-2">Precision</div>
                        <div class="text-gray-600">Real driver positions, pricing tiers, and surge behavior</div>
                    </div>
                </div>

                <div class="p-10 border-l-4 border-blue-600 bg-gray-50">
                    <p class="text-lg text-gray-900 font-semibold mb-4">Data Captured:</p>
                    <ul class="space-y-3 text-gray-600">
                        <li class="flex items-start gap-3">
                            <span class="text-blue-600 font-black mt-1">→</span>
                            <span>Real-time driver positions and availability</span>
                        </li>
                        <li class="flex items-start gap-3">
                            <span class="text-blue-600 font-black mt-1">→</span>
                            <span>Dynamic pricing tiers and surge multipliers</span>
                        </li>
                        <li class="flex items-start gap-3">
                            <span class="text-blue-600 font-black mt-1">→</span>
                            <span>Service area coverage and gaps</span>
                        </li>
                        <li class="flex items-start gap-3">
                            <span class="text-blue-600 font-black mt-1">→</span>
                            <span>Wait times and demand patterns</span>
                        </li>
                    </ul>
                </div>
            </div>

            <!-- Results -->
            <div class="mb-20">
                <div class="text-sm font-bold text-orange-600 uppercase tracking-widest mb-4">The Results</div>
                <h2 class="text-4xl font-black text-gray-900 mb-6">Actionable Intelligence Delivered</h2>
                
                <div class="grid md:grid-cols-3 gap-6 mb-8">
                    <div class="p-8 border border-gray-200 bg-white text-center">
                        <div class="text-4xl font-black text-blue-600 mb-3">Fleet</div>
                        <div class="text-lg font-bold text-gray-900 mb-2">Rebalancing</div>
                        <div class="text-gray-600">Optimized driver distribution based on real-time demand</div>
                    </div>
                    <div class="p-8 border border-gray-200 bg-white text-center">
                        <div class="text-4xl font-black text-orange-600 mb-3">Pricing</div>
                        <div class="text-lg font-bold text-gray-900 mb-2">Forecasts</div>
                        <div class="text-gray-600">Accurate surge prediction for strategic planning</div>
                    </div>
                    <div class="p-8 border border-gray-200 bg-white text-center">
                        <div class="text-4xl font-black text-blue-600 mb-3">Service</div>
                        <div class="text-lg font-bold text-gray-900 mb-2">Gap Analysis</div>
                        <div class="text-gray-600">Identified underserved areas for expansion opportunities</div>
                    </div>
                </div>

                <p class="text-lg text-gray-600 leading-relaxed">
                    Our client was able to provide their customers with actionable intelligence that transformed how they approached fleet management and strategic planning. The real-time data pipeline enabled data-driven decisions that improved operational efficiency and competitive positioning.
                </p>
            </div>

            <!-- Key Takeaways -->
            <div class="p-10 border border-gray-200 bg-gray-50">
                <h3 class="text-2xl font-black text-gray-900 mb-6">Key Takeaways</h3>
                <div class="space-y-4">
                    <div class="flex items-start gap-4">
                        <div class="w-12 h-12 bg-blue-600 text-white font-black flex items-center justify-center flex-shrink-0">1</div>
                        <div>
                            <div class="font-bold text-gray-900 mb-1">Real-time data enables strategic decisions</div>
                            <div class="text-gray-600">15-minute update intervals provide actionable intelligence for dynamic markets</div>
                        </div>
                    </div>
                    <div class="flex items-start gap-4">
                        <div class="w-12 h-12 bg-blue-600 text-white font-black flex items-center justify-center flex-shrink-0">2</div>
                        <div>
                            <div class="font-bold text-gray-900 mb-1">Street-level precision matters</div>
                            <div class="text-gray-600">Granular data capture enables micro-level strategic insights</div>
                        </div>
                    </div>
                    <div class="flex items-start gap-4">
                        <div class="w-12 h-12 bg-orange-600 text-white font-black flex items-center justify-center flex-shrink-0">3</div>
                        <div>
                            <div class="font-bold text-gray-900 mb-1">Scalable data pipelines drive value</div>
                            <div class="text-gray-600">Reliable, consistent data extraction at scale enables competitive advantages</div>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </section>

    {% include contact-section.html %}
</main>

