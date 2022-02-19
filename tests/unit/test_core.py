from pvc.test_utils import flow1


class TestTask:
    def setup(self):
        pass

    def test_task_add(self):
        f = flow1()
        assert f
