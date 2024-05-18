import math
"""
Line 클래스와 이를 입력으로 받아 area_square, area_circle, area_regular_triangle을 계산하는 함수가 정의된 모듈
"""


class Line():
    """
    Line 클래스는 외부에서 접근 불가능한 필드 __length를 가지며 기본값은 1이다.
    생성자를 통해 초기값을 설정할 수 있다.
    해당 필드에 접근하기 위한 메소드 set_length, get_length를 가진다.
    """

    def __init__(self, length = 1):
        """ 생성자. 
        Args:
            length: 선의 길이(기본1). int나 float형이어야 하며 0보다 커야한다.
        Returns:

        Examples:
            >>> line = Line(10)
        """
        if type(length) in [int, float] and length > 0:
            self.__length = length
        else:
            self.__length = 1
        
    def set_length(self, length):
        """ 
        Args:
            length: 선의 길이. int나 float형이어야 하며 0보다 커야한다.
        Returns:

        Examples:
            >>> line.set_length(10)
        """
        if type(length) in [int, float] and length > 0:
            self.__length = length

    def get_length(self):
        """
        Args:

        Returns:
            __length: 선의 길이
        """
        return self.__length
    

def area_square(line):
    """인수로 받은 객체의 길이를 이용하여 정사각형의 넓이를 계산한다.
        인수로 받은 객체의 타입이 Line이 아닐경우 리턴값 0
    Parameters
    ----------
        line: Line타입의 객체
    Returns
    -------
        line.get_length()**2
    Examples
    --------
        >>> line = Line(10)
        >>> area_square(line) 
    """
    if isinstance(line, Line):
        return line.get_length() ** 2
    else:
        return 0
    
def area_circle(line):
    """인수로 받은 객체의 길이를 이용하여 원의 넓이를 계산한다.
        인수로 받은 객체의 타입이 Line이 아닐경우 리턴값 0
    Parameters
    ----------
        line: Line타입의 객체
    Returns
    -------
        math.pi * line.get_length() ** 2
    Examples
    --------
        >>> line = Line(10)
        >>> area_circle(line)
    """
    if isinstance(line, Line):
        return math.pi * line.get_length() ** 2
    else:
        return 0

def area_regular_triangle(line):
    """인수로 받은 객체의 길이를 이용하여 정삼각형의 넓이를 계산한다.
        인수로 받은 객체의 타입이 Line이 아닐경우 리턴값 0
    Parameters
    ----------
        line: Line타입의 객체
    Returns
    -------
        math.sqrt(3) / 4 * line.get_length() ** 2
    Examples
    --------
        >>> line = Line(10)
        >>> area_regular_triangle(line)
    """
    if isinstance(line, Line): 
        return math.sqrt(3) / 4 * line.get_length() ** 2
    else:
        return 0


