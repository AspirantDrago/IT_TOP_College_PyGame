import os
import sys

import pygame as pg


def load_image(image_path: str, color_key=None) -> pg.Surface:
    """
    Функция, открывающая картинку по имени, расположенную в каталоге `/data/img`
     - `colorkey == None` - используем исходный альфа-канал
     - `colorkey as pygame.Color` - используем выбранный хромакей
     - `colorkey == -1` - используем в качестве хромакея цвет пикселя в левом верхнем углу

    :param image_path:  имя файла
    :param colorkey:    хромокей
    :return:            слой с изображением
    """
    fullname = os.path.join('data', 'img', image_path)
    if not os.path.isfile(fullname):
        print(f'Файл с изображением {fullname} не найден!', file=sys.stderr)
        sys.exit(404)
    image = pg.image.load(fullname)
    if color_key is not None:
        image = image.convert()
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


def load_many_images(
            image_path: str,
            count_rows: int = 1,
            count_columns: int = 1,
            color_key=None,
            size: tuple[int, int] | None = None,
        ) -> list[pg.Surface]:
    result = []
    orig_image = load_image(image_path, color_key)
    if size:
        orig_image = pg.transform.smoothscale(orig_image, (size[0] * count_columns, size[1] * count_rows))
    width = orig_image.get_width() // count_columns
    height = orig_image.get_height() // count_rows

    rect = pg.Rect(0, 0, width * 0.95, height * 0.95)
    for row in range(count_rows):
        for column in range(count_columns):
            sub_image = orig_image.subsurface(rect.move((column + 0.025) * width, (row + 0.025) * height))
            sub_image.set_colorkey(sub_image.get_at((0, 0)))

            result.append(sub_image)
    return result
