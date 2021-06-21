---
title: CompletableFuture.delayedExecutor()
permalink: /Java/CompletableFuture/delayedExecutor/
date: 2021-01-11
key: Java.C.CompletableFuture
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompletableFuture.metodos valor="delayedExecutor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Executor delayedExecutor(long delay, TimeUnit unit)
public static Executor delayedExecutor(long delay, TimeUnit unit, Executor executor)
~~~

## Parámetros
* **long delay**,  {% include w3api/param_description.html metodo=_dato parametro="long delay" %}
* **Executor executor**,  {% include w3api/param_description.html metodo=_dato parametro="Executor executor" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_dato parametro="TimeUnit unit" %}

## Clase Padre
[CompletableFuture](/Java/CompletableFuture/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
