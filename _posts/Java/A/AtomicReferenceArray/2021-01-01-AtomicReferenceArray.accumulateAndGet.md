---
title: AtomicReferenceArray.accumulateAndGet()
permalink: /Java/AtomicReferenceArray/accumulateAndGet/
date: 2021-01-11
key: Java.A.AtomicReferenceArray
category: Java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicReferenceArray.metodos valor="accumulateAndGet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final E accumulateAndGet(int i, E x, BinaryOperator<E> accumulatorFunction)
~~~

## Parámetros
* **E x**,  {% include w3api/param_description.html metodo=_dato parametro="E x" %}
* **int i**,  {% include w3api/param_description.html metodo=_dato parametro="int i" %}
* **BinaryOperator&lt;E&gt; accumulatorFunction**,  {% include w3api/param_description.html metodo=_dato parametro="BinaryOperator<E> accumulatorFunction" %}

## Clase Padre
[AtomicReferenceArray](/Java/AtomicReferenceArray/)

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
