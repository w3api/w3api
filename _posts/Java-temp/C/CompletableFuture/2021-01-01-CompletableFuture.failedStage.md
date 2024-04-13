---
title: CompletableFuture.failedStage()
permalink: /Java/CompletableFuture/failedStage/
date: 2021-01-11
key: Java.C.CompletableFuture
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompletableFuture.metodos valor="failedStage" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <U> CompletionStage<U> failedStage(Throwable ex)
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
