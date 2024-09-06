# NetGent

![NetGent Logo](/assets/netgent_banner.png)

NetGent (Network Agent) is a powerful, functional API for designing multi-agent graph systems. Inspired by the functional APIs of LangGraph/LangChain and Keras/PyTorch, NetGent simplifies the creation of complex AI ecosystems.

## 📐 Design Architectures

### Sequential Processing
The sequential processing workflow chains multiple agents for step-by-step processing, where each agent's output becomes the input for the next agent.

### Parallel Processing
The parallel processing workflow executes multiple agents concurrently, where each agent processes the initial state independently.

### Aggregated Parallel Processing
The parallel processing workflow executes multiple agents concurrently, where each agent processes the initial state independently.

## 🌟 Features

- **Simplified Multi-Agent Systems**: Create and manage multi-agent systems with ease.
- **Seamless Integration**: Combine generative AI (LLMs, VLMs, Audio models) with traditional neural networks.
- **Flexible Architecture**: Design your AI workflow using simple, intuitive building blocks.
- **Unified Interface**: Standardized `invoke(state: State) -> State` interface for all AI components.
- **Prompt Engineering Made Easy**: Implement advanced prompt techniques without complexity.

## 🚀 Quick Start
```python
from netgent import llm, response_average, sequential, parallel

# Simple invocation
result_state = llm(state)

# Average multiple responses
result_state = response_average(llm, evaluator=llm, state, k=5)

# Sequential processing
result_state = sequential(sequence=[llm_1, llm_2, llm_3], state)

# Parallel processing
result_state = parallel(agents=[llm_1, llm_2], state)
final_state = wrap_states(result_state)
```

## 🛠 Installation

```bash
pip install netgent
```

## 🗺 Roadmap

1. Develop NetGent Core functionality (v1.0.0)
   - Implement various prompt types
   - Enable different calling patterns (sequential, parallel, skip connections)
   - Ensure robust support for complex multi-agent LLM architectures (text-based)

2. Expand multi-agent capabilities with multimodality (v2.0.0)
   - Add vision agents
   - Integrate speech-to-text agents
   - Enhance multi-agent architectures with multimodal support

Note: All agents will adhere to the NetGent philosophy, maintaining a consistent `invoke(state) -> state` interface.

## 💡 Philosophy

NetGent's core philosophy is "Treat everything as an agent." By standardizing the interface for all AI components, NetGent enables developers to create truly AI-driven software with unprecedented ease and flexibility.

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for more details.

## 📄 License

NetGent is released under the [MIT License](LICENSE).

## 🌐 Learn More

For detailed documentation, tutorials, and examples, visit our [official documentation](https://netgent.readthedocs.io).

---

NetGent: Empowering developers to create the next generation of AI ecosystems.
