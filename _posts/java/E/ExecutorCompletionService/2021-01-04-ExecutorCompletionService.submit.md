---
title: ExecutorCompletionService.submit()
permalink: Java/ExecutorCompletionService/submit
date: 2021-01-04
key: JavaJava.E.ExecutorCompletionService
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ExecutorCompletionService.metodos valor="submit" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Future<V> submit(Runnable task, V result)
public Future<V> submit(Callable<V> task)
~~~

## Parámetros
* **Runnable task**,  {% include w3api/param_description.html metodo=_data parametro="Runnable task" %}
* **Callable&lt;V&gt; task**,  {% include w3api/param_description.html metodo=_data parametro="Callable<V> task" %}
* **V result**,  {% include w3api/param_description.html metodo=_data parametro="V result" %}

## Excepciones
[RejectedExecutionException](/Java/RejectedExecutionException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ExecutorCompletionService](/Java/ExecutorCompletionService/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.ExecutorCompletionService.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
