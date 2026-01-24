---
title:  "System Design Interview Questions"
date:   2024-11-28 10:00:00 +0800
tags: [Theory]
---


1. **Design a URL Shortening Service**  
   - **Question**: Design a service like Bitly, where users can input long URLs and receive a shortened version. Consider scalability, database design, and features like custom alias, redirection, analytics, and expiration of links.

2. **Design a Rate Limiter**  
   - **Question**: Design a system that limits how many requests a user can make to a service within a given time window (e.g., 100 requests per minute). Consider different approaches like token bucket, leaky bucket, or fixed window counters.

3. **Design a Notification System**  
   - **Question**: Design a system that can send real-time notifications to users across different platforms (e.g., mobile, email, SMS). Think about scalability, handling user preferences, message queues, and different types of notifications (push, in-app, etc.).

4. **Design a Web Crawler**  
   - **Question**: Design a system to crawl and index the web (like Googlebot). Discuss how you would handle scalability, data storage, URL filtering, crawl frequency, and obeying robots.txt rules.

5. **Design a Distributed Key-Value Store**  
   - **Question**: Design a scalable, highly available key-value store like Redis or Amazon DynamoDB. Focus on consistency, availability, partition tolerance (CAP theorem), and how data is stored and retrieved efficiently.

6. **Design a Unique Identifier Generator**  
   - **Question**: Design a system that generates unique identifiers for objects (e.g., UUIDs). Consider performance, uniqueness across distributed systems, and collision prevention. Explore algorithms like Snowflake ID generation.

7. **Design a Payment System**  
   - **Question**: Design an online payment system like PayPal or Stripe. Discuss user authentication, security (encryption, PCI compliance), payment gateways, transaction processing, and handling failure cases.

8. **Design a Dating App like Tinder**  
   - **Question**: Design a dating application where users can swipe on profiles to like or pass. Consider the real-time interactions, recommendation algorithms, user profile management, matching logic, scalability, and safety features.

9. **Design a Hotel Booking System like Booking.com**  
   - **Question**: Design a platform for users to search and book hotels. Think about search efficiency, availability management, pricing algorithms, hotel reviews, user account management, and integration with hotel partners.

10. **Design a Streaming Service like Netflix**  
    - **Question**: Design a video streaming platform that can scale to handle millions of users watching high-definition videos. Consider content delivery networks (CDNs), video encoding, adaptive streaming, user recommendations, and subscription management.

11. **Design a Ride-sharing System like Uber**  
    - **Question**: Design a system where users can book rides from drivers in real-time. Discuss trip matching algorithms, geolocation, ride tracking, pricing models, surge pricing, and real-time communication.

12. **Design a News Feed System like Facebook**  
    - **Question**: Design a news feed where users can see posts from their friends or followed accounts. Think about how posts are ranked, handling large numbers of posts, privacy controls, and dealing with real-time updates.

13. **Design a Social Media Network like Twitter**  
    - **Question**: Design a social media platform with short text posts, likes, and retweets. Discuss scaling for high throughput, follower-based relationships, data consistency, and real-time feeds.

14. **Design a Photo Sharing Service like Instagram**  
    - **Question**: Design a photo-sharing application where users can upload, share, and view photos. Consider image storage, feed algorithms, user engagement, privacy controls, and how you would handle scaling for millions of photos.

15. **Design an Instant Messaging Service like WhatsApp**  
    - **Question**: Design a real-time chat application. Focus on message delivery, read receipts, presence status, group chats, media sharing, and security (end-to-end encryption).

16. **Design an E-commerce Platform like Amazon**  
    - **Question**: Design an online store where users can browse products, add to cart, and checkout. Discuss product search, inventory management, payment processing, order fulfillment, and user reviews.

17. **Design a Collaborative Editing Service like Notion**  
    - **Question**: Design a platform where multiple users can collaboratively edit documents in real-time. Think about version control, concurrency, conflict resolution, and data synchronization across users.

18. **Design a File Storage Service like Dropbox**  
    - **Question**: Design a cloud-based file storage system. Consider file uploading, version control, sharing permissions, real-time synchronization, backup, and security of user data.

19. **Design an Autocomplete System like Google Search**  
    - **Question**: Design a search engine autocomplete feature that provides suggestions as users type. Discuss how to handle large datasets, ranking suggestions, and ensuring low-latency responses.

20. **Design a Search Engine like Google**  
    - **Question**: Design a search engine capable of indexing and retrieving web pages based on user queries. Think about crawling, indexing, ranking algorithms (e.g., PageRank), query processing, and scalability for billions of pages.
