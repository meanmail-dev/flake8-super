from _ast import Call, Name
from typing import Any

from flake8_plugin_utils import Error, Plugin, Visitor


class SuperPluginError(Error):
    code = 'SPR100'
    message = 'Use `super()` instead of `super(__class__, self)`'


class SuperPluginVisitor(Visitor):
    def visit_Call(self, node: Call) -> Any:
        if (isinstance(node.func, Name) and
            node.func.id == 'super' and
            node.args):
            self.error_from_node(SuperPluginError, node)

        return self.generic_visit(node)


class SuperPlugin(Plugin):
    name = 'SuperPlugin'
    version = '0.1.2'
    visitors = [SuperPluginVisitor]
