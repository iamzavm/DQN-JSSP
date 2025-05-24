import pytest
from env.job_shop_env import JobShopEnv

def test_step_invalid_action_raises():
    env = JobShopEnv(instance="toy")
    with pytest.raises(ValueError):
        env.step(action=env.action_space.n)  # out of bounds