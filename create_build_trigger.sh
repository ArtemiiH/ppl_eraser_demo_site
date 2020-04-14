#!/bin/bash
gcloud beta builds triggers create cloud-source-repositories \
    --repo=ppl-eraser-demo-site \
    --branch-pattern=".*" \
    --build-config=cloudbuild.yaml
