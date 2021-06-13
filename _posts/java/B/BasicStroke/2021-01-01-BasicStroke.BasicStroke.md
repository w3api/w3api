---
title: BasicStroke.BasicStroke()
permalink: /Java/BasicStroke/BasicStroke/
date: 2021-01-11
key: Java.B.BasicStroke
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BasicStroke.constructores valor="BasicStroke" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BasicStroke()
public BasicStroke(float width)
public BasicStroke(float width, int cap, int join)
public BasicStroke(float width, int cap, int join, float miterlimit)
@ConstructorProperties({"lineWidth","endCap","lineJoin","miterLimit","dashArray","dashPhase"}) public BasicStroke(float width, int cap, int join, float miterlimit, float[] dash, float dash_phase)
~~~

## Parámetros
* **float[] dash**,  {% include w3api/param_description.html metodo=_dato parametro="float[] dash" %}
* **int join**,  {% include w3api/param_description.html metodo=_dato parametro="int join" %}
* **int cap**,  {% include w3api/param_description.html metodo=_dato parametro="int cap" %}
* **float dash_phase**,  {% include w3api/param_description.html metodo=_dato parametro="float dash_phase" %}
* **float miterlimit**,  {% include w3api/param_description.html metodo=_dato parametro="float miterlimit" %}
* **float width**,  {% include w3api/param_description.html metodo=_dato parametro="float width" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[BasicStroke](/Java/BasicStroke/)

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
