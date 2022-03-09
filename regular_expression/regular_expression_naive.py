regular_expression_str = "(ab+)*|(cab)+"
"""
(ab+)*|(cab)+
(abb*)*|cab(cab)*
abb*|(cab)*cab

"""

# text_1 = "abbabbbcabcab"
text_1 = "aaccbbabbbcabcab"

"""
abcab
abbcabcab
abbbbcabcabcab
abbabbabaabbb
"""

# def match_pattern(text):
