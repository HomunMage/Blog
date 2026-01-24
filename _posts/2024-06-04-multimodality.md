---

title:  "Native Multimodality"
date:   2024-06-04 10:00:00 +0800
tags: [Multi]
---


Last year, AI models were often specialized for single tasks, requiring collaboration between multiple systems to achieve multimodal outputs. For example, to generate an image from an audio prompt, one needed to use Whisper AI to convert audio to text, GPT-4 to process the text, and DALL·E 3 to generate the image. This year, native multimodal AI models have emerged, such as OpenAI's GPT-4o, which can directly generate an image from spoken input. These models not only streamline the process but also significantly outperform their single-task predecessors.

<script src="https://unpkg.com/mermaid@10.4.0/dist/mermaid.min.js"></script>

<div class="mermaid">
%% Code for flowchart below
graph TD
  subgraph GPT4
    audio[Speak<br>“draw me image”]
    whisper((Whisper))
    gpt((GPT4))
    dalle((DALL·E 3))

    audio ==> whisper
    whisper -- text --> gpt
    gpt -- text --> dalle
    dalle ==> Image

    end
  
  subgraph gpt-4o
    audio2[Speak<br>“draw me image”]
    gpt4o((GPT-4o))
    image[Image]


    audio2 ==> gpt4o
    gpt4o ==> image

    end
</div>

## Meta's Chameleon
  * Chameleon is a state-of-the-art multimodal AI model developed by Meta (Facebook).
  * It uses an "early-fusion token-based mixed-modal" architecture, which integrates different modalities like text, images, and code from the ground up.
  * Chameleon achieves strong performance on multimodal tasks like image captioning and visual question answering, while also remaining competitive on text-only benchmarks.
  * It was trained on a massive 4.4 trillion token dataset using Nvidia A100 GPUs for over 5 million hours.
  * Chameleon represents a significant advancement in multimodal AI, potentially enabling more unified and flexible AI systems.

## OpenAI's GPT-4o
  * GPT-4o is OpenAI's latest flagship multimodal model, capable of processing and generating text, audio, images, and video.
  * It can respond to audio inputs in under 320ms on average, similar to human response times in conversations.
  * GPT-4o matches the text and coding performance of GPT-4 Turbo, while significantly improving on multilingual, audio, and vision capabilities.
  * It sets new high scores on benchmarks like 0-shot and 5-shot MMLU (Multimodal Language Understanding).
  * GPT-4o is 2x faster, 50% cheaper, and has 5x higher rate limits compared to GPT-4 Turbo in the API.

## Google's Gemini
  * Gemini is Google's suite of next-generation multimodal AI models and applications.
  * It consists of three variants: Gemini Ultra (highest-performing), Gemini Pro (lighter version), and Gemini Nano (compact mobile model).
  * Gemini models are natively multimodal, capable of processing and understanding text, images, audio, video, and code.
  * They achieve state-of-the-art performance on tasks like speech recognition, video question answering, and long-context retrieval.
  * Gemini models have a default context window of up to 1 million tokens, the longest of any large-scale foundation model.
  * Google is integrating Gemini models into various Google products and services, aiming to bring advanced multimodal AI capabilities to billions of users.

## summary
In summary, all three models - Chameleon, GPT-4o, and Gemini - represent significant advancements in the field of multimodal AI, with unique architectural approaches and capabilities. They showcase the rapid progress being made in developing AI systems that can seamlessly integrate and reason across multiple modalities. 




