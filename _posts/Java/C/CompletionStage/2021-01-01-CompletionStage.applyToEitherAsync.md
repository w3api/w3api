---
title: CompletionStage.applyToEitherAsync()
permalink: /Java/CompletionStage/applyToEitherAsync/
date: 2021-01-11
key: Java.C.CompletionStage
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompletionStage.metodos valor="applyToEitherAsync" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<U> CompletionStage<U> applyToEitherAsync(CompletionStage<? extends T> other, Function<? super T,U> fn)
<U> CompletionStage<U> applyToEitherAsync(CompletionStage<? extends T> other, Function<? super T,U> fn, Executor executor)
~~~

## Parámetros
* **U&gt; fn**,  {% include w3api/param_description.html metodo=_dato parametro="U> fn" %}
* **CompletionStage&lt;? extends T&gt; other**,  {% include w3api/param_description.html metodo=_dato parametro="CompletionStage<? extends T> other" %}
* **Function&lt;? super T**,  {% include w3api/param_description.html metodo=_dato parametro="Function<? super T" %}
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
