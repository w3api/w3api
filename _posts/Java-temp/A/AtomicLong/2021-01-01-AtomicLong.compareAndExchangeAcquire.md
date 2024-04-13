---
title: AtomicLong.compareAndExchangeAcquire()
permalink: /Java/AtomicLong/compareAndExchangeAcquire/
date: 2021-01-11
key: Java.A.AtomicLong
category: Java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicLong.metodos valor="compareAndExchangeAcquire" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final long compareAndExchangeAcquire(long expectedValue, long newValue)
~~~

## Parámetros
* **long newValue**,  {% include w3api/param_description.html metodo=_dato parametro="long newValue" %}
* **long expectedValue**,  {% include w3api/param_description.html metodo=_dato parametro="long expectedValue" %}

## Clase Padre
[AtomicLong](/Java/AtomicLong/)

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
