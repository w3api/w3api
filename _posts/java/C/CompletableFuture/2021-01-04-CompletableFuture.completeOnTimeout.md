---
title: CompletableFuture.completeOnTimeout()
permalink: Java/CompletableFuture/completeOnTimeout
date: 2021-01-04
key: JavaJava.C.CompletableFuture
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompletableFuture.metodos valor="completeOnTimeout" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CompletableFuture<T> completeOnTimeout(T value, long timeout, TimeUnit unit)
~~~

## Parámetros
* **T value**,  {% include w3api/param_description.html metodo=_data parametro="T value" %}
* **long timeout**,  {% include w3api/param_description.html metodo=_data parametro="long timeout" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_data parametro="TimeUnit unit" %}

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
