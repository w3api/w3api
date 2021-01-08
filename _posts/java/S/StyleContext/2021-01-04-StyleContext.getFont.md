---
title: StyleContext.getFont()
permalink: Java/StyleContext/getFont
date: 2021-01-04
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
* **AttributeSet attr**,  {% include w3api/param_description.html metodo=_data parametro="AttributeSet attr" %}
* **String family**,  {% include w3api/param_description.html metodo=_data parametro="String family" %}
* **int size**,  {% include w3api/param_description.html metodo=_data parametro="int size" %}
* **int style**,  {% include w3api/param_description.html metodo=_data parametro="int style" %}

## Clase Padre
[StyleContext](/Java/StyleContext/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StyleContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
