---
title: SampleModel.getSampleDouble()
permalink: /Java/SampleModel/getSampleDouble/
date: 2021-01-11
key: Java.S.SampleModel
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SampleModel.metodos valor="getSampleDouble" %}

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

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[SampleModel](/Java/SampleModel/)

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
