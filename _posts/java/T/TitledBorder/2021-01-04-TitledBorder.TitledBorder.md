---
title: TitledBorder.TitledBorder()
permalink: Java/TitledBorder/TitledBorder
date: 2021-01-04
key: JavaJava.T.TitledBorder
category: java
tags: ['java se', 'javax.swing.border', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TitledBorder.constructores valor="TitledBorder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TitledBorder(String title)
public TitledBorder(Border border)
public TitledBorder(Border border, String title)
public TitledBorder(Border border, String title, int titleJustification, int titlePosition)
public TitledBorder(Border border, String title, int titleJustification, int titlePosition, Font titleFont)
@ConstructorProperties({"border","title","titleJustification","titlePosition","titleFont","titleColor"}) public TitledBorder(Border border, String title, int titleJustification, int titlePosition, Font titleFont, Color titleColor)
~~~

## Parámetros
* **String title**,  {% include w3api/param_description.html metodo=_data parametro="String title" %}
* **Border border**,  {% include w3api/param_description.html metodo=_data parametro="Border border" %}
* **Font titleFont**,  {% include w3api/param_description.html metodo=_data parametro="Font titleFont" %}
* **Color titleColor**,  {% include w3api/param_description.html metodo=_data parametro="Color titleColor" %}
* **int titlePosition**,  {% include w3api/param_description.html metodo=_data parametro="int titlePosition" %}
* **int titleJustification**,  {% include w3api/param_description.html metodo=_data parametro="int titleJustification" %}

## Clase Padre
[TitledBorder](/Java/TitledBorder/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TitledBorder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
