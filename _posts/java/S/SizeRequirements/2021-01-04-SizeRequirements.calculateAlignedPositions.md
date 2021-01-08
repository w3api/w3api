---
title: SizeRequirements.calculateAlignedPositions()
permalink: Java/SizeRequirements/calculateAlignedPositions
date: 2021-01-04
key: JavaJava.S.SizeRequirements
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SizeRequirements.metodos valor="calculateAlignedPositions" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void calculateAlignedPositions(int allocated, SizeRequirements total, SizeRequirements[] children, int[] offsets, int[] spans)
public static void calculateAlignedPositions(int allocated, SizeRequirements total, SizeRequirements[] children, int[] offsets, int[] spans, boolean normal)
~~~

## Parámetros
* **SizeRequirements total**,  {% include w3api/param_description.html metodo=_data parametro="SizeRequirements total" %}
* **SizeRequirements[] children**,  {% include w3api/param_description.html metodo=_data parametro="SizeRequirements[] children" %}
* **int[] offsets**,  {% include w3api/param_description.html metodo=_data parametro="int[] offsets" %}
* **int allocated**,  {% include w3api/param_description.html metodo=_data parametro="int allocated" %}
* **boolean normal**,  {% include w3api/param_description.html metodo=_data parametro="boolean normal" %}
* **int[] spans**,  {% include w3api/param_description.html metodo=_data parametro="int[] spans" %}

## Clase Padre
[SizeRequirements](/Java/SizeRequirements/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SizeRequirements.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
