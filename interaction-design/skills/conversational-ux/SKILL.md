---
name: conversational-ux
description: Design voice and conversational interfaces — dialog flows, error recovery, and persona. Use when the interface speaks and listens rather than being tapped. For graphical input collection, use `form-design`.
---
# Conversational UX

You are an expert in designing voice interfaces, chatbots, and AI-driven conversational experiences.

## What You Do

You design the dialog structure, turn logic, error recovery, and persona for voice and conversational interfaces — applying the distinct interaction model that applies when there is no visual UI to explore, or when speech is the primary channel.

## Two Surfaces, One Discipline

**Voice interfaces** (IVR, smart speaker skills, voice assistants): audio-only or audio-primary. No screen to scan. No buttons to click. The interface exists only in the moment of the utterance.

**Conversational UI** (chatbots, AI assistants, messaging interfaces): text-based, but governed by conversation turn structure rather than screen layout. Users read and respond; they do not navigate spatially.

Both share the same underlying design discipline: scripting what the system says, anticipating what the user might say, and handling the gaps between them.

## The Conversation Turn

Every conversational interaction is built from turns:

1. **System prompt** — the interface speaks or displays a message
2. **User response** — the user speaks or types
3. **System acknowledgement and next prompt** — the interface confirms it understood and continues

Designing a conversational interface is designing the script for every meaningful path through this loop.

### What a good system prompt does
- States one clear thing (not three)
- Signals what kind of response is expected
- Does not bury the call to action at the end of a long sentence
- On voice: reads naturally when spoken aloud — punctuation affects cadence

### Confirmation strategies

| Confirmation type | When to use |
|---|---|
| Explicit ("You said Tuesday at 3pm — is that right?") | High-stakes actions, easily confused inputs |
| Implicit ("Booking for Tuesday at 3pm…") | Low-stakes, recoverable actions |
| None | When misrecognition is rare and recovery is easy |

## Error Handling

Conversational error recovery is the highest-leverage design surface. Most conversational experiences fail because they do not handle the gap between what the system expected and what the user said.

### Error types

- **No input** — user did not respond; re-prompt with a shorter version of the original
- **No match / misrecognition** — system heard something but could not parse intent; ask for clarification, offer examples
- **Out-of-scope input** — user said something the system cannot handle; acknowledge and redirect without pretending to understand
- **Partial match** — system understood part of the request; confirm what it understood and ask for the missing piece

### The error reprompt ladder

1. First error: rephrase the prompt with slightly more context
2. Second error: offer explicit examples or constrained choices ("You can say 'morning', 'afternoon', or 'evening'")
3. Third error: offer a graceful exit — a live agent, a different channel, or a clear stopping point

Never loop the same error prompt more than once. Each reprompt must add information.

## Voice-Specific Design

### Writing for ears, not eyes

- Short sentences — voice working memory is shorter than visual
- Active voice — passive constructions are harder to parse aurally
- No visual-only elements — "click the button below" is meaningless on voice
- Spell out abbreviations and acronyms — "ETA" should be "estimated arrival time" on first use
- Avoid lists longer than three items — users cannot re-read; chunk or sequence instead

### Latency and pacing

- Keep system responses under 8 seconds where possible; long silences break the conversation model
- Use earcons (audio cues) to signal state transitions — recording started, processing, done
- On smart speakers, use explicit listening cues ("Go ahead" / chime) to signal when the mic is open

### Multimodal (voice + screen)

Alexa Show, Google Nest Hub, and phone assistants combine voice with a display. Design rules:
- The spoken word must make sense without the screen — not all users look at the screen
- The screen reinforces and disambiguates; it does not replace the spoken prompt
- Interactive visual elements (cards, buttons) must also be activatable by voice

## Conversational UI (Text Chat) Specifics

### Affordances in text interfaces

Unlike voice, text conversational UI can show interface elements:
- **Quick replies / suggestion chips**: constrain the interaction to reduce typing friction; use for common paths, not all paths
- **Persistent menu**: hamburger or menu icon providing navigation outside the conversation thread
- **Typing indicator**: shows the system is processing; suppresses user anxiety during latency
- **Structured cards**: present information (flight details, product results) within the chat stream — more scannable than raw prose

### Distinguishing the conversation from navigation

Text conversational UI tends toward one of two models:
- **Pure conversation**: no persistent UI chrome; all navigation happens through dialogue
- **Hybrid**: conversational input field within a screen-based product; the chat handles help, search, and action initiation; the rest of the product is conventional UI

Do not apply conversational UX patterns to workflows that are better served by a form, a table, or a menu. Conversation excels at ambiguous, open-ended, or multi-step tasks where the user does not know the exact path. It fails at tasks with many required fields or complex parallel selections.

## Persona and Tone

The system's voice is a design decision, not a default:
- **Name and identity**: does the assistant have a name? A consistent one reduces confusion in multimodal contexts
- **Register**: formal, professional, warm, playful — should match the product's brand and the emotional context of the conversation
- **Handling failures gracefully**: the persona must remain consistent when the system fails — robotic error messages that break the established voice undermine trust
- **Avoiding false humanity**: conversational UI should not claim to be human when sincerely asked; this applies to text as much as voice

## Best Practices

- Write every prompt aloud before shipping — if it sounds unnatural spoken, rewrite it
- Design the unhappy path first: error handling and out-of-scope recovery define the experience quality more than the happy path
- Constrain choice at decision points — open-ended "What would you like to do?" fails more often than "Would you like to start, or pick up where you left off?"
- Test with real speech on real devices; text-to-speech synthesis changes cadence in ways that are invisible in a script
- Log what users actually say; the gap between expected utterances and real ones is your highest-value design data
- Design exit paths explicitly — users must always be able to stop, restart, or escalate to a human channel
