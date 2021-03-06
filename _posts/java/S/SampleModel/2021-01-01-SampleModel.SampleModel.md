---
title: SampleModel.SampleModel()
permalink: /Java/SampleModel/SampleModel/
date: 2021-01-11
key: Java.S.SampleModel
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SampleModel.constructores valor="SampleModel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SampleModel(int dataType, int w, int h, int numBands)
~~~

## Parámetros
* **int h**,  {% include w3api/param_description.html metodo=_dato parametro="int h" %}
* **int numBands**,  {% include w3api/param_description.html metodo=_dato parametro="int numBands" %}
* **int dataType**,  {% include w3api/param_description.html metodo=_dato parametro="int dataType" %}
* **int w**,  {% include w3api/param_description.html metodo=_dato parametro="int w" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

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
