# Chapter 25: Sending Claude Things That Are Not Text

## Twenty-eight

Twenty-eight pixels by twenty-eight pixels. That is the size of a single patch, and every number in this chapter is arithmetic built on it. Claude reads an image by tiling it into a grid of these 28×28 squares and charging one visual token per square. An easy-to-overlook measurement decides the entire cost of everything you send that isn't text.

Put a real number on it before going further: an ordinary 1,000×1,000 pixel screenshot, the kind a support ticket arrives with most days, costs about 1,296 visual tokens before Claude reads a single word of your prompt. That cost is knowable in advance, the same way an airline can price a checked bag from its dimensions and weight before you reach the counter, with the same fee landing on the same numbers every time. Image tokens work the same way: a formula you can run before you send the request, patch count in, token count out.

This chapter runs like a budget. Build a request line by line, keep a running total, and by the end you can price an image, a PDF, and the delivery method you send either one by, before you commit to sending anything.

## Line one: what a patch costs

The formula, stated once: an image costs ⌈width / 28⌉ × ⌈height / 28⌉ visual tokens. Each dimension is divided by 28, rounded up to the next whole patch, and the two patch counts are multiplied together. The grid doesn't know what's drawn inside it, only how many squares it takes to cover the image, so a mostly blank screenshot and a busy one of the same pixel size cost the same.

Every model also carries a maximum native resolution it will accept, expressed two ways: a long-edge pixel limit and a visual-token limit. Both differ by model tier, and newer models accept meaningfully larger images than older ones did. The specific numbers move between model generations, sometimes within the same year, so confirm the current per-tier limits against the Vision page at build time rather than treating any number here as fixed. What stays constant is the shape of the constraint: two ceilings, tier-specific, both subject to change.

An image bigger than either ceiling gets downscaled before Claude processes it, and the patch formula then runs against the scaled dimensions. Hold that fact. It's the ledger's first genuine trap, and it earns its own section below.

## Running the total: the arithmetic itself

Take that 1,000×1,000 screenshot and do the division by hand, the way you'd actually check it before shipping a request. 1,000 divided by 28 is 35.7. Round up to the next whole patch: 36. Do the same for the height, since the image is square: also 36. Multiply the two patch counts: 36 × 36 = 1,296. That's the figure from the opening line, and it now has a derivation behind it instead of just an assertion.

Run the comparison that makes the number land: at that rate, ten high-resolution screenshots consume as much context as a detailed system prompt. A support workflow pasting in one screenshot per ticket, across ten tickets in a session, has spent a system-prompt's worth of budget on images alone, before a word of ticket text or Claude's diagnosis gets counted.

Two things fall out of that arithmetic worth carrying forward. The ceiling operation has a real effect on the bill: a 1,001×1,000 image and a 1,020×1,000 image both round up to the same 36-patch height, so small differences near a rounding boundary cost exactly the same. And the formula runs per image: three screenshots in one request are three separate ⌈w/28⌉×⌈h/28⌉ calculations, added together.

## The line you compute on: original size, or the size it becomes

Here is where the airline comparison stops matching the mechanism, and the gap is worth naming precisely, because it's checkable and it's exactly the kind of nuance a scenario stem is built to test. An airline's size limit is enforced at the counter: an oversized bag draws an excess fee or gets turned away on the spot, priced against the dimensions the bag actually has. An oversized image gets no such rejection. It is downscaled before Claude processes it, and the patch formula then runs on the scaled dimensions, not the ones in the original file.

That changes which number you should actually be computing. Run the raw formula on a 4,000×3,000 pixel photo and it looks enormous: ⌈4000/28⌉ × ⌈3000/28⌉ = 143 × 108, over 15,000 visual tokens. But if that resolution exceeds the model's ceiling, Claude downscales it first, and the real charge lands on whatever the scaled dimensions turn out to be, likely a fraction of that figure. Budgeting against the file you have, instead of the file Claude will actually see, gets this arithmetic wrong in either direction.

## Line two: how the bytes actually travel

The patch formula prices what an image costs once it arrives. A separate line on the ledger is how it gets there, and the three delivery methods trade off differently.

Inline base64 encodes the image bytes directly into the message. The full payload travels with every request, which inflates request size and adds to latency on large images. Reach for it on a one-off image, something sent exactly once. If that same image comes back on a later turn, the cost of sending the same bytes multiplies with every repeat.

A URL reference carries no payload at all; Claude fetches the image from the address you give it. The tradeoff moves from bytes to a dependency: the URL has to stay stable, public, and reachable at the exact moment the request runs. Anything behind auth, or signed with a short expiry, breaks this method before Claude ever sees the image.

The Files API uploads the image once, hands back a `file_id`, and every later request carries just that ID. The upload is a one-time cost; everything after it is close to free on the payload side. It fits the case where the same image or PDF appears across multiple requests or turns. Two conditions are worth checking before relying on it: it's currently in beta, and it isn't available on Bedrock or Vertex AI, so confirm it exists on your deployment platform before the reuse math depends on it.

## Same ledger, a different block: PDFs

PDFs use a `document` block instead of `image`, but the ledger doesn't change shape. The source can be base64, a URL, or a Files API `file_id`, the same three lines above, and the same token-cost mechanics and reuse logic apply once the file is in.

```
{
  "type": "document",
  "source": {
    "type": "base64",
    "media_type": "application/pdf",
    "data": "<base64-encoded-pdf-bytes>"
  },
  "title": "contract_review.pdf"
}
```

There's no required `name` field. `title` and `context` are both optional, there for a readable label and extra metadata; the cost formula doesn't read either one. The field names matter less than the fact that a PDF is priced and delivered on the same three-line ledger an image is.

## The one line text never has to itemize

Structuring a prompt for an image needs one line beyond what a text prompt needs: a statement of how to handle the image's own ambiguity. Objects overlap. Depth and spatial relationships aren't stated anywhere in the pixels. Part of something sits behind something else. A bare "describe this image" prompt produces the same shallow output a bare text prompt does, for the same reason: no target structure to aim for. But an image prompt also needs to say what to do when the picture itself is ambiguous. "If objects overlap, describe each separately and note the overlap" is a constraint a text-only prompt would never need to write, because text has nothing sitting behind anything else.

## Closing the ledger

Two lines stay off this chapter's page on purpose. The choice between a synchronous request and the Batch API is chapter 5's decision, made on latency. What does belong here: an image or PDF submitted through a batch call still prices out by the same patch formula and the same delivery-method tradeoffs above, so a batch job processing thousands of screenshots multiplies the per-item image cost by exactly as many items as it multiplies the text cost by. Running inside a batch call changes the per-token rate and the latency model. A single image's price is unaffected.

The other line worth closing on is scale. A pipeline loading two or three large images per request can work fine in a demo and still blow past context limits once it's handling production volume, because nobody ran this chapter's arithmetic against production-sized inputs before shipping. Measure token cost against production-scale inputs before you build.

## The tell

A stem naming this chapter says "screenshot," "PDF," "vision," "resize," "base64," or `file_id`, or hands you an image's pixel dimensions and asks what it costs. A scenario that instead hinges on how many times the same asset gets reused, or on whether a request runs once or repeatedly, is testing the delivery-method line.

## Self-test

**1.** A 700 × 900 pixel image is sent to Claude. What is its approximate visual token cost? *(Select one.)*

A. ⌈700/28⌉ + ⌈900/28⌉ = 25 + 33 = 58 tokens
B. ⌈700/28⌉ × ⌈900/28⌉ = 25 × 33 = 825 tokens
C. 700 × 900 ÷ 28 = 22,500 tokens
D. (700 + 900) ÷ 28 = 57 tokens, rounded up

**2.** A team sends a 6,000 × 4,000 pixel product photo that exceeds the model's resolution ceiling. What actually happens, and what should the team compute the token cost against? *(Select one.)*

A. The request is rejected outright, the same way an airline rejects an overweight bag at check-in.
B. Claude processes the full original resolution regardless of the ceiling, so the raw dimensions are the right numbers to budget against.
C. Claude downscales the image before processing, so the token cost should be computed against the scaled dimensions it produces.
D. The image is silently dropped from the request, and only the text prompt is processed.

**3.** Which two of the following are genuine reasons to choose the Files API over inline base64 for an image? *(Select 2 of 4.)*

A. The same image will be sent across multiple requests or conversation turns.
B. The image only needs to be sent once and will never be reused.
C. Repeated payload transfer would otherwise dominate request size.
D. The Files API is available on every deployment platform, including Bedrock and Vertex AI.

**4.** A PDF needs to be sent for analysis, and the same document will be referenced across several follow-up turns. Which statement is accurate? *(Select one.)*

A. PDFs use an image block with a required name field, and the reuse logic that applies to images doesn't apply to them.
B. PDFs use a document block; the source can be base64, a URL, or a Files API file_id, and the same token-cost and reuse mechanics as images apply.
C. PDFs cannot be uploaded through the Files API; only base64 encoding is supported.
D. PDF token cost is fixed per page and does not depend on delivery method.

**5.** A nightly batch job classifies 50,000 product images against a fixed taxonomy. Which statement about cost is accurate? *(Select one.)*

A. Running inside the Batch API removes image token cost entirely; only text tokens are charged.
B. Each image is still priced by the same patch formula, so the per-item image cost multiplies across all 50,000 items the same way it would synchronously.
C. Batch requests price images by file size in megabytes rather than by patch count.
D. Only the first image in a batch call is charged; every other image in the same batch is free.

**Answers.** 1: B. The formula multiplies the two ceiling-rounded patch counts; it doesn't add them, and it doesn't divide raw pixel area by 28. 2: C. Oversized images are downscaled before processing rather than rejected, so the patch formula runs on the scaled dimensions. 3: A and C. Reuse across turns and a large payload that would otherwise dominate request size are the reasons to pay the Files API's one-time upload cost. B describes exactly the case where inline base64 fits better, and D is false: the Files API is currently unavailable on Bedrock and Vertex AI. 4: B. Document blocks share the same base64/URL/Files-API source structure and the same cost and reuse mechanics as image blocks, with no required name field. 5: B. The patch formula and per-image cost don't change inside a batch call; batch changes the per-token rate and the latency model, and each image is still priced individually.
