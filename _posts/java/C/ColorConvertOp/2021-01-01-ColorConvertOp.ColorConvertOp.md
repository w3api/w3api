---
title: ColorConvertOp.ColorConvertOp()
permalink: Java/ColorConvertOp/ColorConvertOp
date: 2021-01-11
key: JavaJava.C.ColorConvertOp
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ColorConvertOp.constructores valor="ColorConvertOp" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ColorConvertOp(ColorSpace srcCspace, ColorSpace dstCspace, RenderingHints hints)
public ColorConvertOp(ColorSpace cspace, RenderingHints hints)
public ColorConvertOp(ICC_Profile[] profiles, RenderingHints hints)
public ColorConvertOp(RenderingHints hints)
~~~

## Parámetros
* **ColorSpace cspace**,  {% include w3api/param_description.html metodo=_dato parametro="ColorSpace cspace" %}
* **ColorSpace dstCspace**,  {% include w3api/param_description.html metodo=_dato parametro="ColorSpace dstCspace" %}
* **ICC_Profile[] profiles**,  {% include w3api/param_description.html metodo=_dato parametro="ICC_Profile[] profiles" %}
* **ColorSpace srcCspace**,  {% include w3api/param_description.html metodo=_dato parametro="ColorSpace srcCspace" %}
* **RenderingHints hints**,  {% include w3api/param_description.html metodo=_dato parametro="RenderingHints hints" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ColorConvertOp](/Java/ColorConvertOp/)

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
