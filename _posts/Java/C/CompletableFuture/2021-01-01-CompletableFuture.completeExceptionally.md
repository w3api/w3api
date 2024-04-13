---
title: CompletableFuture.completeExceptionally()
permalink: /Java/CompletableFuture/completeExceptionally/
date: 2021-01-11
key: Java.C.CompletableFuture
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompletableFuture.metodos valor="completeExceptionally" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean completeExceptionally(Throwable ex)
~~~

## Parámetros
* **Throwable ex**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable ex" %}

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
