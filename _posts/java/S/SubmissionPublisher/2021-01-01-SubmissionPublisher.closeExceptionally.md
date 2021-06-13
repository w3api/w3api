---
title: SubmissionPublisher.closeExceptionally()
permalink: /Java/SubmissionPublisher/closeExceptionally/
date: 2021-01-11
key: Java.S.SubmissionPublisher
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SubmissionPublisher.metodos valor="closeExceptionally" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void closeExceptionally(Throwable error)
~~~

## Parámetros
* **Throwable error**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable error" %}

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
