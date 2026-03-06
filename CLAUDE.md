# CLAUDE.md

## Project Overview

Language Training Revenue & Capacity Planning Calculator — an interactive web app for financial planning and scheduling of language training programs. Models corporate, institutional, private, and open enrollment programs with visual scheduling, revenue projections, and cost breakdowns.

## Tech Stack

- **Framework:** React 19 + TypeScript
- **Build Tool:** Vite 7
- **Styling:** Tailwind CSS 4 (via `@tailwindcss/vite` plugin)
- **Icons:** Lucide React
- **Charts:** Recharts
- **Deployment:** GitHub Pages (base path: `/AyElSeeMoldo/`)

## Project Structure

```
calculator/                    # Main application directory
├── src/
│   ├── main.tsx              # React entry point
│   ├── App.tsx               # Root layout component
│   ├── types.ts              # Type definitions, constants, and rate tables
│   ├── calculations.ts       # Pure financial calculation functions
│   ├── index.css             # Tailwind CSS imports
│   ├── components/
│   │   ├── RevenueCalculator.tsx  # Form inputs and financial summary
│   │   ├── VisualScheduler.tsx    # Drag-and-drop scheduling grid
│   │   └── CalcBreakdown.tsx      # Cost structure reference display
│   └── assets/
├── public/
├── package.json
├── vite.config.ts
├── eslint.config.js          # ESLint flat config
├── tsconfig.json             # References tsconfig.app.json and tsconfig.node.json
├── tsconfig.app.json         # App: ES2022, strict, react-jsx
└── tsconfig.node.json        # Build tooling: ES2023
```

## Common Commands

All commands run from the `calculator/` directory:

```bash
npm install          # Install dependencies
npm run dev          # Start Vite dev server with HMR
npm run build        # Type-check (tsc -b) then bundle with Vite
npm run lint         # Run ESLint across the project
npm run preview      # Preview production build locally
```

## Architecture & Key Conventions

- **State management:** React `useState` for local state, `useMemo` for derived calculations. No external state library.
- **Business logic separation:** All financial calculations live in `calculations.ts` as pure functions. All constants and types live in `types.ts`. Components handle only presentation and user interaction.
- **Styling:** Tailwind utility classes applied directly in JSX. No custom CSS component classes.
- **TypeScript:** Strict mode enabled. `noUnusedLocals`, `noUnusedParameters`, and `noFallthroughCasesInSwitch` are all enforced.
- **Naming:** `camelCase` for functions and variables, `PascalCase` for components and types.
- **Components:** Functional components with hooks only — no class components.

## Linting & Type Checking

ESLint uses flat config format with:
- `@eslint/js` recommended rules
- TypeScript ESLint recommended rules
- React Hooks plugin (enforces rules-of-hooks)
- React Refresh plugin

Run `npm run lint` before committing. The build script (`npm run build`) runs `tsc -b` first, so type errors will fail the build.

## Business Domain Context

The calculator models a language school with:
- **5 rooms:** Small 1, Small 2, Large 1, Large 2, Conference
- **4 daily time slots:** ~2–2.25 hour classes
- **Day patterns:** Mon/Wed and Tue/Thu rotations
- **4 program types** with different rate structures:
  - Corporate, Institutional, Private (fixed per-student rates)
  - Open Enrollment (dynamic rates based on student count)
- **Cost model:** Teacher costs (with 40% salaried surcharge for benefits), rent allocation to facility-using programs, 12% IDC rate on direct costs, and fixed monthly costs (rent $3,400, admin $5,740, other $1,550)

When modifying calculation logic, update `types.ts` for rate/constant changes and `calculations.ts` for formula changes. These are the source of truth for all financial numbers.
