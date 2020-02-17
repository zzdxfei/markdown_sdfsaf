import pynvim
import numpy as np


def AddSdfsaf(lines):
    states = np.zeros((10, ), dtype=np.int32)
    new_lines = []
    for line in lines:
        if len(line) == 0 or line[0] != "#":
            new_lines.append(line)
            continue
        label = len(line.split(" ")[0])
        states[label - 1] += 1
        states[label:] = 0
        sdfsaf = states[:label]
        sdfsaf = [str(s) for s in sdfsaf]
        sdfsaf = '.'.join(sdfsaf)
        new_line = " ".join(['#' * label, sdfsaf, line[label+1:]])
        new_lines.append(new_line)
    return new_lines


@pynvim.plugin
class MARKDOWN_SDFSAF(object):
    def __init__(self, vim):
        self.vim = vim

    @pynvim.command('Mdsdfsaf', range='', nargs='*', sync=True)
    def command_handler(self, args, range):
        self.vim.current.buffer[:] = AddSdfsaf(self.vim.current.buffer[:])

    """
    @pynvim.autocmd('BufEnter', pattern='*.py', eval='expand("<afile>")',
                    sync=True)
    def autocmd_handler(self, filename):
        self._increment_calls()
        self.vim.current.line = (
            'Autocmd: Called %s times, file: %s' % (self.calls, filename))
    """
