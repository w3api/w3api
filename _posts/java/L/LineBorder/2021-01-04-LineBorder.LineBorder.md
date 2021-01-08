---
title: LineBorder.LineBorder()
permalink: Java/LineBorder/LineBorder
date: 2021-01-04
key: JavaJava.L.LineBorder
category: java
tags: ['java se', 'javax.swing.border', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LineBorder.constructores valor="LineBorder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LineBorder(Color color)
public LineBorder(Color color, int thickness)
@ConstructorProperties({"lineColor","thickness","roundedCorners"}) public LineBorder(Color color, int thickness, boolean roundedCorners)
~~~

## Parámetros
* **int thickness**,  {% include w3api/param_description.html metodo=_data parametro="int thickness" %}
* **boolean roundedCorners**,  {% include w3api/param_description.html metodo=_data parametro="boolean roundedCorners" %}
* **Color color**,  {% include w3api/param_description.html metodo=_data parametro="Color color" %}

## Clase Padre
[LineBorder](/Java/LineBorder/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LineBorder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
