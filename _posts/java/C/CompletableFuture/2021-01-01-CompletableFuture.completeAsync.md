---
title: CompletableFuture.completeAsync()
permalink: Java/CompletableFuture/completeAsync
date: 2021-01-11
key: JavaJava.C.CompletableFuture
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompletableFuture.metodos valor="completeAsync" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CompletableFuture<T> completeAsync(Supplier<? extends T> supplier)
public CompletableFuture<T> completeAsync(Supplier<? extends T> supplier, Executor executor)
~~~

## Parámetros
* **Supplier&lt;? extends T&gt; supplier**,  {% include w3api/param_description.html metodo=_dato parametro="Supplier<? extends T> supplier" %}
* **Executor executor**,  {% include w3api/param_description.html metodo=_dato parametro="Executor executor" %}

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
