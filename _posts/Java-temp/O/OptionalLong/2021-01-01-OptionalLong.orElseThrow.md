---
title: OptionalLong.orElseThrow()
permalink: /Java/OptionalLong/orElseThrow/
date: 2021-01-11
key: Java.O.OptionalLong
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.OptionalLong.metodos valor="orElseThrow" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public long orElseThrow()
<X extends Throwable>long orElseThrow(Supplier<? extends X> exceptionSupplier)
~~~

## Parámetros
* **Supplier&lt;? extends X&gt; exceptionSupplier**,  {% include w3api/param_description.html metodo=_dato parametro="Supplier<? extends X> exceptionSupplier" %}

## Excepciones
[NoSuchElementException](/Java/NoSuchElementException/)

## Clase Padre
[OptionalLong](/Java/OptionalLong/)

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
