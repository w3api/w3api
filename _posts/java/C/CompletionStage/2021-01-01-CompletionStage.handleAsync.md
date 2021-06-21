---
title: CompletionStage.handleAsync()
permalink: /Java/CompletionStage/handleAsync/
date: 2021-01-11
key: Java.C.CompletionStage
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompletionStage.metodos valor="handleAsync" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<U> CompletionStage<U> handleAsync(BiFunction<? super T,Throwable,? extends U> fn)
<U> CompletionStage<U> handleAsync(BiFunction<? super T,Throwable,? extends U> fn, Executor executor)
~~~

## Parámetros
* **Throwable**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable" %}
* **? extends U&gt; fn**,  {% include w3api/param_description.html metodo=_dato parametro="? extends U> fn" %}
* **BiFunction&lt;? super T**,  {% include w3api/param_description.html metodo=_dato parametro="BiFunction<? super T" %}
* **Executor executor**,  {% include w3api/param_description.html metodo=_dato parametro="Executor executor" %}

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
