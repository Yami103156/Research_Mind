from agents.search import build_search_agent

agent = build_search_agent()

response = agent.invoke(

    {

        "messages":[

            (

                "user",

                "Find latest breakthroughs in Quantum Computing."

            )

        ]

    }

)

print(

    response["messages"][-1].content

)