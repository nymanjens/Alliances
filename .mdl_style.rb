all

# Rule configuration
rule 'line-length', :line_length => 100

# Permanently disabled rules
exclude_rule 'no-inline-html'

# Disabled rules to be revisited
exclude_rule 'MD005' # Inconsistent indentation for list items at the same level
exclude_rule 'MD006' # Lists at beginning of line
exclude_rule 'MD007' # List indentation
exclude_rule 'MD022' # Headers should be surrounded by blank lines
exclude_rule 'MD025' # Multiple top level headers in the same document
exclude_rule 'MD032' # Lists should be surrounded by blank lines
exclude_rule 'MD034' # Bare URL used
exclude_rule 'MD036' # Emphasis used instead of a header
exclude_rule 'MD041' # First line in file should be a top level header
