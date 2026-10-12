---
name: design-engineer-craft
description: >-
  Master guide for bridging Figma design, Ceramic luxury aesthetic, modern Tailwind CSS v4,
  Framer Motion micro-interactions, and 3D spatial staging in React/Next.js. Use when building
  visually breathtaking real estate, agency, and client UI components.
---

# Design Engineer Craft: Figma to Production Interface Systems

This skill guides the translation of high-end visual concepts into crisp, performant production code.

## 1. Ceramic Luxury Aesthetic Tokens
* **Obsidian Canvas:** `#04060A` / `#090C15`
* **Surface Elevation:** `#111420` (Card backings)
* **Hairline Borders:** `border-white/10` or `border-white/5` (1px precision)
* **Luxury Accents:**
  * Royal Amber / Gold: `#F59E0B`
  * Electric Violet: `#A855F7`
  * Cyber Cyan: `#00F5D4`
  * Verification Emerald: `#10B981`

## 2. Typographic Pairings
* **Headlines / Display:** Clash Display / Space Grotesk (`font-bold`, tracking `-0.03em`)
* **Body / Narration:** Satoshi / Plus Jakarta Sans (`font-normal`, clean leading)
* **Data / Badges / Code:** JetBrains Mono (`text-xs uppercase tracking-wider`)

## 3. Micro-Interactions with Framer Motion
```tsx
import { motion } from 'framer-motion';

export const LuxuryButton = ({ label }: { label: string }) => (
  <motion.button
    whileHover={{ scale: 1.02 }}
    whileTap={{ scale: 0.98 }}
    className="px-6 py-3 rounded-xl bg-gradient-to-r from-purple-600 to-indigo-600 text-white font-mono text-xs uppercase tracking-wider shadow-[0_0_20px_rgba(168,85,247,0.25)]"
  >
    {label}
  </motion.button>
);
```

## 4. Mobile Responsiveness First
* Always verify touch targets (minimum 44x44px for buttons).
* Test in mobile viewport (`390px` width) for zero horizontal overflow.
