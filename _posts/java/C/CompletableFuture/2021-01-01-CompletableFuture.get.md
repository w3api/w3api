---
title: CompletableFuture.get()
permalink: /Java/CompletableFuture/get/
date: 2021-01-11
key: Java.C.CompletableFuture
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompletableFuture.metodos valor="get" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public T get() throws InterruptedException, ExecutionException
public T get(long timeout, TimeUnit unit) throws InterruptedException, ExecutionException, TimeoutException
~~~

## Parámetros
* **long timeout**,  {% include w3api/param_description.html metodo=_dato parametro="long timeout" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_dato parametro="TimeUnit unit" %}

## Excepciones
[ExecutionException](/Java/ExecutionException/), [InterruptedException](/Java/InterruptedException/), [TimeoutException](/Java/TimeoutException/), [CancellationException](/Java/CancellationException/)

## Clase Padre
[CompletableFuture](/Java/CompletableFuture/)

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
