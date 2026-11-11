<p align="center">
  <img src="assets/header.svg" width="100%" alt="Noor Mohammad Sowan. Software engineer in Dhaka. I build AI automation and full-stack systems.">
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/noor-mohammad-sowan"><img src="https://img.shields.io/badge/LinkedIn-38e062?style=for-the-badge" alt="LinkedIn"></a>
  <a href="mailto:nurmohammadsowan119@gmail.com"><img src="https://img.shields.io/badge/Email-38e062?style=for-the-badge" alt="Email"></a>
  <a href="https://sowan-portfolio.vercel.app"><img src="https://img.shields.io/badge/Portfolio-38e062?style=for-the-badge" alt="Portfolio"></a>
  <a href="https://www.pexels.com/@noor-mohammad-sowan-944251072"><img src="https://img.shields.io/badge/Pexels-17171b?style=for-the-badge" alt="Pexels"></a>
</p>

## About

I am a software engineer in Dhaka, Bangladesh. I studied Software Engineering at Universiti Sains Malaysia in Penang and finished in August 2026.

Most of my work is AI automation and the full-stack systems around it. At ECTrons in 2025 I designed Virtual Zara, an n8n agent that connected GitLab, Google Workspace, Microsoft Graph, Telegram and OpenAI for the company's HR, finance and project teams. My final-year project, BahasaBot, won a Silver Award at the PIXEL 2026 showcase. In November 2026 I built DocIntel, an invoice-processing system, in five days from my phone.

I am looking for AI engineering and automation roles, and I am open to relocation and remote work. Outside of code I read on psychology, geopolitics and religion, and I publish photographs on Pexels.

## How I build

<p align="center">
  <img src="assets/method.svg" width="100%" alt="How I build: requirements, rules in CLAUDE.md, phases in PHASES.md, build with Claude Code, log in STATUS.md and DECISIONS.md, then test in CI and ship.">
</p>

I write the requirements, a short file of rules the build must never break, and a phased plan before any code. Then I build phase by phase with AI coding tools, mainly Claude Code, and log each decision. DocIntel has 89 recorded decisions. Vindeshi Express started from a baseline of 81 functional requirements, and its commits cite the requirement each one satisfies.

## Featured

<p align="center">
  <a href="https://github.com/Sowan3k/AI-Powered-Document-Intelligence-System">
    <img src="assets/docintel.svg" width="100%" alt="DocIntel. Pipeline: ingest, OCR, extract, validate, review and search. All fields correct on 91 of 91 synthetic invoices, 439 tests in CI, 12 of 12 planted errors caught.">
  </a>
</p>

**DocIntel** reads invoices from digital and scanned PDFs, phone photos, TIFF, Excel and CSV. Gemini extracts each field with a confidence score and the source text it came from. Eleven validation rules in exact decimal arithmetic check the numbers and send failures to a review queue. With real Gemini models on a labelled synthetic dataset, all eight fields were correct on 91 of 91 invoices. I built it in five days as a technical assessment, through Claude Code sessions driven by written specifications.

[Repository](https://github.com/Sowan3k/AI-Powered-Document-Intelligence-System) · [Walkthrough video](https://youtu.be/n9xKvACPR90) · [API docs](https://docintel-api-y25b.onrender.com/api/docs) · [Evaluation report](https://github.com/Sowan3k/AI-Powered-Document-Intelligence-System/blob/main/docs/EVALUATION.md) · [Web app](https://docintel-tan-two.vercel.app) (sign-in required)

<p align="center">
  <a href="https://bahasa-bot.vercel.app">
    <img src="assets/bahasabot.svg" width="100%" alt="BahasaBot. RAG chatbot, course generator and adaptive quiz. Repeat course generation from about 78 seconds to about 280 milliseconds. In-app rating 4.3 out of 5 from 30 users.">
  </a>
</p>

**BahasaBot** teaches Malay to international students at Malaysian public universities. A RAG chatbot streams replies over Server-Sent Events from a pgvector store. A course generator turns any topic into modules and quizzes, and a template-and-clone layer cut a repeat course from about 78 seconds and 21,300 tokens to about 280 ms and zero tokens. The adaptive quiz recalculates the learner's level on the BahasaBot Proficiency Scale (BPS-1 to BPS-4) from the last three attempts.

[Live demo](https://bahasa-bot.vercel.app) (the first load can take a minute) · [Repository](https://github.com/Sowan3k/BahasaBot)

## More builds

| Project | What it is | Stack |
| --- | --- | --- |
| **[Vindeshi&nbsp;Express](https://github.com/Sowan3k/Project-V)**<br>in&nbsp;testing | Community-maintained map of study-abroad routes for Bangladeshi students. Shared knowledge is append-only, enforced by PostgreSQL triggers, a Prisma client extension and an ESLint import boundary. Unit and Playwright suites run in CI. | Next.js 15, React 19, TypeScript, Prisma, Neon Postgres, Auth.js, Vitest, Playwright, GitHub Actions |
| **[ChargeWatch](https://github.com/Sowan3k/chargewatch)**<br>open&nbsp;source | Android app under 500 KB that tells a second phone when the first reaches 80% and when it is full. No account and no backend. Phones pair by QR code and talk through the ntfy push relay. Every release passes an end-to-end test on an Android 14 emulator. | Kotlin, Android, ntfy, GitHub Actions |
| **[USM&nbsp;Evently](https://usm-evently.vercel.app)**<br>live&nbsp;demo | Campus events platform for USM. Three roles, QR check-in, MyCSD co-curricular points, English and Bahasa Malaysia. Payments are simulated. [Repository](https://github.com/Sowan3k/usm_evently) | Next.js 15, TypeScript, Prisma, Neon Postgres, NextAuth, Zod, Tailwind, shadcn/ui |
| **[My&nbsp;Bibi](https://github.com/Sowan3k/My-Bibi-App)**<br>open&nbsp;source | Self-hosted private chat and journal app. Local Ollama models, PWA, journals encrypted at rest with a key derived from each user's password. | Next.js, FastAPI, SQLite FTS5, Ollama, Docker Compose |
| **[Grab&nbsp;Real&#8209;Time&nbsp;Demo](https://grab-realtime-demo.onrender.com)**<br>team&nbsp;coursework | Ride-hailing operations dashboard for CSE443, built by a team of four. Driver fatigue alerts within a 2 s deadline, surge pricing pushed over WebSocket within 500 ms. [Repository](https://github.com/Sowan3k/grab-realtime-demo) | Node.js, Express, WebSocket |
| **Virtual&nbsp;Zara**<br>internal,&nbsp;ECTrons | n8n automation agent across five systems and three business areas. Takes text, voice and documents, generates documents and PDFs, and turns GitLab activity into project reports. No public code. | n8n, JavaScript, OpenAI API, GitLab API, Google Workspace APIs, Microsoft Graph API, Telegram Bot API |

## Stack

**Languages**

![Python](https://img.shields.io/badge/Python-17171b?style=for-the-badge&logo=python&logoColor=38e062) ![TypeScript](https://img.shields.io/badge/TypeScript-17171b?style=for-the-badge&logo=typescript&logoColor=38e062) ![JavaScript](https://img.shields.io/badge/JavaScript-17171b?style=for-the-badge&logo=javascript&logoColor=38e062) ![Kotlin](https://img.shields.io/badge/Kotlin-17171b?style=for-the-badge&logo=kotlin&logoColor=38e062) ![SQL](https://img.shields.io/badge/SQL-17171b?style=for-the-badge)

**AI and automation**

![LangChain](https://img.shields.io/badge/LangChain-17171b?style=for-the-badge&logo=langchain&logoColor=38e062) ![Gemini API](https://img.shields.io/badge/Gemini_API-17171b?style=for-the-badge&logo=googlegemini&logoColor=38e062) ![Ollama](https://img.shields.io/badge/Ollama-17171b?style=for-the-badge&logo=ollama&logoColor=38e062) ![n8n](https://img.shields.io/badge/n8n-17171b?style=for-the-badge&logo=n8n&logoColor=38e062) ![OpenCV](https://img.shields.io/badge/OpenCV-17171b?style=for-the-badge&logo=opencv&logoColor=38e062) ![RAG with pgvector](https://img.shields.io/badge/RAG_with_pgvector-17171b?style=for-the-badge) ![Tesseract OCR](https://img.shields.io/badge/Tesseract_OCR-17171b?style=for-the-badge) ![OpenAI API](https://img.shields.io/badge/OpenAI_API-17171b?style=for-the-badge)

**Backend and data**

![FastAPI](https://img.shields.io/badge/FastAPI-17171b?style=for-the-badge&logo=fastapi&logoColor=38e062) ![Pydantic](https://img.shields.io/badge/Pydantic-17171b?style=for-the-badge&logo=pydantic&logoColor=38e062) ![Node.js](https://img.shields.io/badge/Node.js-17171b?style=for-the-badge&logo=nodedotjs&logoColor=38e062) ![Express](https://img.shields.io/badge/Express-17171b?style=for-the-badge&logo=express&logoColor=38e062) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17171b?style=for-the-badge&logo=postgresql&logoColor=38e062) ![Supabase](https://img.shields.io/badge/Supabase-17171b?style=for-the-badge&logo=supabase&logoColor=38e062) ![Redis](https://img.shields.io/badge/Redis-17171b?style=for-the-badge&logo=redis&logoColor=38e062) ![SQLite](https://img.shields.io/badge/SQLite-17171b?style=for-the-badge&logo=sqlite&logoColor=38e062) ![Prisma](https://img.shields.io/badge/Prisma-17171b?style=for-the-badge&logo=prisma&logoColor=38e062) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-17171b?style=for-the-badge&logo=sqlalchemy&logoColor=38e062)

**Frontend and mobile**

![Next.js](https://img.shields.io/badge/Next.js-17171b?style=for-the-badge&logo=nextdotjs&logoColor=38e062) ![React](https://img.shields.io/badge/React-17171b?style=for-the-badge&logo=react&logoColor=38e062) ![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-17171b?style=for-the-badge&logo=tailwindcss&logoColor=38e062) ![shadcn/ui](https://img.shields.io/badge/shadcn%2Fui-17171b?style=for-the-badge&logo=shadcnui&logoColor=38e062) ![Android](https://img.shields.io/badge/Android-17171b?style=for-the-badge&logo=android&logoColor=38e062)

**Testing and delivery**

![pytest](https://img.shields.io/badge/pytest-17171b?style=for-the-badge&logo=pytest&logoColor=38e062) ![Vitest](https://img.shields.io/badge/Vitest-17171b?style=for-the-badge&logo=vitest&logoColor=38e062) ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-17171b?style=for-the-badge&logo=githubactions&logoColor=38e062) ![Docker](https://img.shields.io/badge/Docker-17171b?style=for-the-badge&logo=docker&logoColor=38e062) ![Vercel](https://img.shields.io/badge/Vercel-17171b?style=for-the-badge&logo=vercel&logoColor=38e062) ![Render](https://img.shields.io/badge/Render-17171b?style=for-the-badge&logo=render&logoColor=38e062) ![Sentry](https://img.shields.io/badge/Sentry-17171b?style=for-the-badge&logo=sentry&logoColor=38e062) ![Postman](https://img.shields.io/badge/Postman-17171b?style=for-the-badge&logo=postman&logoColor=38e062) ![Playwright](https://img.shields.io/badge/Playwright-17171b?style=for-the-badge)

**Also**

![Figma](https://img.shields.io/badge/Figma-17171b?style=for-the-badge&logo=figma&logoColor=38e062) ![Linux CLI](https://img.shields.io/badge/Linux_CLI-17171b?style=for-the-badge&logo=linux&logoColor=38e062) ![Raspberry Pi 5](https://img.shields.io/badge/Raspberry_Pi_5-17171b?style=for-the-badge&logo=raspberrypi&logoColor=38e062)

## GitHub

<p align="center">
  <img src="https://github-readme-stats.shion.dev/api?username=Sowan3k&show_icons=true&include_all_commits=true&count_private=true&hide_rank=true&hide=issues,contribs&card_width=330&bg_color=09090b&border_color=27272a&border_radius=15&title_color=fafafa&text_color=a1a1aa&icon_color=38e062&ring_color=38e062" height="160" alt="GitHub stats">
  <img src="https://github-readme-stats.shion.dev/api/top-langs/?username=Sowan3k&layout=compact&langs_count=5&card_width=320&bg_color=09090b&border_color=27272a&border_radius=15&title_color=fafafa&text_color=a1a1aa" height="160" alt="Top languages">
</p>

<p align="center">
  <img src="https://streak-stats.demolab.com/?user=Sowan3k&background=09090b&border=27272a&border_radius=15&stroke=27272a&ring=38e062&fire=38e062&currStreakNum=fafafa&sideNums=fafafa&currStreakLabel=38e062&sideLabels=a1a1aa&dates=a1a1aa" alt="Contribution streak">
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Sowan3k/Sowan3k/output/snake-dark.svg">
    <img src="https://raw.githubusercontent.com/Sowan3k/Sowan3k/output/snake.svg" width="100%" alt="Animated contribution graph">
  </picture>
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=Sowan3k&style=flat-square&color=38e062&label=profile+views" alt="Profile views">
</p>
