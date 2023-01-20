#!/usr/bin/env python3

#
# This is a sample to use taskflow internal listener
#
# Output:
#
# 'Linear Flow' flow started.
# '__main__.TaskOne' task started.
# Task One - Executed
# It took task '__main__.TaskOne' 0.00 seconds to finish.
# '__main__.TaskTwo' task started.
# Task Two - Executed
# It took task '__main__.TaskTwo' 0.00 seconds to finish.
# It took flow 'Linear Flow' 0.00 seconds to finish.
#

from taskflow import engines
from taskflow.patterns import linear_flow
from taskflow.task import Task
from taskflow.listeners import timing


class TaskOne(Task):
    def execute(self, **kwargs):
        print("Task One - Executed")

class TaskTwo(Task):
    def execute(self, **kwargs):
        print("Task Two - Executed")

flow = linear_flow.Flow("Linear Flow").add(
    TaskOne(),
    TaskTwo()
)

engine = engines.load(flow)
timer = timing.PrintingDurationListener(engine=engine)
timer.register()
engine.run()
