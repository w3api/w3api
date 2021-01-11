---
title: SizeRequirements.calculateTiledPositions()
permalink: Java/SizeRequirements/calculateTiledPositions
date: 2021-01-11
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
* **int[] spans**,  {% include w3api/param_description.html metodo=_dato parametro="int[] spans" %}
* **SizeRequirements total**,  {% include w3api/param_description.html metodo=_dato parametro="SizeRequirements total" %}
* **SizeRequirements[] children**,  {% include w3api/param_description.html metodo=_dato parametro="SizeRequirements[] children" %}
* **boolean forward**,  {% include w3api/param_description.html metodo=_dato parametro="boolean forward" %}
* **int allocated**,  {% include w3api/param_description.html metodo=_dato parametro="int allocated" %}
* **int[] offsets**,  {% include w3api/param_description.html metodo=_dato parametro="int[] offsets" %}

## Clase Padre
[SizeRequirements](/Java/SizeRequirements/)

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
