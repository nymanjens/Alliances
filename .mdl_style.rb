all

# Rule configuration
rule 'line-length', :line_length => 100
rule 'ul-indent', :indent => 4

# Permanently disabled rules
exclude_rule 'no-inline-html' # Inline HTML
exclude_rule 'single-h1' # Multiple top level headers in the same document

# Disabled rules to be revisited
exclude_rule 'MD034' # Bare URL used
exclude_rule 'MD036' # Emphasis used instead of a header
exclude_rule 'MD041' # First line in file should be a top level header
