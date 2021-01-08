---
title: CompletionStage.whenCompleteAsync()
permalink: Java/CompletionStage/whenCompleteAsync
date: 2021-01-04
key: JavaJava.C.CompletionStage
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompletionStage.metodos valor="whenCompleteAsync" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
CompletionStage<T> whenCompleteAsync(BiConsumer<? super T,? super Throwable> action)
CompletionStage<T> whenCompleteAsync(BiConsumer<? super T,? super Throwable> action, Executor executor)
~~~

## Parámetros
* **? super Throwable&gt; action**,  {% include w3api/param_description.html metodo=_data parametro="? super Throwable> action" %}
* **BiConsumer&lt;? super T**,  {% include w3api/param_description.html metodo=_data parametro="BiConsumer<? super T" %}
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
