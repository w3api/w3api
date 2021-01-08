---
title: UncheckedIOException.UncheckedIOException()
permalink: Java/UncheckedIOException/UncheckedIOException
date: 2021-01-04
key: JavaJava.U.UncheckedIOException
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.UncheckedIOException.constructores valor="UncheckedIOException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public UncheckedIOException(IOException cause)
public UncheckedIOException(String message, IOException cause)
~~~

## Parámetros
* **IOException cause**,  {% include w3api/param_description.html metodo=_data parametro="IOException cause" %}
* **String message**,  {% include w3api/param_description.html metodo=_data parametro="String message" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[UncheckedIOException](/Java/UncheckedIOException/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.U.UncheckedIOException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
