from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",   # model_id, not repo_id
    task="text-generation",
    pipeline_kwargs=dict(
        do_sample=True,
        temperature=0.3,
        max_new_tokens=100,
    ),
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("one line story")
print(result.content)