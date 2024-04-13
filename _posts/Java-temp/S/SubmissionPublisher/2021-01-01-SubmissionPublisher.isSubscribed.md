---
title: SubmissionPublisher.isSubscribed()
permalink: /Java/SubmissionPublisher/isSubscribed/
date: 2021-01-11
key: Java.S.SubmissionPublisher
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SubmissionPublisher.metodos valor="isSubscribed" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean isSubscribed(Flow.Subscriber<? super T> subscriber)
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
