---
title: CompletableFuture.runAsync()
permalink: Java/CompletableFuture/runAsync
date: 2021-01-04
key: JavaJava.C.CompletableFuture
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompletableFuture.metodos valor="runAsync" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static CompletableFuture<Void> runAsync(Runnable runnable)
public static CompletableFuture<Void> runAsync(Runnable runnable, Executor executor)
~~~

## Parámetros
* **Executor executor**,  {% include w3api/param_description.html metodo=_data parametro="Executor executor" %}
* **Runnable runnable**,  {% include w3api/param_description.html metodo=_data parametro="Runnable runnable" %}

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
