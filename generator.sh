mkdir -p source
python3 -c 'import this' | \
python3 -c "import sys;import re;import string;input_dir='source';[open(f'{input_dir}/source{index}', 'w').write(line) for index, line in enumerate(re.sub(f'[{string.punctuation}]', '', sys.stdin.read().lower()).split('\n')) if line.strip()]"
