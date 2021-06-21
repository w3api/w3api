---
title: CompletionStage.thenComposeAsync()
permalink: /Java/CompletionStage/thenComposeAsync/
date: 2021-01-11
key: Java.C.CompletionStage
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompletionStage.metodos valor="thenComposeAsync" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<U> CompletionStage<U> thenComposeAsync(Function<? super T,? extends CompletionStage<U>> fn)
<U> CompletionStage<U> thenComposeAsync(Function<? super T,? extends CompletionStage<U>> fn, Executor executor)
~~~

## Parámetros
* **? extends CompletionStage&lt;U&gt;&gt; fn**,  {% include w3api/param_description.html metodo=_dato parametro="? extends CompletionStage<U>> fn" %}
* **Executor executor**,  {% include w3api/param_description.html metodo=_dato parametro="Executor executor" %}
* **Function&lt;? super T**,  {% include w3api/param_description.html metodo=_dato parametro="Function<? super T" %}

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
