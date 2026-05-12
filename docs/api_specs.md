# API Specifications

**AGENT DIRECTIVE:** This file acts as the contract between the Next.js frontend and the FastAPI backend. 
* If you write a new Python endpoint in `/src/backend`, you MUST document it here.
* If you are writing Next.js frontend code in `/src/frontend`, rely on this document for your fetch calls.

## Base URL
* **Local Development:** `http://localhost:8000`
* All frontend fetch requests should target this base URL.

## Endpoints Overview

### Health & Status
* **`GET /`**
  * Returns basic health check.
  * Response: `{ "status": "healthy", "message": string }`

* **`GET /api/v1/status`**
  * Returns detailed system status.
  * Response: `{ "database": string, "ai_agent": string, "version": string }`

## Frontend Fetching Rules
When fetching from Next.js Server Components, use native `fetch` with appropriate caching strategies:
```typescript
// Example frontend fetch
async function getStatus() {
  const res = await fetch('http://localhost:8000/api/v1/status', {
    cache: 'no-store' // or next: { revalidate: 3600 }
  });
  if (!res.ok) throw new Error('Failed to fetch data');
  return res.json();
}