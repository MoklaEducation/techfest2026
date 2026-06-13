import sys

def is_moon_password(phrase: str) -> bool:
    cleaned = ''.join(ch.lower() for ch in phrase if ch != ' ')
    return cleaned == cleaned[::-1]

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    t = int(data[0].strip())
    phrases = data[1:1+t]
    ans = ['TRUE' if is_moon_password(p) else 'FALSE' for p in phrases]
    sys.stdout.write('\n'.join(ans))

if __name__ == '__main__':
    main()
