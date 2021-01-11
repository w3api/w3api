---
title: CompletionStage.whenComplete()
permalink: Java/CompletionStage/whenComplete
date: 2021-01-11
key: JavaJava.C.CompletionStage
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompletionStage.metodos valor="whenComplete" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
CompletionStage<T> whenComplete(BiConsumer<? super T,? super Throwable> action)
~~~

## Parámetros
* **? super Throwable&gt; action**,  {% include w3api/param_description.html metodo=_dato parametro="? super Throwable> action" %}
* **BiConsumer&lt;? super T**,  {% include w3api/param_description.html metodo=_dato parametro="BiConsumer<? super T" %}

## Clase Padre
[CompletionStage](/Java/CompletionStage/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
