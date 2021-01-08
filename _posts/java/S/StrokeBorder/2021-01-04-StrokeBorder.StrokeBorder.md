---
title: StrokeBorder.StrokeBorder()
permalink: Java/StrokeBorder/StrokeBorder
date: 2021-01-04
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
* **BasicStroke stroke**,  {% include w3api/param_description.html metodo=_data parametro="BasicStroke stroke" %}
* **Paint paint**,  {% include w3api/param_description.html metodo=_data parametro="Paint paint" %}

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
{%- for _ldc in site.data.Java.S.StrokeBorder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
