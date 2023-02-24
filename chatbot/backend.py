import openai


class ChatBot:
	def __init__(self):
		openai.api_key = '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'

	def get_response(self, user_input):
		response = openai.Completion.create(
			engine='text-davinci-003',
			prompt=user_input,
			max_tokens=3000,
			temperature=0.5,
		).choices[0].text

		# get the response from the AI
		return response


def main():
	chatbot = ChatBot()
	response = chatbot.get_response('Tell me a joke about Llamas?')
	print(response)


if __name__ == '__main__':
	main()
