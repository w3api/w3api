---
title: BevelBorder.BevelBorder()
permalink: Java/BevelBorder/BevelBorder
date: 2021-01-04
key: JavaJava.B.BevelBorder
category: java
tags: ['java se', 'javax.swing.border', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BevelBorder.constructores valor="BevelBorder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BevelBorder(int bevelType)
public BevelBorder(int bevelType, Color highlight, Color shadow)
@ConstructorProperties({"bevelType","highlightOuterColor","highlightInnerColor","shadowOuterColor","shadowInnerColor"}) public BevelBorder(int bevelType, Color highlightOuterColor, Color highlightInnerColor, Color shadowOuterColor, Color shadowInnerColor)
~~~

## Parámetros
* **Color shadowInnerColor**,  {% include w3api/param_description.html metodo=_data parametro="Color shadowInnerColor" %}
* **Color highlightOuterColor**,  {% include w3api/param_description.html metodo=_data parametro="Color highlightOuterColor" %}
* **Color highlight**,  {% include w3api/param_description.html metodo=_data parametro="Color highlight" %}
* **Color highlightInnerColor**,  {% include w3api/param_description.html metodo=_data parametro="Color highlightInnerColor" %}
* **Color shadowOuterColor**,  {% include w3api/param_description.html metodo=_data parametro="Color shadowOuterColor" %}
* **int bevelType**,  {% include w3api/param_description.html metodo=_data parametro="int bevelType" %}
* **Color shadow**,  {% include w3api/param_description.html metodo=_data parametro="Color shadow" %}

## Clase Padre
[BevelBorder](/Java/BevelBorder/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BevelBorder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
