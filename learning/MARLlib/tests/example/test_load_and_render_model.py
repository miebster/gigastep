# MIT License

# Copyright (c) 2023 Replicable-MARL

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from marllib import marl
import unittest

class TestPolicyRendering(unittest.TestCase):

    def test_policy_rendering(self):
        # prepare the environment
        env = marl.make_env(environment_name="mpe", map_name="simple_spread", force_coop=True)

        # initialize algorithm and load hyperparameters
        mappo = marl.algos.mappo(hyperparam_source="test")

        # build agent model based on env + algorithms + user preference if checked available
        model = marl.build_model(env, mappo, {"core_arch": "gru", "encode_layer": "128-256"})

        # rendering
        mappo.render(env, model,
                     restore_path={'params_path': "../../examples/checkpoint_000010/params.json",
                                   'model_path': "../../examples/checkpoint_000010/checkpoint-10"},
                     local_mode=True,
                     share_policy="all",
                     checkpoint_end=False)
