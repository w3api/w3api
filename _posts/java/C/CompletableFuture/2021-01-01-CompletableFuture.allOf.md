---
title: CompletableFuture.allOf()
permalink: /Java/CompletableFuture/allOf/
date: 2021-01-11
key: Java.C.CompletableFuture
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompletableFuture.metodos valor="allOf" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static CompletableFuture<Void> allOf(CompletableFuture<?>... cfs)
~~~

## Parámetros
* **CompletableFuture&lt;?&gt;... cfs**,  {% include w3api/param_description.html metodo=_dato parametro="CompletableFuture<?>... cfs" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

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
