---
title: SizeRequirements.calculateTiledPositions()
permalink: Java/SizeRequirements/calculateTiledPositions
date: 2021-01-04
key: JavaJava.S.SizeRequirements
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SizeRequirements.metodos valor="calculateTiledPositions" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void calculateTiledPositions(int allocated, SizeRequirements total, SizeRequirements[] children, int[] offsets, int[] spans)
public static void calculateTiledPositions(int allocated, SizeRequirements total, SizeRequirements[] children, int[] offsets, int[] spans, boolean forward)
~~~

## Parámetros
* **SizeRequirements total**,  {% include w3api/param_description.html metodo=_data parametro="SizeRequirements total" %}
* **boolean forward**,  {% include w3api/param_description.html metodo=_data parametro="boolean forward" %}
* **SizeRequirements[] children**,  {% include w3api/param_description.html metodo=_data parametro="SizeRequirements[] children" %}
* **int[] offsets**,  {% include w3api/param_description.html metodo=_data parametro="int[] offsets" %}
* **int allocated**,  {% include w3api/param_description.html metodo=_data parametro="int allocated" %}
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
