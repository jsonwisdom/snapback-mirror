# Jason's Cards & Stuff — 2026 brand and commerce update (DRAFT)

Review artifact; not a deployed site, Facebook post, Stripe product, or payment system.

## Brand identity
- Public Facebook Page: https://www.facebook.com/jasonscardsandstuff/
- Original brands: Jason's Cards & Stuff; Garbage Press; JSON Cards; Computer Wisdom.
- Retain historical scans as archives, not as evidence of a Topps relationship.
- Proposed independent replacement cover: `JASONS_CARDS_STUFF_FACEBOOK_COVER_2026-11-06.png` (1640 × 624; locally generated, NOT yet committed or uploaded to Facebook).
- Distinct, typography-first cover. Do not use Topps logos, trademarks, packaging, third-party character art, or claims of endorsement on sale pages.
- Disclaimer: 'Independent project. Not affiliated with Topps or Garbage Pail Kids.' Disclaimers do not substitute for rights clearance.

## Facebook Page draft description
Independent original satirical trading-card art, JSON Cards, Garbage Press commentary, and Computer Wisdom research. We separate evidence from parody and preserve verifiable source records. Not affiliated with Topps or Garbage Pail Kids.

## Integration change contract
1. Preserve GitHub `main`, existing Cloudflare Workers, Stripe prices/products, payout routes, x402 settlement destination, and wallet identities unchanged.
2. Existing Cloudflare Workers identified read-only: `jasons-art-gallery`, `political-triggerdeck-2026`, `wisdom-catalog-curator`. No production API writes.
3. Connected Stripe Computer Wisdom live account: observed inactive draft products in JASON SKU series and zero Payment Links as checked 2026-11-06. No new product/price/Checkout activation.
4. Sale eligibility requires independently original/licensed art, clear product terms and pricing, review of applicable legal/platform restrictions, and Stripe Checkout with verified signed webhook events before digital delivery.
5. Wolfram validates arithmetic; SHA-256 compares bytes, not ownership or authorship. No signature/wallet authority claims.
6. ChatGPT content drafts require human editorial review and verifiable reporting citations. Label fiction/parody separately from claims of fact.
7. Repo update is draft-only. Do not publish to Facebook or merge without review of the art, disclosures and payment receipts.

## CI-FIRST 2026-11-06
- PASS: independent cover file created locally; dimensions and SHA-256 computed.
- PASS: GitHub repository and Cloudflare Workers inspected read-only.
- PASS: Stripe live account and read-only catalog/links list inspected.
- UNKNOWN: Facebook editor authorization, rights clearance, purchase/fulfillment receipts, Cloudflare runtime health, current wallet signing authority.
- NOT_ESTABLISHED: any new checkout, sale, Facebook publication, or x402 payout.
- FAIL: none found in this narrow isolated check; no broader integrity verdict is asserted.

## Reversibility
Do not merge this branch until reviewer approves. There are no modifications to existing source, deployed workers, or Stripe objects.
