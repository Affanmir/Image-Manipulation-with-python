import PIL
from PIL import Image
import array as arr
import numpy as numpy


class MyListIterator:

    ''' Iterator class to make MyList iterable.
    https://thispointer.com/python-how-to-make-a-class-iterable-create-iterator-class-for-it/

    '''

    def __init__(self, lst):

        # MyList object reference
        self._lst: MyList = lst

        # member variable to keep track of current index
        self._index: int = 0

    def __next__(self):
        ''''Returns the next value from the stored MyList instance.'''

        if self._index < len(self._lst):
            value = self._lst[self._index]
            self._index += 1
            return value

        raise StopIteration


class Node:

    def __init__(self, data) -> None:

        self.data = data
        self.left = self.right = None


class MyList:

    def __init__(self, size: int, value=None) -> None:
        """Creates a list of the given size, optionally intializing elements to value.
        The list is static. It only has space for size elements.

        Args:
        - size: size of the list; space is reserved for these many elements. 
        - value: the optional initial value of the created elements.

        Returns:
        none
        """

        self.size = size
        pass

    def __len__(self) -> int:
        '''Returns the size of the list. Allows len() to be called on it.
        Ref: https://stackoverflow.com/q/7642434/1382487

        Args:

        Returns:
        the size of the list.
        '''

        pass

    def __getitem__(self, i: int):
        '''Returns the value at index, i. Allows indexing syntax.
        Ref: https://stackoverflow.com/a/33882066/1382487

        Args:
        - i: the index from which to retrieve the value.

        Returns:
        the value at index i.
        '''

        # Ensure bounds.

        assert 0 <= i < len(self),\
            f'Getting invalid list index {i} from list of size {len(self)}'
        pass

    def __setitem__(self, i: int, value) -> None:
        '''Sets the element at index, i, to value. Allows indexing syntax.
        Ref: https://stackoverflow.com/a/33882066/1382487

        Args:

        - i: the index of the elemnent to be set
        - value: the value to be set

        Returns:
        none
        '''

        # Ensure bounds.

        assert 0 <= i < len(self),\
            f'Setting invalid list index {i} in list of size {self.size()}'
        pass

    def __iter__(self) -> MyListIterator:
        '''Returns an iterator that allows iteration over this list.
        Ref: https://thispointer.com/python-how-to-make-a-class-iterable-create-iterator-class-for-it/
        Args:
        Returns:
        an iterator that allows iteration over this list.
        '''
        return MyListIterator(self)

    def get(self, i: int):
        '''Returns the value at index, i.
        Alternate to use of indexing syntax.

        Args:
        - i: the index from which to retrieve the value.

        Returns:
        the value at index i.
        '''

        return self[i]

    def set(self, i: int, value) -> None:
        '''Sets the element at index, i, to value.
        Alternate to use of indexing syntax. 

        Args:
        - i: the index of the elemnent to be set
        - value: the value to be set

        Returns:
        none
        '''

        self[i] = value


class ArrayList:

    def __init__(self, size: int, value=None) -> None:

        if not value:
            value = (0, 0, 0)
        self.size = size
        self.R_array = arr.array('B', [value[0]]*size)
        self.G_array = arr.array('B', [value[1]]*size)
        self.B_array = arr.array('B', [value[2]]*size)

    def __len__(self) -> int:

        return self.size

    def __getitem__(self, i: int):
        '''Returns the value at index, i. Allows indexing syntax.

        Ref: https://stackoverflow.com/a/33882066/1382487

        Args:
        - i: the index from which to retrieve the value. 

        Returns:
        the value at index i.
        '''

        # Ensure bounds.

        assert 0 <= i < len(self),\
            f'Getting invalid list index {i} from list of size {len(self)}'
        return (self.R_array[i], self.G_array[i], self.B_array[i])

    def __setitem__(self, i: int, value) -> None:
        '''Sets the element at index, i, to value. Allows indexing syntax.
        Ref: https://stackoverflow.com/a/33882066/1382487

        Args:

        - i: the index of the elemnent to be set

        - value: the value to be set '''

        self.R_array[i] = value[0]
        self.G_array[i] = value[1]
        self.B_array[i] = value[2]

    def __iter__(self) -> MyListIterator:
        '''Returns an iterator that allows iteration over this list.
        Ref: https: // thispointer.com/python-how-to-make-a-class-iterable-create-iterator-class-for-it/

        Args:

        Returns:
        an iterator that allows iteration over this list.

        '''

        return MyListIterator(self)

    def get(self, i: int):
        '''Returns the value at index, i.
        Alternate to use of indexing syntax.

        Args:

        - i: the index from which to retrieve the value.
        Returns:

        the value at index i.
        '''

        return self[i]

    def set(self, i: int, value) -> None:

        self[i] = value


class PointerList(MyList):

    def __init__(self, size: int, value=None) -> None:
        """Creates a list of the given size, optionally intializing elements to value.
        The list is static. It only has space for size elements.

        Args:
        - size: size of the list; space is reserved for these many elements. 
        - value: the optional initial value of the created elements.

        Returns:
        none
        """

        self.head = Node(value)
        self.size = size
        current = self.head

        while (size > 0):

            right = Node(value)
            current.right = right
            current = current.right
            size = size-1

        self.value = value

    def __len__(self) -> int:
        '''Returns the size of the list. Allows len() to be called on it.
        Ref: https://stackoverflow.com/q/7642434/1382487
        Args:

        Returns:
        the size of the list.
        '''

        return self.size

    def __getitem__(self, i: int):
        '''Returns the value at index, i. Allows indexing syntax.
        Ref: https://stackoverflow.com/a/33882066/1382487

        Args:
        - i: the index from which to retrieve the value.

        Returns:
        the value at index i.
        '''

        assert 0 <= i < len(self),\
            f'Getting invalid list index {i} from list of size {len(self)}'
        u = self.head
        for j in range(i):
            u = u.right
        return u.data

    def __setitem__(self, i: int, value) -> None:
        '''Sets the element at index, i, to value. Allows indexing syntax.
        Ref: https://stackoverflow.com/a/33882066/1382487

        Args:
        - i: the index of the elemnent to be set
        - value: the value to be set

        Returns:
        none
        '''

        assert 0 <= i < len(self),\
            f'Setting invalid list index {i} in list of size {self.size()}'
        if(self.head.data != None):

            current = self.head

            while(i > 0):

                current = current.right
                i = i-1
            current.data = value

        else:

            self.head.data = value

      

    def __iter__(self) -> MyListIterator:
        '''Returns an iterator that allows iteration over this list.
        Ref: https://thispointer.com/python-how-to-make-a-class-iterable-create-iterator-class-for-it/

        Args:

        Returns:
        an iterator that allows iteration over this list.
        '''

        return MyListIterator(self)

    def get(self, i: int):
        '''Returns the value at index, i.
        Alternate to use of indexing syntax.

        Args:
        - i: the index from which to retrieve the value.

        Returns:
        the value at index i.
        '''

        return self[i]

    def set(self, i: int, value) -> None:
        '''Sets the element at index, i, to value.
        Alternate to use of indexing syntax.

        Args:
        - i: the index of the elemnent to be set
        - value: the value to be set

        Returns:
        none
        '''

        self[i] = value


class MyImage:

    def __init__(self, size: (int, int), pointer=False) -> None:

        width, height = self.size = size
        self.pointer = pointer
        if pointer:

            self.pixels: PointerList = PointerList(
                width * height, value=(0, 0, 0))

        else:

            self.pixels: ArrayList = ArrayList(width * height, value=(0, 0, 0))

    def _get_index(self, r: int, c: int) -> int:
        """Returns the list index for the given row, column coordinates.
        This is an internal function for use in class methods only. It should
        not be used or called from outside the class.

        Args:
        - r: the row coordinate
        - c: the column coordinate

        Returns:
        the list index corresponding to the given row and column coordinates
        """

        # Confirm bounds, compute and return list index.

        width, height = self.size
        assert 0 <= r < height and 0 <= c < width, "Bad image coordinates: "\
            f"(r, c): ({r}, {c}) for image of size: {self.size}"
        return r*width + c

    def open(path: str, pointer=False):
        """Creates and returns an image containing from the information at file path.
        The image format is inferred from the file name. The read image is
        converted to RGB as our type only stores RGB.

        Args:
        - path: path to the file containing image information

        Returns:
        the image created using the information from file path.
        """

        # Use PIL to read the image information and store it in our instance.

        img: PIL.Image = Image.open(path)

        myimg: MyImage = MyImage(img.size, pointer)

        width, height = img.size

        # Covert image to RGB. https://stackoverflow.com/a/11064935/1382487

        img: PIL.Image = img.convert('RGB')

        # Get list of pixel values (https://stackoverflow.com/a/1109747/1382487),

        # copy to our instance and return it.

        for i, rgb in enumerate(list(img.getdata())):

            myimg.pixels.set(i, rgb)

        return myimg

    def save(self, path: str) -> None:
        """Saves the image to the given file path.
        The image format is inferred from the file name.

        Args:
        - path: the image has to be saved here.

        Returns:
        none
        """

        # Use PIL to write the image.

        img: PIL.Image = Image.new("RGB", self.size)

        img.putdata([rgb for rgb in self.pixels])

        img.save(path)

    def get(self, r: int, c: int) -> (int, int, int):
        """Returns the value of the pixel at the given row and column coordinates.

        Args:
        - r: the row coordinate
        - c: the column coordinate

        Returns:
        the stored RGB value of the pixel at the given row and column coordinates.
        """

        return self.pixels[self._get_index(r, c)]

    def set(self, r: int, c: int, rgb: (int, int, int)) -> None:
        """Write the rgb value at the pixel at the given row and column coordinates.

        Args:
        - r: the row coordinate
        - c: the column coordinate
        - rgb: the rgb value to write

        Returns:
        none
        """

        self.pixels[self._get_index(r, c)] = rgb

    def show(self) -> None:
        """Display the image in a GUI window.

        Args:

        Returns:
        none
        """

        # Use PIL to display the image.

        img: PIL.Image = Image.new("RGB", self.size)

        img.putdata([rgb for rgb in self.pixels])

        img.show()


def remove_channel(src: MyImage, red: bool = False, green: bool = False, blue: bool = False) -> MyImage:
    """Returns a copy of src in which the indicated channels are suppressed.
    Suppresses the red channel if no channel is indicated. src is not modified.

    Args:
    - src: the image whose copy the indicated channels have to be suppressed.
    - red: suppress the red channel if this is True.
    - green: suppress the green channel if this is True.
    - blue: suppress the blue channel if this is True.

    Returns:
    a copy of src with the indicated channels suppressed.
    """

    x, y = src.size

    copy = MyImage((x, y), src.pointer)

    for i in range(x):
        for j in range(y):  # iterating over every pixel, and setting the bool values to zero

            pix = src.get(j, i)
            r, g, b = pix

            if red:
                r = 0

            if blue:
                b = 0

            if green:
                g = 0
            if not green and not blue and not red:
                r = 0
            pix = (r, g, b)
            copy.set(j, i, pix)

    return copy


def horizontal_vertical(src: MyImage) -> MyImage:
    x, y = src.size
    copy = MyImage((x, y), src.pointer)
    for i in range(x):
        for j in range(y):
            pixel = src.get(j, i)
            row = y//j
            column = i % x
            copy.set(row, column, pixel)
    return copy


def rotations(src: MyImage) -> MyImage:
    """Returns an image containing the 4 rotations of src.
    The new image has twice the dimensions of src. src is not modified.

    Args:
    - src: the image whose rotations have to be stored and returned.

    Returns:
    an image twice the size of src and containing the 4 rotations of src.
    """
    # we rotate the image then we set it to specific areas by adding the width to the colum
    # and height to the row

    x, y = src.size

    # we make a copy which is twice the size of the original
    copy = MyImage((x*2, y*2), src.pointer)

    for i in range(x):
        for j in range(y):

            pixel = src.get(j, i)
            row = j
            colum = i
            copy.set(row, colum+y, pixel)

    for i in range(x):
        for j in range(y):

            pixel = src.get(j, i)
            row = j
            colum = y - i-1
            copy.set(colum, row, pixel)

    for i in range(x):
        for j in range(y):

            pixel = src.get(j, i)
            row = x-j
            colum = y-i
            copy.set(row+x-1, colum-1, pixel)

    for i in range(x):
        for j in range(y):

            pixel = src.get(j, i)
            row = x-j
            colum = i
            copy.set(colum+x, row+x-1, pixel)

    return copy


def apply_mask(src: MyImage, maskfile: str, average: bool = True) -> MyImage:
    """Returns an copy of src with the mask from maskfile applied to it.
    maskfile specifies a text file which contains an n by n mask. It has the

    following format:
    - the first line contains n
    - the next n^2 lines contain 1 element each of the flattened mask

    Args:
    - src: the image on which the mask is to be applied
    - maskfile: path to a file specifying the mask to be applied
    - average: if True, averaging should to be done when applying the mask

    Returns:
    an image which the result of applying the specified mask to src.
    """

    file_object = open(maskfile, 'r')
    n = file_object.readline()
    n = int(n)

    lszz = []
    for i in range(n**2):

        line = file_object.readline()
        lszz.append(int(line))

    mask = numpy.reshape(lszz, (n, n))  # created a 2d list mask using numpy

    numpy.shape(mask)

    x, y = src.size

    copy = MyImage(src.size, src.pointer)

    for i in range(x):  # iterating over every pixel
        for j in range(y):

            endsum = 0
            Weight = 0

            for maski in range(n):  # for every pixel we iterate over the mask
                for maskj in range(n):

                    XX = maski+i
                    YY = maskj+j

                    # bounding the pixels to be considered (edge cases)
                    if (-maski+i) >= 0 and (maski+i) < x and (maskj+j) < y and(-maskj+j) >= 0:

                        Weight = Weight+mask[maski][maskj]
                        r, g, b = src.get(YY, XX)
                        avg = ((r+g+b)//3)
                        endsum = endsum+avg*(mask[maski][maskj])

            if average:  # If average required we divide with the weight else we dont
                if Weight != 0:
                    endsum = (endsum//Weight)

            endsum = min(max(0, endsum), 255)
            copy.set(j, i, (endsum, endsum, endsum))

    return copy



