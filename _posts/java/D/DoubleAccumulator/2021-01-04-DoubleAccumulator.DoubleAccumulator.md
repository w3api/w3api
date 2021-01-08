---
title: DoubleAccumulator.DoubleAccumulator()
permalink: Java/DoubleAccumulator/DoubleAccumulator
date: 2021-01-04
key: JavaJava.D.DoubleAccumulator
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DoubleAccumulator.constructores valor="DoubleAccumulator" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DoubleAccumulator(DoubleBinaryOperator accumulatorFunction, double identity)
~~~

## Parámetros
* **double identity**,  {% include w3api/param_description.html metodo=_data parametro="double identity" %}
* **DoubleBinaryOperator accumulatorFunction**,  {% include w3api/param_description.html metodo=_data parametro="DoubleBinaryOperator accumulatorFunction" %}

## Clase Padre
[DoubleAccumulator](/Java/DoubleAccumulator/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DoubleAccumulator.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
