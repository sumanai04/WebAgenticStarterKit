# Agentic Web Starter Kit - Global Directives

You are an expert full-stack developer operating in an autonomous loop. Your primary stack is Next.js (App Router), TypeScript, Tailwind CSS, and Prisma ORM (PostgreSQL).

## 1. Directory Routing (Read First)
Never guess the project structure. If you are unsure where a file belongs or what the architectural rules are, read the documentation first using your subagent (`claude-haiku`).
* **System Architecture & Next.js Rules:** Read `/docs/architecture.md`
* **Database Schema & Prisma Rules:** Read `/docs/db_schema.md`

## 2. Strict Next.js & React Rules
* **App Router Only:** We strictly use the Next.js `app/` directory. Do not create or reference a `pages/` directory.
* **Server Components Default:** Default to React Server Components (RSC). Only use the `"use client"` directive when hooks (`useState`, `useEffect`) or browser APIs are strictly required.
* **Styling:** Use Tailwind CSS exclusively. 

## 3. Strict Database & Prisma Rules
* **Prisma as Truth:** The `prisma/schema.prisma` file is the absolute source of truth.
* **Documentation Sync:** If you modify `schema.prisma`, you MUST simultaneously update `/docs/db_schema.md` to reflect the changes.
* **Migration Protocol:** If you change the schema locally, always run `npx prisma generate` before attempting to use the Prisma Client in the code.

## 4. Execution Protocol
* **Investigation:** Use your subagent for broad directory searches. DO NOT output massive file contents into the main chat.
* **Verification:** Always run `npm run lint` and verify it passes before confirming a task is complete.