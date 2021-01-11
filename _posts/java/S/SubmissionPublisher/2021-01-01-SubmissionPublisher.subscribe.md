---
title: SubmissionPublisher.subscribe()
permalink: Java/SubmissionPublisher/subscribe
date: 2021-01-11
key: JavaJava.S.SubmissionPublisher
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SubmissionPublisher.metodos valor="subscribe" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void subscribe(Flow.Subscriber<? super T> subscriber)
~~~

## Parámetros
* **Flow.Subscriber&lt;? super T&gt; subscriber**,  {% include w3api/param_description.html metodo=_dato parametro="Flow.Subscriber<? super T> subscriber" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

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