# Application Architecture & Standards

## Directory Structure Strategy
All application source code lives strictly inside `/src`. 

* `/src/app/`: Next.js routing (pages, layouts, loading, error boundaries). 
  * Keep `page.tsx` files as thin as possible. Fetch data here, then pass it down to components.
* `/src/components/`: Reusable React components.
  * `/src/components/ui/`: Dumb/Presentational components (buttons, inputs, cards).
  * `/src/components/features/`: Smart components bound to specific business logic.
* `/src/lib/`: Utility functions, Prisma client initialization (`prisma.ts`), and constants.
* `/src/actions/`: Next.js Server Actions. All database mutations (POST/PUT/DELETE) go here.

## Next.js Best Practices
1. **Server vs. Client:** Use React Server Components (RSC) by default to keep bundle sizes zero. Add `"use client"` ONLY when you need interactivity, hooks, or browser APIs.
2. **Data Mutations:** Do not use generic `/app/api/` route handlers for internal data mutations. Use Next.js **Server Actions** placed in the `/src/actions/` directory, and call them from your client components.
3. **Data Fetching:** Fetch data directly in Server Components using Prisma. You do not need an API route to fetch data for a page.
4. **Tailwind CSS:** Use utility classes directly in the `className` attribute. Use tools like `clsx` and `tailwind-merge` (typically wrapped in a `cn()` utility) for conditional class joining. Do not use `@apply` in global CSS unless it is for base layer resets.
5. **Error Handling:** Use `error.tsx` boundaries for UI fallbacks. Server Actions should return standardized objects, e.g., `{ success: true, data: ... }` or `{ success: false, error: "message" }`.