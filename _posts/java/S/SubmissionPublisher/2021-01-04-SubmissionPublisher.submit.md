---
title: SubmissionPublisher.submit()
permalink: Java/SubmissionPublisher/submit
date: 2021-01-04
key: JavaJava.S.SubmissionPublisher
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SubmissionPublisher.metodos valor="submit" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int submit(T item)
~~~

## Parámetros
* **T item**,  {% include w3api/param_description.html metodo=_data parametro="T item" %}

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
