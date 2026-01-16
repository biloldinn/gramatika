# Upgrade Plan

## User Requirements
- Automatic daily 5 words via AI.
- "Learn Word" button functionality (Grammar, Examples).
- Fix bugs ("hatolarni tigilla").
- Audio/Reading included.

## Changes
1.  **AI Prompting**: Change to JSON output for structured data.
2.  **UI/UX**:
    -   Send Word + Meaning + Reading.
    -   Attach Inline Keyboard: [🔊 Audio] [ℹ️ Grammar] [✍️ Usage].
3.  **Interaction**:
    -   Clicking [🔊 Audio] sends voice.
    -   Clicking [ℹ️ Grammar] sends alert/message with grammar rule.
    -   Clicking [✍️ Usage] sends example sentence.
4.  **Code Structure**: Refactor `ai_generate_words` and message sending logic.

## Execution
- Rewrite `bot.py`.
- Run `python bot.py`.
