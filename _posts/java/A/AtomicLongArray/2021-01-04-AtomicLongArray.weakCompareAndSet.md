---
title: AtomicLongArray.weakCompareAndSet()
permalink: Java/AtomicLongArray/weakCompareAndSet
date: 2021-01-04
key: JavaJava.A.AtomicLongArray
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicLongArray.metodos valor="weakCompareAndSet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated(since="9") public final boolean weakCompareAndSet(int i, long expectedValue, long newValue)
~~~

## Parámetros
* **long expectedValue**,  {% include w3api/param_description.html metodo=_data parametro="long expectedValue" %}
* **int i**,  {% include w3api/param_description.html metodo=_data parametro="int i" %}
* **long newValue**,  {% include w3api/param_description.html metodo=_data parametro="long newValue" %}

## Clase Padre
[AtomicLongArray](/Java/AtomicLongArray/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AtomicLongArray.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
