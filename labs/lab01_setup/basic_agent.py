from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
import asyncio

class HelloAgent(Agent):
    class HelloBehaviour(CyclicBehaviour):
        async def run(self):
            print(f"[{self.agent.jid}] Agent is running.")
            await asyncio.sleep(5)

    async def setup(self):
        print("HelloAgent started.")
        self.add_behaviour(self.HelloBehaviour())

if __name__ == "__main__":
    agent = HelloAgent("agent1@localhost", "password")
    agent.start()
    input("Press ENTER to stop agent\n")
    agent.stop()