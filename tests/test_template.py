from scripts.alchemist.template import HEADINGS, MAX_RATHER_THAN, validate_body


def body(definition="The object, defined in one sentence a reader could quote.",
         expression="$$\nS(t) = P(T \\gt t)\n$$\n\nHere $S$ is the survival function and $T$ the event time.",
         why="A hazard divides by survival, so the hazard rate needs it next."):
    return (f"## Definition\n\n{definition}\n\n## The expression\n\n{expression}\n\n"
            f"## Why this node exists\n\n{why}\n")


def test_the_headings_are_the_spec_s_three_in_order():
    assert HEADINGS == ("## Definition", "## The expression", "## Why this node exists")
    assert MAX_RATHER_THAN == 1


def test_a_conforming_body_has_no_problems():
    assert validate_body(body()) == []


def test_a_missing_section_is_one_problem_naming_the_order():
    missing = body().split("## Why this node exists")[0]
    problems = validate_body(missing)
    assert len(problems) == 1 and "in that order" in problems[0]


def test_sections_out_of_order_fail():
    swapped = (body().replace("## Definition", "## TEMP")
               .replace("## The expression", "## Definition")
               .replace("## TEMP", "## The expression"))
    problems = validate_body(swapped)
    assert len(problems) == 1 and "in that order" in problems[0]


def test_a_fourth_heading_of_any_level_fails():
    problems = validate_body(body() + "\n### A note\n\nMore.\n")
    assert len(problems) == 1 and "no other heading" in problems[0]


def test_text_before_the_first_heading_fails():
    problems = validate_body("A preamble.\n\n" + body())
    assert len(problems) == 1 and "before the first heading" in problems[0]


def test_an_empty_section_fails():
    problems = validate_body(body(why=""))
    assert len(problems) == 1 and "no text beneath" in problems[0]


def test_no_display_block_fails():
    problems = validate_body(body(expression="Inline $S(t) = P(T \\gt t)$ only."))
    assert len(problems) == 1 and "no display block" in problems[0]


def test_two_display_blocks_pass_and_three_fail():
    two = body(expression="$$\na\n$$\n\n$$\nb\n$$\n\nHere $a$ and $b$ are named.")
    assert validate_body(two) == []
    three = body(expression="$$\na\n$$\n\n$$\nb\n$$\n\n$$\nc\n$$\n\nHere $a$, $b$ and $c$.")
    problems = validate_body(three)
    assert len(problems) == 1 and "3 display blocks" in problems[0]


def test_an_em_dash_and_an_en_dash_each_fail_with_the_line_named():
    for dash in ("—", "–"):
        problems = validate_body(body(why=f"A hazard {dash} defined above {dash} divides by survival."))
        assert len(problems) == 2 and all("dash on line 15" in p for p in problems)


def test_a_hyphen_in_a_compound_passes():
    assert validate_body(body(definition="A left-truncated duration, defined.")) == []


def test_a_currency_amount_fails_and_inline_maths_does_not():
    """`$2m` and `$1,500` are currency and fail; `$1$` is the number one in
    maths and passes. Every `$` on the page is a maths delimiter, which is why
    the rule targets the amount pattern and never the bare sign."""
    assert any("currency" in p for p in validate_body(body(definition="An exposure of $2m, defined.")))
    assert any("currency" in p for p in validate_body(body(definition="An exposure of $1,500, defined.")))
    assert any("currency" in p for p in validate_body(body(definition="Some $1.5 billion of exposure.")))
    assert validate_body(body(definition="So $S(0) = 1$ holds, and exactly $1$ unit is at risk.")) == []


def test_rather_than_once_passes_and_twice_fails():
    once = body(why="A hazard is estimated rather than assumed, and the hazard rate needs it next.")
    assert validate_body(once) == []
    twice = body(definition="Defined rather than derived.",
                 why="A hazard is estimated rather than assumed, and the hazard rate needs it next.")
    problems = validate_body(twice)
    assert len(problems) == 1 and "'rather than' appears 2 times" in problems[0]


def test_two_bare_amounts_on_a_line_fail():
    """The case CLAUDE.md warns about: `$500 and $600` is valid TeX between the
    two signs, so KaTeX stays silent and the page publishes garbled."""
    problems = validate_body(body(definition="A fee of $500 and a limit of $600, defined."))
    assert any("currency" in p for p in problems)


def test_inline_maths_that_looks_like_an_amount_passes():
    """Closed by its own `$`, these are maths, never currency."""
    assert validate_body(body(definition="The scale is $2m$ and the count $1,000$, defined.")) == []
