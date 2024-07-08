import autogen
import environ

env = environ.Env()
environ.Env.read_env()


def main():
    config_list = [
        {
            "model": "gpt-3.5-turbo",
            "api_key": env("OPENAI_API_KEY"),
        },
        {
            "model":"llama3-8b-8192",
            "api_key": env("GROQ_API_KEY"),
            "api_type": "groq",
        }
    ]

    assistant = autogen.AssistantAgent(
        name="Wikipedia Assistant",
        llm_config={
            "config_list": config_list,
        },
        system_message="Help the user from the content about Bangladesh from this wikipedia page https://en.wikipedia.org/wiki/Bangladesh",
    )

    user_proxy = autogen.UserProxyAgent(
        name="User",
        human_input_mode="ALWAYS",
    )

    user_proxy.initiate_chat(assistant, message="Can you help me with some questions about Bangladesh?")


if __name__ == "__main__":
    main()
