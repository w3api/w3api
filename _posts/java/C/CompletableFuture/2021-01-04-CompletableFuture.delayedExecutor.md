---
title: CompletableFuture.delayedExecutor()
permalink: Java/CompletableFuture/delayedExecutor
date: 2021-01-04
key: JavaJava.C.CompletableFuture
category: java
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
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_data parametro="TimeUnit unit" %}
* **long delay**,  {% include w3api/param_description.html metodo=_data parametro="long delay" %}
* **Executor executor**,  {% include w3api/param_description.html metodo=_data parametro="Executor executor" %}

## Clase Padre
[CompletableFuture](/Java/CompletableFuture/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CompletableFuture.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
