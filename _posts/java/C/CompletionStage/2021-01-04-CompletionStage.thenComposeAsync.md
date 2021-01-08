---
title: CompletionStage.thenComposeAsync()
permalink: Java/CompletionStage/thenComposeAsync
date: 2021-01-04
key: JavaJava.C.CompletionStage
category: java
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
* **? extends CompletionStage&lt;U&gt;&gt; fn**,  {% include w3api/param_description.html metodo=_data parametro="? extends CompletionStage<U>> fn" %}
* **Function&lt;? super T**,  {% include w3api/param_description.html metodo=_data parametro="Function<? super T" %}
* **Executor executor**,  {% include w3api/param_description.html metodo=_data parametro="Executor executor" %}

## Clase Padre
[CompletionStage](/Java/CompletionStage/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CompletionStage.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
