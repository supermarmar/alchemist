// Read spans as JSON on stdin, render each with KaTeX throwing on error, and
// write the failures back as JSON. Node is used rather than a Python TeX parser
// because KaTeX itself is the only authority on what KaTeX accepts.
import { readFileSync } from "node:fs";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const katex = require("../vendor/katex/katex.min.js");

const spans = JSON.parse(readFileSync(0, "utf8"));
const failures = spans.map((span) => {
  try {
    katex.renderToString(span.tex, {
      displayMode: span.display,
      throwOnError: true,
      strict: "warn",
    });
    return null;
  } catch (error) {
    const kind = span.display ? "display" : "inline";
    return `${span.file}:${span.line} (${kind}): ${error.message}`;
  }
});
process.stdout.write(JSON.stringify(failures));
