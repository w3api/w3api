---
title: SubmissionPublisher.SubmissionPublisher()
permalink: Java/SubmissionPublisher/SubmissionPublisher
date: 2021-01-11
key: JavaJava.S.SubmissionPublisher
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SubmissionPublisher.constructores valor="SubmissionPublisher" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SubmissionPublisher()
public SubmissionPublisher(Executor executor, int maxBufferCapacity)
public SubmissionPublisher(Executor executor, int maxBufferCapacity, BiConsumer<? super Flow.Subscriber<? super T>,? super Throwable> handler)
~~~

## Parámetros
* **int maxBufferCapacity**,  {% include w3api/param_description.html metodo=_dato parametro="int maxBufferCapacity" %}
* **? super Throwable&gt; handler**,  {% include w3api/param_description.html metodo=_dato parametro="? super Throwable> handler" %}
* **BiConsumer&lt;? super Flow.Subscriber&lt;? super T&gt;**,  {% include w3api/param_description.html metodo=_dato parametro="BiConsumer<? super Flow.Subscriber<? super T>" %}
* **Executor executor**,  {% include w3api/param_description.html metodo=_dato parametro="Executor executor" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[SubmissionPublisher](/Java/SubmissionPublisher/)

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
