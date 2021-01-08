---
title: SubmissionPublisher.offer()
permalink: Java/SubmissionPublisher/offer
date: 2021-01-04
key: JavaJava.S.SubmissionPublisher
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SubmissionPublisher.metodos valor="offer" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int offer(T item, long timeout, TimeUnit unit, BiPredicate<Flow.Subscriber<? super T>,? super T> onDrop)
public int offer(T item, BiPredicate<Flow.Subscriber<? super T>,? super T> onDrop)
~~~

## Parámetros
* **? super T&gt; onDrop**,  {% include w3api/param_description.html metodo=_data parametro="? super T> onDrop" %}
* **T item**,  {% include w3api/param_description.html metodo=_data parametro="T item" %}
* **BiPredicate&lt;Flow.Subscriber&lt;? super T&gt;**,  {% include w3api/param_description.html metodo=_data parametro="BiPredicate<Flow.Subscriber<? super T>" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_data parametro="TimeUnit unit" %}
* **long timeout**,  {% include w3api/param_description.html metodo=_data parametro="long timeout" %}

## Excepciones
[RejectedExecutionException](/Java/RejectedExecutionException/), [IllegalStateException](/Java/IllegalStateException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[SubmissionPublisher](/Java/SubmissionPublisher/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SubmissionPublisher.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
