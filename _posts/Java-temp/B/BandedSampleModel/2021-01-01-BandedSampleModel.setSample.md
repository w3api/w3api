---
title: BandedSampleModel.setSample()
permalink: /Java/BandedSampleModel/setSample/
date: 2021-01-11
key: Java.B.BandedSampleModel
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BandedSampleModel.metodos valor="setSample" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setSample(int x, int y, int b, double s, DataBuffer data)
public void setSample(int x, int y, int b, float s, DataBuffer data)
public void setSample(int x, int y, int b, int s, DataBuffer data)
~~~

## Parámetros
* **DataBuffer data**,  {% include w3api/param_description.html metodo=_dato parametro="DataBuffer data" %}
* **double s**,  {% include w3api/param_description.html metodo=_dato parametro="double s" %}
* **int s**,  {% include w3api/param_description.html metodo=_dato parametro="int s" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **float s**,  {% include w3api/param_description.html metodo=_dato parametro="float s" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **int b**,  {% include w3api/param_description.html metodo=_dato parametro="int b" %}

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
