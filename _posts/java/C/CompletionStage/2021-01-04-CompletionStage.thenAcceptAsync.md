---
title: CompletionStage.thenAcceptAsync()
permalink: Java/CompletionStage/thenAcceptAsync
date: 2021-01-04
key: JavaJava.C.CompletionStage
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompletionStage.metodos valor="thenAcceptAsync" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
CompletionStage<Void> thenAcceptAsync(Consumer<? super T> action)
CompletionStage<Void> thenAcceptAsync(Consumer<? super T> action, Executor executor)
~~~

## Parámetros
* **Consumer&lt;? super T&gt; action**,  {% include w3api/param_description.html metodo=_data parametro="Consumer<? super T> action" %}
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
