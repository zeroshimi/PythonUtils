import re

def RemoveExSpace(string: str):
    # コピペしたときに改行が半角スペースになってしまうので、日本語間の不必要な半角スペース削除
    return re.sub('([あ-んア-ン一-龥ー])\s+((?=[あ-んア-ン一-龥ー]))', r'\1\2', string)