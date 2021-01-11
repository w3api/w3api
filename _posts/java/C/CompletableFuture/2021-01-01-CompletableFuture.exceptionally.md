---
title: CompletableFuture.exceptionally()
permalink: Java/CompletableFuture/exceptionally
date: 2021-01-11
key: JavaJava.C.CompletableFuture
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompletableFuture.metodos valor="exceptionally" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CompletableFuture<T> exceptionally(Function<Throwable,? extends T> fn)
~~~

## Parámetros
* **? extends T&gt; fn**,  {% include w3api/param_description.html metodo=_dato parametro="? extends T> fn" %}
* **Function&lt;Throwable**,  {% include w3api/param_description.html metodo=_dato parametro="Function<Throwable" %}

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
