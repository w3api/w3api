---
title: StrokeBorder.StrokeBorder()
permalink: Java/StrokeBorder/StrokeBorder
date: 2021-01-11
key: JavaJava.S.StrokeBorder
category: java
tags: ['java se', 'javax.swing.border', 'java.desktop', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StrokeBorder.constructores valor="StrokeBorder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public StrokeBorder(BasicStroke stroke)
@ConstructorProperties({"stroke","paint"}) public StrokeBorder(BasicStroke stroke, Paint paint)
~~~

## Parámetros
* **Paint paint**,  {% include w3api/param_description.html metodo=_dato parametro="Paint paint" %}
* **BasicStroke stroke**,  {% include w3api/param_description.html metodo=_dato parametro="BasicStroke stroke" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[StrokeBorder](/Java/StrokeBorder/)

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
