---
title: AbstractExecutorService.submit()
permalink: Java/AbstractExecutorService/submit
date: 2021-01-10
key: JavaJava.A.AbstractExecutorService
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractExecutorService.metodos valor="submit" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Future<?> submit(Runnable task)
<T> Future<T> submit(Runnable task, T result)
<T> Future<T> submit(Callable<T> task)
~~~

## Parámetros
* **Runnable task**,  {% include w3api/param_description.html metodo=_dato parametro="Runnable task" %}
* **Callable&lt;T&gt; task**,  {% include w3api/param_description.html metodo=_dato parametro="Callable<T> task" %}
* **T result**,  {% include w3api/param_description.html metodo=_dato parametro="T result" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [RejectedExecutionException](/Java/RejectedExecutionException/)

## Clase Padre
[AbstractExecutorService](/Java/AbstractExecutorService/)

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
