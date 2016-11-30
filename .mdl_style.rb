all

# Rule configuration
rule 'line-length', :line_length => 100
rule 'ul-indent', :indent => 4

# Permanently disabled rules
exclude_rule 'no-inline-html' # Inline HTML
exclude_rule 'single-h1' # Multiple top level headers in the same document
exclude_rule 'no-emphasis-as-header' # Emphasis used instead of a header
