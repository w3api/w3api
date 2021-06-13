---
title: ForkJoinPool.submit()
permalink: /Java/ForkJoinPool/submit/
date: 2021-01-11
key: Java.F.ForkJoinPool
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.ForkJoinPool.metodos valor="submit" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ForkJoinTask<?> submit(Runnable task)
<T> ForkJoinTask<T> submit(Runnable task, T result)
<T> ForkJoinTask<T> submit(Callable<T> task)
<T> ForkJoinTask<T> submit(ForkJoinTask<T> task)
~~~

## Parámetros
* **Callable&lt;T&gt; task**,  {% include w3api/param_description.html metodo=_dato parametro="Callable<T> task" %}
* **Runnable task**,  {% include w3api/param_description.html metodo=_dato parametro="Runnable task" %}
* **ForkJoinTask&lt;T&gt; task**,  {% include w3api/param_description.html metodo=_dato parametro="ForkJoinTask<T> task" %}
* **T result**,  {% include w3api/param_description.html metodo=_dato parametro="T result" %}

## Excepciones
[RejectedExecutionException](/Java/RejectedExecutionException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ForkJoinPool](/Java/ForkJoinPool/)

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
