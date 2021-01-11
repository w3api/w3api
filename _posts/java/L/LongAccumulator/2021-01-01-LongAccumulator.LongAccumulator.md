---
title: LongAccumulator.LongAccumulator()
permalink: Java/LongAccumulator/LongAccumulator
date: 2021-01-11
key: JavaJava.L.LongAccumulator
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LongAccumulator.constructores valor="LongAccumulator" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LongAccumulator(LongBinaryOperator accumulatorFunction, long identity)
~~~

## Parámetros
* **long identity**,  {% include w3api/param_description.html metodo=_dato parametro="long identity" %}
* **LongBinaryOperator accumulatorFunction**,  {% include w3api/param_description.html metodo=_dato parametro="LongBinaryOperator accumulatorFunction" %}

## Clase Padre
[LongAccumulator](/Java/LongAccumulator/)

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
