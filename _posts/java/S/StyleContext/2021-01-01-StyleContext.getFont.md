---
title: StyleContext.getFont()
permalink: Java/StyleContext/getFont
date: 2021-01-11
key: JavaJava.S.StyleContext
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StyleContext.metodos valor="getFont" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Font getFont(String family, int style, int size)
public Font getFont(AttributeSet attr)
~~~

## Parámetros
* **AttributeSet attr**,  {% include w3api/param_description.html metodo=_dato parametro="AttributeSet attr" %}
* **String family**,  {% include w3api/param_description.html metodo=_dato parametro="String family" %}
* **int style**,  {% include w3api/param_description.html metodo=_dato parametro="int style" %}
* **int size**,  {% include w3api/param_description.html metodo=_dato parametro="int size" %}

## Clase Padre
[StyleContext](/Java/StyleContext/)

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
