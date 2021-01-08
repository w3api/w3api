---
title: CompletableFuture.completedFuture()
permalink: Java/CompletableFuture/completedFuture
date: 2021-01-04
key: JavaJava.C.CompletableFuture
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompletableFuture.metodos valor="completedFuture" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <U> CompletableFuture<U> completedFuture(U value)
~~~

## Parámetros
* **U value**,  {% include w3api/param_description.html metodo=_data parametro="U value" %}

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
