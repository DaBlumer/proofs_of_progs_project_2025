from pygments.lexer import RegexLexer, words
from pygments.token import Text, Comment, Operator, Keyword, Name, String, Number, Punctuation, Error

class WhyMLLexer(RegexLexer):
    name = 'WhyML'
    aliases = 'whyml'

    keywords = (
        'abstract', 'absurd', 'alias', 'any', 'as', 'assert', 'assume', 'at', 'axiom',
        'begin', 'break', 'by', 'check', 'clone', 'coinductive', 'constant', 'continue',
        'diverges', 'do', 'done', 'downto',
        'else', 'end', 'ensures', 'epsilon', 'exception', 'exists', 'export',
        'false', 'float', 'for', 'forall', 'fun', 'function', 'ghost', 'goal',
        'if', 'import', 'in', 'inductive', 'invariant', 'label', 'lemma', 'let',
        'match', 'meta', 'module', 'mutable', 'not', 'old',
        'partial', 'predicate', 'private', 'pure',
        'raise', 'raises', 'range', 'reads', 'rec', 'ref', 'requires', 'return', 'returns',
        'scope', 'so', 'then', 'theory', 'to', 'true', 'try', 'type', 'use', 'val', 'variant',
        'while', 'with', 'writes',
    )

    tokens = {
        'root': [
            (r'\s+', Text),
            (r'\(\*\)', Operator),
            (r'\(\*', Comment, 'comment'),
            (r'\[@[^]]*\]', Comment),
            (words(keywords, suffix=r'\b'), Keyword),
            (r'[-~!%^&*+=|?<>/\\]', Operator),
            (r'[][{};:.,()]', Punctuation),
            (r"[^\W\d][\w']*", Name),
            (r'\bresult\b', Name.Builtin.Pseudo),

            (r'-?\d\d*([.]\d*)?([eE][+-]?\d\d*)', Number.Float),
            (r'-?0[xX][\da-fA-F][\da-fA-F]*([.][\da-fA-F]*)?([pP][+-]?\d\d*)', Number.Float),
            (r'0[xX][\da-fA-F][\da-fA-F_]*', Number.Hex),
            (r'0[oO][0-7][0-7_]*', Number.Oct),
            (r'0[bB][01][01_]*', Number.Bin),
            (r'\d[\d_]*', Number.Integer),

            (r"'", Keyword),
            (r'"', String.Double, 'string'),
        ],
        'comment': [
            (r'[^(*)]+', Comment),
            (r'\(\*', Comment, '#push'),
            (r'\*\)', Comment, '#pop'),
            (r'[(*)]', Comment),
        ],
        'string': [
            (r'[^\\"]+', String.Double),
            (r'\\[\\"\'ntbr]', String.Escape),
            (r'\\[0-9]{3}', String.Escape),
            (r'\\x[0-9a-fA-F]{2}', String.Escape),
            (r'\\\n', String.Double),
            (r'"', String.Double, '#pop'),
        ],
    }
