from .base_executor import CompiledExecutor


class Executor(CompiledExecutor):
    ext = '.rs'
    name = 'RUST'
    command = 'rustc'
    test_program = 'fn main() { println!("echo: Hello, World!"); }'

    def get_compile_args(self):
        return [self.get_command(), '-O', self._code]
