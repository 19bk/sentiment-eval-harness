<!--
LinkedIn article draft. To publish:
  1. LinkedIn → Write article. Title + subtitle go in the LinkedIn fields (below).
  2. Upload the three PNGs from assets/ at the [IMAGE] marks (export-free; they're committed).
  3. Image 3 (results) also makes the strongest cover image.
  Note: LinkedIn's editor does NOT render Markdown. Don't paste this file raw; retype headings/bold
  using LinkedIn's native formatting and upload the images by hand. (This file is the GitHub writeup.)
This file also renders as the repo's long-form writeup on GitHub (images embed via relative paths).
Audience: mostly non-technical. Voice: plain English, no jargon, no em dashes. All numbers trace to this repo.
-->

# In the demo it was 100% accurate. It was actually 50%.

*How I caught my own AI being confidently wrong, and the simple test that keeps it honest.*

I built a small AI tool and showed it off. Every example I tried, it got right. 100%. It felt finished.

Then I tested it properly, and it was right half the time.

Same code. The only thing that changed was the questions I asked it. That gap, between "looked great" and "actually works," is the most expensive misunderstanding in AI today. Here is how I found it, and the simple habit that closes it.

## An eval is just a test with an answer key

![A test for an AI: take examples with known answers, run the AI, and score what it gets right](assets/what-is-an-eval.png)

Think about how you trust normal software. Type 2 + 2 into a calculator and you get 4, today and forever. Test it once, trust it always.

AI is not like that. Ask it the same question twice and it can be brilliant one time and confidently wrong the next, and the wrong answer sounds every bit as sure as the right one. On top of that, when you try out a new tool you naturally feed it the things you expect it to handle. You never see the rest.

An eval is the fix, and it is exactly what it sounds like: a test for an AI. You gather real examples where you already know the correct answer, run them all through the system, and score it like a teacher with an answer key. Now you are not saying "it seems good." You are saying "it is right 85% of the time, and here is exactly where it gets things wrong."

## I watched it happen on my own code

To make this concrete, I built the simplest possible version: a tool that reads a sentence and decides whether it sounds happy or unhappy.

In my demo it was perfect. So I sat it down for a real exam, a set of sentences I would never bother showing off.

![The demo said 100%. A real test said 50%. After a three-line fix, 90%. Sarcasm still fails](assets/results.png)

It dropped to 50%, and the test showed me precisely why. It aced the easy, obvious sentences and got the tricky ones backwards, every single time. Sentences like "not bad" or "wasn't terrible," where the words look negative but the meaning is positive. My tool was simply counting happy words and sad words, so it could not see the word "not." No demo of cheerful examples was ever going to reveal that.

The fix was tiny, about three lines. The score jumped to 90%.

## The best thing a test can do is point at the next problem

Here is the part I love. The test did not just grade me. It pointed straight at the next wall: every version still scores zero on sarcasm, like "Oh great, it broke again." That is not the test failing. That is the test writing my next to-do for me.

That is the whole loop, and it is the same whether you are checking three lines of code or the most advanced AI on the planet.

![The loop: a set of known answers, run the system, score it, decide ship or block, and every failure becomes a new test](assets/how-evals-work.png)

If you remember one thing: a demo shows you what an AI gets right. An eval shows you what it gets wrong. Only one of those tells you whether it is safe to ship.

## Why this matters to you, even if you never touch code

Modern AI is moving past just answering questions. It is starting to take actions on its own: booking, buying, replying, deciding, across many steps in a row. One confident mistake early on quietly corrupts everything that comes after it.

When someone's paycheck, a customer's refund, or a missed delivery depends on that, "it looked fine when we tried it" is not an acceptable answer. Somebody has to be able to say, with evidence, how often it is right and where it breaks. That is the work.

## What I actually do

That is the skill I bring. I make AI systems prove they work, in numbers a business can trust, and I find the failures before customers do.

If that is useful to you, follow along. I write about making AI trustworthy, in plain English. The little project behind this post is public, runs in seconds, and needs nothing installed: github.com/19bk/sentiment-eval-harness.

So I will ask you the question this taught me to ask: what is the most confidently wrong answer an AI has ever given you?
