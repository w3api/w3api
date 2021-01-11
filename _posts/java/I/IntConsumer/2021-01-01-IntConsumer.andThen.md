---
title: IntConsumer.andThen()
permalink: Java/IntConsumer/andThen
date: 2021-01-11
key: JavaJava.I.IntConsumer
category: java
tags: ['java se', 'java.util.function', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IntConsumer.metodos valor="andThen" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default IntConsumer andThen(IntConsumer after)
~~~

## Parámetros
* **IntConsumer after**,  {% include w3api/param_description.html metodo=_dato parametro="IntConsumer after" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[IntConsumer](/Java/IntConsumer/)

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
