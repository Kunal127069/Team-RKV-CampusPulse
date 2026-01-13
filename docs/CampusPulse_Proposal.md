Project Proposal: CampusPulse

Tagline: The heartbeat of a smarter, faster, and more connected campus.

1. Executive Summary

CampusPulse is an integrated ecosystem designed to resolve the most common friction points in college life: dining congestion, information asymmetry, and peer-to-peer knowledge sharing. By combining a smart pre-ordering system with an offline-ready verification protocol and a community skill marketplace, we aim to save students an average of 45 minutes daily.

2. The Problem Statement

Despite being in a tech-forward environment, our campus dining faces:

The "Line Lag": Peak-hour (12:00 PM) congestion leads to 20+ minute waits, causing students to skip lunch.

Inventory Blindness: No real-time way to know if items are "Sold Out," leading to disappointment after long waits.

The "Network Dead-Zone": Poor signal in mess/canteen areas causes UPI payment timeouts, freezing the entire queue.

System Vulnerability: Digital pre-ordering risks "Ghost Orders" (orders placed but never collected).

Staff Inertia: Traditional workers often find complex digital systems disruptive to their established physical slip workflow.

3. The CampusPulse Solution

A. The Smart Canteen Module

Remote Ordering: Order and pay via the app from classrooms/hostels.

Live Stock Sync: Items are greyed out in real-time as they run out.

Hybrid Slip System: Students scan a Time-Based QR Code at the counter which triggers a physical slip for the staff. This maintains the staff's traditional "Prepare & Tear" workflow, ensuring job security and ease of adoption.

B. The "Anti-Troll" Integrity Protocol (USP)

To prevent the misuse of pre-ordering, we've implemented:

The ₹5 Penalty: Automatically applied to the next order if a student "ghosts" a pickup.

Smart Reset: A 4-day cooldown period that clears penalties for accidental misses, ensuring the system remains student-friendly.

C. The Offline Mess Module

Local Token Caching: Secure tokens are generated while the student has internet and can be verified by guards even in zero-signal zones using localized decryption logic.

D. The Skill Swap Module

Knowledge Barter: A dedicated tab for students to trade skills (e.g., "I'll teach you Photoshop if you help me with Engineering Drawing").

4. Technical Implementation

Frontend: TypeScript with React (for type-safe, high-fidelity UI).

Backend: Python (Django) with PostgreSQL for high-integrity transaction handling.

Core Engine: C++ for low-latency, offline cryptographic QR decryption.

Intelligence: Gemini AI API for predictive stock analytics.

Security: TTL (Time-To-Live) QR Codes and JWT for secure authentication.

5. User Roles

Student: Browses menus, places orders, manages skill profile, tracks penalty status.

Canteen/Counter Staff: Scans QR codes, prints physical slips, updates item availability.

Security/Mess Guard: Simplified "One-Tap" scanner for mess entry verification.

Administrators (RKV): Views peak-hour analytics, manages the "Skill Swap" moderation.

6. Impact & Scalability

Operational Efficiency: Estimated 50% reduction in physical queue density.

Student Wellness: Reliable access to nutrition without compromising class schedules.

Staff Empowerment: Digitization without the learning curve of complex new workflows.
