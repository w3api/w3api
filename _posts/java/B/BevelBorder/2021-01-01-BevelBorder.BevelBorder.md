---
title: BevelBorder.BevelBorder()
permalink: Java/BevelBorder/BevelBorder
date: 2021-01-11
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
* **Color shadow**,  {% include w3api/param_description.html metodo=_dato parametro="Color shadow" %}
* **Color highlight**,  {% include w3api/param_description.html metodo=_dato parametro="Color highlight" %}
* **Color highlightOuterColor**,  {% include w3api/param_description.html metodo=_dato parametro="Color highlightOuterColor" %}
* **Color shadowInnerColor**,  {% include w3api/param_description.html metodo=_dato parametro="Color shadowInnerColor" %}
* **Color highlightInnerColor**,  {% include w3api/param_description.html metodo=_dato parametro="Color highlightInnerColor" %}
* **int bevelType**,  {% include w3api/param_description.html metodo=_dato parametro="int bevelType" %}
* **Color shadowOuterColor**,  {% include w3api/param_description.html metodo=_dato parametro="Color shadowOuterColor" %}

## Clase Padre
[BevelBorder](/Java/BevelBorder/)

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
