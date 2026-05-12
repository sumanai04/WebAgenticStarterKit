# Database Schema & State

**AGENT DIRECTIVE:** Every time you modify `prisma/schema.prisma`, you MUST update this file to accurately reflect the current state of the database. This prevents you from hallucinating incorrect table relations.

## Current Database Engine: PostgreSQL

## Prisma Guidelines
* Always use `cuid()` or `uuid()` for primary keys. Do not use auto-incrementing integers (`autoincrement()`).
* Use `@map()` to map camelCase Prisma fields to snake_case database columns if required by external DB conventions, though camelCase is generally preferred for Next.js consistency.
* **Relations:** Always explicitly define relation names if there are multiple relations between the same two models to avoid ambiguity.
* **Timestamps:** Every model should include `createdAt DateTime @default(now())` and `updatedAt DateTime @updatedAt`.

## Models Overview

*(Keep this section updated as the project grows)*

### `User`
Handles system authentication and user profiles.
* `id` (String, CUID, Primary Key)
* `email` (String, Unique)
* `passwordHash` (String, Optional if using OAuth)
* `name` (String, Optional)
* `createdAt` (DateTime)
* `updatedAt` (DateTime)

### `ExampleItem`
*(Placeholder for the first feature model)*
* `id` (String, CUID, Primary Key)
* `title` (String)
* `userId` (String, Foreign Key to User)
* `createdAt` (DateTime)
* `updatedAt` (DateTime)