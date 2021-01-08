---
title: AtomicInteger.compareAndExchangeAcquire()
permalink: Java/AtomicInteger/compareAndExchangeAcquire
date: 2021-01-04
key: JavaJava.A.AtomicInteger
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicInteger.metodos valor="compareAndExchangeAcquire" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final int compareAndExchangeAcquire(int expectedValue, int newValue)
~~~

## Parámetros
* **int expectedValue**,  {% include w3api/param_description.html metodo=_data parametro="int expectedValue" %}
* **int newValue**,  {% include w3api/param_description.html metodo=_data parametro="int newValue" %}

## Clase Padre
[AtomicInteger](/Java/AtomicInteger/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AtomicInteger.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
