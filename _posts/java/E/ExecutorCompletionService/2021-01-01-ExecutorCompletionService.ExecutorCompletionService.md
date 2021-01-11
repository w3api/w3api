---
title: ExecutorCompletionService.ExecutorCompletionService()
permalink: Java/ExecutorCompletionService/ExecutorCompletionService
date: 2021-01-11
key: JavaJava.E.ExecutorCompletionService
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ExecutorCompletionService.constructores valor="ExecutorCompletionService" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ExecutorCompletionService(Executor executor)
public ExecutorCompletionService(Executor executor, BlockingQueue<Future<V>> completionQueue)
~~~

## Parámetros
* **Executor executor**,  {% include w3api/param_description.html metodo=_dato parametro="Executor executor" %}
* **BlockingQueue&lt;Future&lt;V&gt;&gt; completionQueue**,  {% include w3api/param_description.html metodo=_dato parametro="BlockingQueue<Future<V>> completionQueue" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ExecutorCompletionService](/Java/ExecutorCompletionService/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
