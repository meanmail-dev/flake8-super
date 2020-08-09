from _ast import Call
from typing import Any

from flake8_plugin_utils import Error, Plugin, Visitor


class SuperPluginError(Error):
    code = 'SPR100'
    message = 'Use `super()` instead of `super(__class__, self)`'


class SuperPluginVisitor(Visitor):
    def visit_Call(self, node: Call) -> Any:
        func = node.func
        value = getattr(func, 'value', None)

        if value and value.func.id == 'super' and value.args:
            self.error_from_node(SuperPluginError, node)


class SuperPlugin(Plugin):
    name = 'SuperPlugin'
    version = '0.1.0'
    visitors = [SuperPluginVisitor]
