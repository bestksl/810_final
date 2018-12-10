# @Author: HaoxuanLi
# @Date 2018/11/4
# CWID: 10434197


class FileReader:
    @staticmethod
    def read_lines(path: str, flag: str, header=False):
        lines = []
        header_list = None
        try:
            file = open(path)
        except FileNotFoundError:
            raise FileNotFoundError(f'warning: file({path}) not found')
        with file:
            for line in file:
                if header:
                    header_list = line.split(flag)
                    header = False
                    continue
                attr = line.strip().split(flag)
                if len(attr) != 0 or attr is not None:
                    lines.append(attr)
                else:
                    break
        if header_list:
            return header_list, lines
        return lines
