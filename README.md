<p align="center">
  <img src="assets/header.svg" width="100%" alt="Noor Mohammad Sowan. Software engineer in Dhaka. I build AI automation and full-stack systems.">
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/noor-mohammad-sowan"><img src="https://img.shields.io/badge/LinkedIn-f2b34a?style=for-the-badge" alt="LinkedIn"></a>
  <a href="mailto:nurmohammadsowan119@gmail.com"><img src="https://img.shields.io/badge/Email-f2b34a?style=for-the-badge" alt="Email"></a>
  <a href="https://sowan-portfolio.vercel.app"><img src="https://img.shields.io/badge/Portfolio-f2b34a?style=for-the-badge" alt="Portfolio"></a>
  <a href="https://www.pexels.com/@noor-mohammad-sowan-944251072"><img src="https://img.shields.io/badge/Pexels-161d2b?style=for-the-badge" alt="Pexels"></a>
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

![Python](https://img.shields.io/badge/Python-161d2b?style=for-the-badge&logo=python&logoColor=f2b34a) ![TypeScript](https://img.shields.io/badge/TypeScript-161d2b?style=for-the-badge&logo=typescript&logoColor=f2b34a) ![JavaScript](https://img.shields.io/badge/JavaScript-161d2b?style=for-the-badge&logo=javascript&logoColor=f2b34a) ![Kotlin](https://img.shields.io/badge/Kotlin-161d2b?style=for-the-badge&logo=kotlin&logoColor=f2b34a) ![SQL](https://img.shields.io/badge/SQL-161d2b?style=for-the-badge)

**AI and automation**

![LangChain](https://img.shields.io/badge/LangChain-161d2b?style=for-the-badge&logo=langchain&logoColor=f2b34a) ![Gemini API](https://img.shields.io/badge/Gemini_API-161d2b?style=for-the-badge&logo=googlegemini&logoColor=f2b34a) ![Ollama](https://img.shields.io/badge/Ollama-161d2b?style=for-the-badge&logo=ollama&logoColor=f2b34a) ![n8n](https://img.shields.io/badge/n8n-161d2b?style=for-the-badge&logo=n8n&logoColor=f2b34a) ![OpenCV](https://img.shields.io/badge/OpenCV-161d2b?style=for-the-badge&logo=opencv&logoColor=f2b34a) ![RAG with pgvector](https://img.shields.io/badge/RAG_with_pgvector-161d2b?style=for-the-badge) ![Tesseract OCR](https://img.shields.io/badge/Tesseract_OCR-161d2b?style=for-the-badge) ![OpenAI API](https://img.shields.io/badge/OpenAI_API-161d2b?style=for-the-badge)

**Backend and data**

![FastAPI](https://img.shields.io/badge/FastAPI-161d2b?style=for-the-badge&logo=fastapi&logoColor=f2b34a) ![Pydantic](https://img.shields.io/badge/Pydantic-161d2b?style=for-the-badge&logo=pydantic&logoColor=f2b34a) ![Node.js](https://img.shields.io/badge/Node.js-161d2b?style=for-the-badge&logo=nodedotjs&logoColor=f2b34a) ![Express](https://img.shields.io/badge/Express-161d2b?style=for-the-badge&logo=express&logoColor=f2b34a) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-161d2b?style=for-the-badge&logo=postgresql&logoColor=f2b34a) ![Supabase](https://img.shields.io/badge/Supabase-161d2b?style=for-the-badge&logo=supabase&logoColor=f2b34a) ![Redis](https://img.shields.io/badge/Redis-161d2b?style=for-the-badge&logo=redis&logoColor=f2b34a) ![SQLite](https://img.shields.io/badge/SQLite-161d2b?style=for-the-badge&logo=sqlite&logoColor=f2b34a) ![Prisma](https://img.shields.io/badge/Prisma-161d2b?style=for-the-badge&logo=prisma&logoColor=f2b34a) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-161d2b?style=for-the-badge&logo=sqlalchemy&logoColor=f2b34a)

**Frontend and mobile**

![Next.js](https://img.shields.io/badge/Next.js-161d2b?style=for-the-badge&logo=nextdotjs&logoColor=f2b34a) ![React](https://img.shields.io/badge/React-161d2b?style=for-the-badge&logo=react&logoColor=f2b34a) ![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-161d2b?style=for-the-badge&logo=tailwindcss&logoColor=f2b34a) ![shadcn/ui](https://img.shields.io/badge/shadcn%2Fui-161d2b?style=for-the-badge&logo=shadcnui&logoColor=f2b34a) ![Android](https://img.shields.io/badge/Android-161d2b?style=for-the-badge&logo=android&logoColor=f2b34a)

**Testing and delivery**

![pytest](https://img.shields.io/badge/pytest-161d2b?style=for-the-badge&logo=pytest&logoColor=f2b34a) ![Vitest](https://img.shields.io/badge/Vitest-161d2b?style=for-the-badge&logo=vitest&logoColor=f2b34a) ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-161d2b?style=for-the-badge&logo=githubactions&logoColor=f2b34a) ![Docker](https://img.shields.io/badge/Docker-161d2b?style=for-the-badge&logo=docker&logoColor=f2b34a) ![Vercel](https://img.shields.io/badge/Vercel-161d2b?style=for-the-badge&logo=vercel&logoColor=f2b34a) ![Render](https://img.shields.io/badge/Render-161d2b?style=for-the-badge&logo=render&logoColor=f2b34a) ![Sentry](https://img.shields.io/badge/Sentry-161d2b?style=for-the-badge&logo=sentry&logoColor=f2b34a) ![Postman](https://img.shields.io/badge/Postman-161d2b?style=for-the-badge&logo=postman&logoColor=f2b34a) ![Playwright](https://img.shields.io/badge/Playwright-161d2b?style=for-the-badge)

**Also**

![Figma](https://img.shields.io/badge/Figma-161d2b?style=for-the-badge&logo=figma&logoColor=f2b34a) ![Linux CLI](https://img.shields.io/badge/Linux_CLI-161d2b?style=for-the-badge&logo=linux&logoColor=f2b34a) ![Raspberry Pi 5](https://img.shields.io/badge/Raspberry_Pi_5-161d2b?style=for-the-badge&logo=raspberrypi&logoColor=f2b34a)

## GitHub

<p align="center">
  <img src="https://github-readme-stats.shion.dev/api?username=Sowan3k&show_icons=true&include_all_commits=true&count_private=true&hide_rank=true&hide=issues,contribs&card_width=330&bg_color=0b0f17&border_color=212a3a&border_radius=12&title_color=f2b34a&text_color=c3ccd9&icon_color=6cc7e6&ring_color=f2b34a" height="160" alt="GitHub stats">
  <img src="https://github-readme-stats.shion.dev/api/top-langs/?username=Sowan3k&layout=compact&langs_count=5&card_width=320&bg_color=0b0f17&border_color=212a3a&border_radius=12&title_color=f2b34a&text_color=c3ccd9" height="160" alt="Top languages">
</p>

<p align="center">
  <img src="https://streak-stats.demolab.com/?user=Sowan3k&background=0b0f17&border=212a3a&border_radius=12&stroke=212a3a&ring=f2b34a&fire=f2b34a&currStreakNum=e8edf4&sideNums=e8edf4&currStreakLabel=f2b34a&sideLabels=8a96a8&dates=56627a" alt="Contribution streak">
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Sowan3k/Sowan3k/output/snake-dark.svg">
    <img src="https://raw.githubusercontent.com/Sowan3k/Sowan3k/output/snake.svg" width="100%" alt="Animated contribution graph">
  </picture>
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=Sowan3k&style=flat-square&color=f2b34a&label=profile+views" alt="Profile views">
</p>
