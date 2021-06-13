---
title: OptionalDouble.orElseThrow()
permalink: /Java/OptionalDouble/orElseThrow/
date: 2021-01-11
key: JavaJava.O.OptionalDouble
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.OptionalDouble.metodos valor="orElseThrow" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public double orElseThrow()
<X extends Throwable>double orElseThrow(Supplier<? extends X> exceptionSupplier)
~~~

## Parámetros
* **Supplier&lt;? extends X&gt; exceptionSupplier**,  {% include w3api/param_description.html metodo=_dato parametro="Supplier<? extends X> exceptionSupplier" %}

## Excepciones
[NoSuchElementException](/Java/NoSuchElementException/)

## Clase Padre
[OptionalDouble](/Java/OptionalDouble/)

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
