---
title: FutureTask.get()
permalink: /Java/FutureTask/get/
date: 2021-01-11
key: Java.F.FutureTask
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FutureTask.metodos valor="get" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public V get() throws InterruptedException, ExecutionException
public V get(long timeout, TimeUnit unit) throws InterruptedException, ExecutionException, TimeoutException
~~~

## Parámetros
* **long timeout**,  {% include w3api/param_description.html metodo=_dato parametro="long timeout" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_dato parametro="TimeUnit unit" %}

## Excepciones
[ExecutionException](/Java/ExecutionException/), [InterruptedException](/Java/InterruptedException/), [TimeoutException](/Java/TimeoutException/), [CancellationException](/Java/CancellationException/)

## Clase Padre
[FutureTask](/Java/FutureTask/)

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
