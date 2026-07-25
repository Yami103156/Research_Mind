from agents.reader import build_reader_agent

agent = build_reader_agent()

response = agent.invoke(

    {

        "messages":[

            (

                "user",

                "Read this webpage and summarize it.\n\nhttps://en.wikipedia.org/wiki/Large_language_model"

            )

        ]

    }

)

print(

    response["messages"][-1].content

)