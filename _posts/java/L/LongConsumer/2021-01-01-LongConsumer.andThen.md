---
title: LongConsumer.andThen()
permalink: Java/LongConsumer/andThen
date: 2021-01-11
key: JavaJava.L.LongConsumer
category: java
tags: ['java se', 'java.util.function', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LongConsumer.metodos valor="andThen" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default LongConsumer andThen(LongConsumer after)
~~~

## Parámetros
* **LongConsumer after**,  {% include w3api/param_description.html metodo=_dato parametro="LongConsumer after" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[LongConsumer](/Java/LongConsumer/)

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
