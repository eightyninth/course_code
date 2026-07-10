# 基础镜像（来自 node:22.22.2-slim，其内部包含 debian、yarn 等）
FROM node:22.22.2-slim

# 安装 pnpm 和 inkos（全局安装）
RUN npm install -g pnpm@10.33.0 && npm install -g @actalk/inkos

WORKDIR /novels
RUN if [ -d "novels" ]; then rm -rf novels; fi \
    && (inkos init novels || mkdir -p novels) \
    && cd novels \
    && echo '{ \
                "name": "novels",  \
                "version": "0.1.0""language": "zh", \
                "llm": { \
                    "provider": "openai", \
                    "service": "custom", \
                    "configSource": "studio", \
                    "baseUrl": "", \
                    "model": "", \
                    "apiFormat": "chat", \
                    "stream": true \
                }, \
                "notify": [], \
                "inputGovernanceMode": "v2", \
                "daemon": { \
                    "schedule": { \
                        "radarCron": "0 */6 * * *", \
                        "writeCron": "*/15 * * * *" \
                    }, \
                    "maxConcurrentBooks": 3 \
                }, \
                "modelOverrides": { \
                    "writer": { \
                          "model": "qwen2.5:7b", \
                          "baseUrl": "http://0.0.0.0:11434", \
                          "provider": "custom", \
                          "apiKeyEnv": "PACKY_API_KEY" \
                    }, \
                    "auditor": { \
                      "model": "deepseek-r1", \
                      "provider": "custom" \
                    } \
                } \
    }' > inkos.json

# 设置启动命令
ENTRYPOINT ["inkos"]

# docker run -d -p 7000:4567 -v /data/docker/inkos:/inkos --name inkos --restart always eightyninth/inkos:latest
