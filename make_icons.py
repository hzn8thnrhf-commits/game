"""Generate app icons (icon-180.png, icon-512.png) with no external deps."""
import struct, zlib


def make_icon(size, path):
    px = bytearray(size * size * 3)

    def put(x, y, rgb):
        i = (y * size + x) * 3
        px[i:i + 3] = bytes(rgb)

    top, bottom = (35, 42, 92), (21, 26, 58)
    for y in range(size):
        t = y / (size - 1)
        row = tuple(int(a + (b - a) * t) for a, b in zip(top, bottom))
        for x in range(size):
            put(x, y, row)

    # 3x3 grid of rounded blocks in the game palette
    colors = [
        (255, 92, 92), (255, 167, 38), (255, 212, 94),
        (102, 211, 110), (79, 195, 247), (92, 108, 255),
        (201, 108, 255), (255, 92, 92), (79, 195, 247),
    ]
    margin = size // 6
    area = size - 2 * margin
    gap = max(2, size // 45)
    cell = (area - 2 * gap) // 3
    radius = cell // 4
    for gy in range(3):
        for gx in range(3):
            color = colors[gy * 3 + gx]
            x0 = margin + gx * (cell + gap)
            y0 = margin + gy * (cell + gap)
            for y in range(cell):
                for x in range(cell):
                    # rounded corners
                    cx = min(x, cell - 1 - x)
                    cy = min(y, cell - 1 - y)
                    if cx < radius and cy < radius:
                        dx, dy = radius - cx, radius - cy
                        if dx * dx + dy * dy > radius * radius:
                            continue
                    # simple top-light shading
                    shade = 1.08 if y < cell // 5 else (0.82 if y > cell * 4 // 5 else 1.0)
                    rgb = tuple(min(255, int(c * shade)) for c in color)
                    put(x0 + x, y0 + y, rgb)

    raw = b"".join(b"\x00" + bytes(px[y * size * 3:(y + 1) * size * 3]) for y in range(size))

    def chunk(typ, data):
        c = struct.pack(">I", len(data)) + typ + data
        return c + struct.pack(">I", zlib.crc32(typ + data) & 0xFFFFFFFF)

    ihdr = struct.pack(">IIBBBBB", size, size, 8, 2, 0, 0, 0)
    png = (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr)
           + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b""))
    with open(path, "wb") as f:
        f.write(png)
    print(f"wrote {path} ({size}x{size})")


make_icon(180, "icon-180.png")
make_icon(512, "icon-512.png")
