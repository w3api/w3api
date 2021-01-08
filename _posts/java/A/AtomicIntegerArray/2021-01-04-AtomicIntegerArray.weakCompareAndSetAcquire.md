---
title: AtomicIntegerArray.weakCompareAndSetAcquire()
permalink: Java/AtomicIntegerArray/weakCompareAndSetAcquire
date: 2021-01-04
key: JavaJava.A.AtomicIntegerArray
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicIntegerArray.metodos valor="weakCompareAndSetAcquire" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final boolean weakCompareAndSetAcquire(int i, int expectedValue, int newValue)
~~~

## Parámetros
* **int expectedValue**,  {% include w3api/param_description.html metodo=_data parametro="int expectedValue" %}
* **int i**,  {% include w3api/param_description.html metodo=_data parametro="int i" %}
* **int newValue**,  {% include w3api/param_description.html metodo=_data parametro="int newValue" %}

## Clase Padre
[AtomicIntegerArray](/Java/AtomicIntegerArray/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AtomicIntegerArray.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
