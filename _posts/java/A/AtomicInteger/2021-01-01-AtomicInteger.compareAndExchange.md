---
title: AtomicInteger.compareAndExchange()
permalink: Java/AtomicInteger/compareAndExchange
date: 2021-01-11
key: JavaJava.A.AtomicInteger
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicInteger.metodos valor="compareAndExchange" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final int compareAndExchange(int expectedValue, int newValue)
~~~

## Parámetros
* **int newValue**,  {% include w3api/param_description.html metodo=_dato parametro="int newValue" %}
* **int expectedValue**,  {% include w3api/param_description.html metodo=_dato parametro="int expectedValue" %}

## Clase Padre
[AtomicInteger](/Java/AtomicInteger/)

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
