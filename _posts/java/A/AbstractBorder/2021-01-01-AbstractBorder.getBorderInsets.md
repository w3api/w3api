---
title: AbstractBorder.getBorderInsets()
permalink: /Java/AbstractBorder/getBorderInsets/
date: 2021-01-11
key: Java.A.AbstractBorder
category: Java
tags: ['java se', 'javax.swing.border', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractBorder.metodos valor="getBorderInsets" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Insets getBorderInsets(Component c)
public Insets getBorderInsets(Component c, Insets insets)
~~~

## Parámetros
* **Insets insets**,  {% include w3api/param_description.html metodo=_dato parametro="Insets insets" %}
* **Component c**,  {% include w3api/param_description.html metodo=_dato parametro="Component c" %}

## Clase Padre
[AbstractBorder](/Java/AbstractBorder/)

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
