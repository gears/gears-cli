import os
import shlex
from gears_cli.__main__ import get_command
from mock import patch
from unittest2 import TestCase


class CompileCommandTests(TestCase):

    def setUp(self):
        self.save_patch = patch('gears.environment.Environment.save')
        self.save_mock = self.save_patch.start()

    def tearDown(self):
        self.save_patch.stop()

    def assertPathsEqual(self, first, second, msg=None):
        first = os.path.relpath(first)
        second = os.path.relpath(second)
        self.assertEqual(first, second, msg=msg)

    def get_command(self, args):
        return get_command(shlex.split(args))

    def test_it_compiles_assets_to_output_directory(self):
        command = self.get_command('compile assets static')
        self.assertPathsEqual(command.environment.root, 'static')

    def test_it_finds_assets_in_source_directory(self):
        command = self.get_command('compile assets static')
        self.assertEqual(len(command.environment.finders), 1)
        self.assertEqual(len(command.environment.finders[0].locations), 1)
        self.assertPathsEqual(command.environment.finders[0].locations[0], 'assets')
