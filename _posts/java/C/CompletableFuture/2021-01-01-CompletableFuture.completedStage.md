---
title: CompletableFuture.completedStage()
permalink: /Java/CompletableFuture/completedStage/
date: 2021-01-11
key: Java.C.CompletableFuture
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompletableFuture.metodos valor="completedStage" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <U> CompletionStage<U> completedStage(U value)
~~~

## Parámetros
* **U value**,  {% include w3api/param_description.html metodo=_dato parametro="U value" %}

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
