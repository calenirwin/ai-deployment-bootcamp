FROM gcr.io/deeplearning-platform-release/tf2-gpu.2-8

# Copies the trainer code to the docker image.
COPY trainer /trainer

WORKDIR /trainer

# Sets up the entry point to invoke the trainer.
ENTRYPOINT ["python", "-m", "task.py"]