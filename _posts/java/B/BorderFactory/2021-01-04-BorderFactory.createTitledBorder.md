---
title: BorderFactory.createTitledBorder()
permalink: Java/BorderFactory/createTitledBorder
date: 2021-01-04
key: JavaJava.B.BorderFactory
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BorderFactory.metodos valor="createTitledBorder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static TitledBorder createTitledBorder(String title)
public static TitledBorder createTitledBorder(Border border)
public static TitledBorder createTitledBorder(Border border, String title)
public static TitledBorder createTitledBorder(Border border, String title, int titleJustification, int titlePosition)
public static TitledBorder createTitledBorder(Border border, String title, int titleJustification, int titlePosition, Font titleFont)
public static TitledBorder createTitledBorder(Border border, String title, int titleJustification, int titlePosition, Font titleFont, Color titleColor)
~~~

## Parámetros
* **String title**,  {% include w3api/param_description.html metodo=_data parametro="String title" %}
* **Border border**,  {% include w3api/param_description.html metodo=_data parametro="Border border" %}
* **Font titleFont**,  {% include w3api/param_description.html metodo=_data parametro="Font titleFont" %}
* **Color titleColor**,  {% include w3api/param_description.html metodo=_data parametro="Color titleColor" %}
* **int titlePosition**,  {% include w3api/param_description.html metodo=_data parametro="int titlePosition" %}
* **int titleJustification**,  {% include w3api/param_description.html metodo=_data parametro="int titleJustification" %}

## Clase Padre
[BorderFactory](/Java/BorderFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BorderFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
