---
title: PackedColorModel.createCompatibleSampleModel()
permalink: /Java/PackedColorModel/createCompatibleSampleModel/
date: 2021-01-11
key: Java.P.PackedColorModel
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PackedColorModel.metodos valor="createCompatibleSampleModel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SampleModel createCompatibleSampleModel(int w, int h)
~~~

## Parámetros
* **int h**,  {% include w3api/param_description.html metodo=_dato parametro="int h" %}
* **int w**,  {% include w3api/param_description.html metodo=_dato parametro="int w" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PackedColorModel](/Java/PackedColorModel/)

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
