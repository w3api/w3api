---
title: BandedSampleModel.getSampleDouble()
permalink: /Java/BandedSampleModel/getSampleDouble/
date: 2021-01-11
key: Java.B.BandedSampleModel
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BandedSampleModel.metodos valor="getSampleDouble" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public double getSampleDouble(int x, int y, int b, DataBuffer data)
~~~

## Parámetros
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **DataBuffer data**,  {% include w3api/param_description.html metodo=_dato parametro="DataBuffer data" %}
* **int b**,  {% include w3api/param_description.html metodo=_dato parametro="int b" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}

## Clase Padre
[BandedSampleModel](/Java/BandedSampleModel/)

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
