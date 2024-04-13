---
title: SubmissionPublisher.consume()
permalink: /Java/SubmissionPublisher/consume/
date: 2021-01-11
key: Java.S.SubmissionPublisher
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SubmissionPublisher.metodos valor="consume" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CompletableFuture<Void> consume(Consumer<? super T> consumer)
~~~

## Parámetros
* **Consumer&lt;? super T&gt; consumer**,  {% include w3api/param_description.html metodo=_dato parametro="Consumer<? super T> consumer" %}

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
