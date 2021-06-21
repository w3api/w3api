---
title: CompletionStage.exceptionally()
permalink: /Java/CompletionStage/exceptionally/
date: 2021-01-11
key: Java.C.CompletionStage
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompletionStage.metodos valor="exceptionally" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
CompletionStage<T> exceptionally(Function<Throwable,? extends T> fn)
~~~

## Parámetros
* **? extends T&gt; fn**,  {% include w3api/param_description.html metodo=_dato parametro="? extends T> fn" %}
* **Function&lt;Throwable**,  {% include w3api/param_description.html metodo=_dato parametro="Function<Throwable" %}

## Clase Padre
[CompletionStage](/Java/CompletionStage/)

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
