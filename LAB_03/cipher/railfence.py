class RailFenceCipher:
    def __init__(self):
        pass

    def validate_input(self, text, num_rails):
        if text is None or text.strip() == "":
            raise ValueError("Text không được rỗng")
        try:
            num_rails = int(num_rails)
        except ValueError:
            raise ValueError("Key phải là số nguyên")
        if num_rails < 2:
            raise ValueError("Key phải >= 2")
        if num_rails > len(text):
            raise ValueError("Key không được lớn hơn độ dài text")
        return num_rails

    def create_pattern(self, text_length, num_rails):
        pattern = []
        rail_index = 0
        direction = 1
        for _ in range(text_length):
            pattern.append(rail_index)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += (direction if num_rails > 1 else 0)
        return pattern

    def rail_fence_encrypt(self, plain_text, num_rails):
        num_rails = self.validate_input(plain_text, num_rails)
        pattern = self.create_pattern(len(plain_text), num_rails)
        rails = [[] for _ in range(num_rails)]
        for char, rail in zip(plain_text, pattern):
            rails[rail].append(char)
        return ''.join(''.join(rail) for rail in rails)

    def rail_fence_decrypt(self, cipher_text, num_rails):
        num_rails = self.validate_input(cipher_text, num_rails)
        pattern = self.create_pattern(len(cipher_text), num_rails)
        rails = [[] for _ in range(num_rails)]
        index = 0
        for rail in range(num_rails):
            count = pattern.count(rail)
            rails[rail] = list(cipher_text[index:index + count])
            index += count
        plain_text = ""
        for rail in pattern:
            plain_text += rails[rail].pop(0)
        return plain_text
