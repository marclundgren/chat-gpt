# Chat GPT

## Setup

### Add [your openai api key](https://beta.openai.com/account/api-keys) to `key.txt`

```sh
# note it's possible that this will result in a newline character. If so, delete it
echo "YOUR KEY" > key.txt
```

### Install Python 3.9

```sh
sudo apt install python3-pip # ubuntu/wsl
# or
brew install pyenv && pyenv install 3 # mac
```

### Install project dependencies

```sh
pip3 install requests numpy tqdm openai
```

## Running with a command line prompt

```sh
python3 app.py hello there
```

## Running without a command line prompt

```sh
# update the fallback_prompt variable in app.py
python3 app.py
```

## Model Family

|  Model  |  Technical Name  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| :-----: | :--------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   Ada   |   text-ada-001   | Ada is the fastest model. It performs well at tasks where creativity is more important than precision. It is suitable for applications such as chatbots, parsing text, simple classification, keywords, and address correction. Ada has the lowest costs.                                                                                                                                                                                                                   |
| Babbage | text-babbage-001 | Babbage excels at identifying salient patterns in text and utilizing them as a reference to generate new text. Additionally, it can effectively perform general classification tasks, such as categorizing industries, genres, and media content. However, Babbage is not as adept at creative tasks as other models. It can understand sufficient structure to generate simple plots and titles, but it may not be the best choice for more complex creative applications. |
|  Curie  |  text-curie-001  | Curie is capable of many nuanced tasks like sentiment classification and summarization. It reaches almost the level of Davinci but has lower costs. It is also good at answering questions, performing Q&A, and as a general service chatbot.                                                                                                                                                                                                                               |
| Davinci | text-davinci-003 | Davinci, in its current version 003, corresponds to ChatGPT (GPT3.5). It is a versatile model that can perform a wide range of tasks, often with fewer specific instructions. It excels in tasks that require a deep understanding of content, such as summary generation and creative writing. However, it requires more computational resources and may not be as fast or cost-effective as other models.                                                                 |

### Note

By default, use `text-davinci-002`. I tried to generate this model family table in markdown with `text-davinci-003` but it resulted in odd results.
