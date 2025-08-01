# Guía AWS AI/ML - LLMs, Bedrock y RAG

## 📋 Tabla de Contenidos
- [AWS Bedrock](#aws-bedrock)
- [Implementación RAG](#implementación-rag)
- [Lambda + EKS](#lambda--eks)
- [Bases Vectoriales](#bases-vectoriales)
- [Proyectos Prácticos](#proyectos-prácticos)
- [Recursos para CV](#recursos-para-cv)

---

## 🚀 AWS Bedrock

### ¿Qué es Bedrock?
AWS Bedrock es el servicio completamente gestionado de AWS para acceder a modelos de IA generativa de diferentes proveedores sin necesidad de gestionar infraestructura.

### Modelos Disponibles
- **Anthropic Claude** (Claude 3 Sonnet, Haiku, Opus)
- **Meta Llama 2/3** (7B, 13B, 70B)
- **Amazon Titan** (Text, Embeddings)
- **AI21 Labs Jurassic**
- **Cohere Command**
- **Stability AI** (Stable Diffusion)

### Características Clave
```python
# Ejemplo básico con Bedrock
import boto3
import json

bedrock = boto3.client('bedrock-runtime')

def invoke_claude(prompt):
    body = json.dumps({
        "prompt": f"\n\nHuman: {prompt}\n\nAssistant:",
        "max_tokens_to_sample": 1000,
        "temperature": 0.7
    })
    
    response = bedrock.invoke_model(
        modelId='anthropic.claude-3-sonnet-20240229-v1:0',
        body=body
    )
    
    return json.loads(response['body'].read())
```

### Ventajas
- Sin gestión de infraestructura
- Escalabilidad automática
- Seguridad y compliance integradas
- Integración nativa con otros servicios AWS
- Fine-tuning disponible para algunos modelos

---

## 🔍 Implementación RAG

### ¿Qué es RAG?
Retrieval-Augmented Generation combina recuperación de información con generación de texto para crear respuestas más precisas y contextuales.

### Arquitectura RAG Típica
```
Documentos → Chunking → Embeddings → Vector DB → Retrieval → LLM → Respuesta
```

### Componentes AWS para RAG

#### 1. Procesamiento de Documentos
```python
# Ejemplo con Lambda para procesar documentos
import json
import boto3
from langchain.text_splitter import RecursiveCharacterTextSplitter

def lambda_handler(event, context):
    # Procesar documento desde S3
    s3 = boto3.client('s3')
    bucket = event['bucket']
    key = event['key']
    
    # Descargar y procesar documento
    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body'].read().decode('utf-8')
    
    # Dividir en chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = text_splitter.split_text(content)
    
    # Generar embeddings con Bedrock
    bedrock = boto3.client('bedrock-runtime')
    
    for chunk in chunks:
        embedding = generate_embedding(bedrock, chunk)
        store_in_vector_db(chunk, embedding)
    
    return {'statusCode': 200, 'body': 'Procesado exitosamente'}
```

#### 2. Generación de Embeddings
```python
def generate_embedding(bedrock_client, text):
    body = json.dumps({
        "inputText": text
    })
    
    response = bedrock_client.invoke_model(
        modelId='amazon.titan-embed-text-v1',
        body=body
    )
    
    return json.loads(response['body'].read())['embedding']
```

#### 3. Búsqueda y Generación
```python
def rag_query(question, vector_db, bedrock_client):
    # 1. Generar embedding de la pregunta
    question_embedding = generate_embedding(bedrock_client, question)
    
    # 2. Buscar documentos similares
    similar_docs = vector_db.similarity_search(question_embedding, k=3)
    
    # 3. Crear contexto
    context = "\n".join([doc.content for doc in similar_docs])
    
    # 4. Generar respuesta con Claude
    prompt = f"""
    Contexto: {context}
    
    Pregunta: {question}
    
    Respuesta basada en el contexto:
    """
    
    return invoke_claude(prompt)
```

---

## ⚡ Lambda + EKS

### AWS Lambda para IA
Lambda es ideal para:
- APIs de inferencia ligeras
- Procesamiento de eventos
- Orchestración de pipelines ML
- Funciones de preprocesamiento

#### Ejemplo API Lambda
```python
import json
import boto3

def lambda_handler(event, context):
    # Configurar Bedrock
    bedrock = boto3.client('bedrock-runtime')
    
    # Extraer prompt del evento
    prompt = json.loads(event['body'])['prompt']
    
    # Llamar a Claude
    response = invoke_claude(prompt)
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(response)
    }
```

### EKS para Aplicaciones ML
EKS es mejor para:
- Modelos custom que requieren GPUs
- Aplicaciones ML complejas
- Entrenamiento distribuido
- Serving de modelos con alta demanda

#### Ejemplo Deployment EKS
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: llama-model-server
spec:
  replicas: 3
  selector:
    matchLabels:
      app: llama-server
  template:
    metadata:
      labels:
        app: llama-server
    spec:
      containers:
      - name: llama-container
        image: your-repo/llama-server:latest
        ports:
        - containerPort: 8080
        resources:
          requests:
            nvidia.com/gpu: 1
          limits:
            nvidia.com/gpu: 1
```

### Caching Strategies
```python
import redis
import json

# Configurar Redis para cache
redis_client = redis.Redis(host='elasticache-endpoint')

def cached_inference(prompt):
    # Check cache first
    cache_key = f"inference:{hash(prompt)}"
    cached_result = redis_client.get(cache_key)
    
    if cached_result:
        return json.loads(cached_result)
    
    # Si no está en cache, hacer inferencia
    result = invoke_claude(prompt)
    
    # Guardar en cache por 1 hora
    redis_client.setex(cache_key, 3600, json.dumps(result))
    
    return result
```

---

## 📊 Bases Vectoriales

### Amazon OpenSearch
```python
from opensearchpy import OpenSearch

def setup_opensearch():
    client = OpenSearch(
        hosts=[{'host': 'your-opensearch-endpoint', 'port': 443}],
        http_auth=('username', 'password'),
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection
    )
    return client

def store_embedding(client, doc_id, text, embedding):
    document = {
        'text': text,
        'embedding': embedding,
        'timestamp': datetime.now()
    }
    
    client.index(index='documents', id=doc_id, body=document)

def search_similar(client, query_embedding, k=5):
    search_body = {
        'query': {
            'knn': {
                'embedding': {
                    'vector': query_embedding,
                    'k': k
                }
            }
        }
    }
    
    response = client.search(index='documents', body=search_body)
    return response['hits']['hits']
```

### Pinecone (Alternativa)
```python
import pinecone

# Configurar Pinecone
pinecone.init(api_key="your-api-key", environment="your-env")

def create_index():
    pinecone.create_index(
        name="document-embeddings",
        dimension=1536,  # Dimensión de embeddings de Titan
        metric="cosine"
    )

def upsert_embeddings(index, vectors):
    index.upsert(vectors=vectors)

def query_similar(index, query_vector, top_k=5):
    return index.query(
        vector=query_vector,
        top_k=top_k,
        include_metadata=True
    )
```

---

## 🛠️ Proyectos Prácticos

### 1. Chatbot RAG con Bedrock
```python
# Arquitectura: S3 → Lambda → OpenSearch → Bedrock
class RAGChatbot:
    def __init__(self):
        self.bedrock = boto3.client('bedrock-runtime')
        self.opensearch = setup_opensearch()
    
    def process_documents(self, s3_bucket, s3_key):
        # Procesar documentos y crear embeddings
        pass
    
    def chat(self, question):
        # Buscar contexto relevante
        context = self.retrieve_context(question)
        
        # Generar respuesta
        response = self.generate_response(question, context)
        
        return response
```

### 2. Document Q&A System
```python
class DocumentQA:
    def __init__(self):
        self.setup_components()
    
    def upload_document(self, file_path):
        # Subir a S3, procesar con Lambda
        pass
    
    def ask_question(self, question):
        # RAG pipeline completo
        pass
```

### 3. API de Clasificación de Texto
```python
# Lambda function para clasificación
def classify_text(event, context):
    text = event['text']
    categories = event.get('categories', ['positive', 'negative', 'neutral'])
    
    prompt = f"""
    Clasifica el siguiente texto en una de estas categorías: {', '.join(categories)}
    
    Texto: {text}
    
    Categoría:
    """
    
    response = invoke_claude(prompt)
    return {'classification': response['completion'].strip()}
```

---

## 📄 Recursos para CV

### Tecnologías a Destacar
- **AWS Bedrock**: Implementación de LLMs en producción
- **RAG Systems**: Retrieval-Augmented Generation con OpenSearch
- **Lambda Functions**: APIs serverless para AI/ML
- **EKS**: Containerización de aplicaciones ML
- **Vector Databases**: OpenSearch, Pinecone para embeddings
- **Caching**: Redis/ElastiCache para optimización

### Certificaciones Relevantes
- AWS Certified Solutions Architect
- AWS Certified Machine Learning - Specialty
- AWS Certified Developer - Associate

### Proyectos para Portfolio
1. **Chatbot RAG**: Sistema de preguntas y respuestas sobre documentos
2. **Document Intelligence**: Extracción y análisis de información
3. **API ML**: Endpoints para clasificación y generación de texto
4. **Pipeline MLOps**: Despliegue automatizado de modelos

### Habilidades Técnicas
- Python, JavaScript/TypeScript
- AWS SDK (boto3)
- Docker, Kubernetes
- Vector databases y embeddings
- LangChain, Hugging Face
- CI/CD para ML (MLOps)

---

## 🔗 Recursos Adicionales

### Documentación AWS
- [AWS Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [Amazon OpenSearch](https://docs.aws.amazon.com/opensearch-service/)
- [AWS Lambda](https://docs.aws.amazon.com/lambda/)
- [Amazon EKS](https://docs.aws.amazon.com/eks/)

### Herramientas y Librerías
- **LangChain**: Framework para aplicaciones LLM
- **Streamlit**: UI rápida para demos
- **FastAPI**: APIs REST para ML
- **Gradio**: Interfaces web para modelos

### Cursos y Certificaciones
- AWS Machine Learning Learning Path
- Deep Learning Specialization (Coursera)
- MLOps Specialization
- AWS Solutions Architect

---

*Última actualización: Julio 2025*