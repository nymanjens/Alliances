all

# Rule configuration
rule 'line-length', :line_length => 100
rule 'ul-indent', :indent => 4

# Permanently disabled rules
exclude_rule 'list-indent' # Inconsistent indentation for list items at the same level
exclude_rule 'ul-start-left' # Consider starting bulleted lists at the beginning of the line
exclude_rule 'no-inline-html' # Inline HTML
exclude_rule 'single-h1' # Multiple top level headers in the same document
exclude_rule 'no-emphasis-as-header' # Emphasis used instead of a header
exclude_rule 'no-duplicate-header' # Multiple headers with the same content
