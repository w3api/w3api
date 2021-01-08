---
title: AtomicLong.weakCompareAndSetAcquire()
permalink: Java/AtomicLong/weakCompareAndSetAcquire
date: 2021-01-04
key: JavaJava.A.AtomicLong
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicLong.metodos valor="weakCompareAndSetAcquire" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final boolean weakCompareAndSetAcquire(long expectedValue, long newValue)
~~~

## Parámetros
* **long expectedValue**,  {% include w3api/param_description.html metodo=_data parametro="long expectedValue" %}
* **long newValue**,  {% include w3api/param_description.html metodo=_data parametro="long newValue" %}

## Clase Padre
[AtomicLong](/Java/AtomicLong/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AtomicLong.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
