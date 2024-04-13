---
title: SubmissionPublisher.offer()
permalink: /Java/SubmissionPublisher/offer/
date: 2021-01-11
key: Java.S.SubmissionPublisher
category: Java
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
* **long timeout**,  {% include w3api/param_description.html metodo=_dato parametro="long timeout" %}
* **BiPredicate&lt;Flow.Subscriber&lt;? super T&gt;**,  {% include w3api/param_description.html metodo=_dato parametro="BiPredicate<Flow.Subscriber<? super T>" %}
* **T item**,  {% include w3api/param_description.html metodo=_dato parametro="T item" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_dato parametro="TimeUnit unit" %}
* **? super T&gt; onDrop**,  {% include w3api/param_description.html metodo=_dato parametro="? super T> onDrop" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
