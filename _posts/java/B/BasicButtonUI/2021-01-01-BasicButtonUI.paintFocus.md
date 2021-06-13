---
title: BasicButtonUI.paintFocus()
permalink: /Java/BasicButtonUI/paintFocus/
date: 2021-01-11
key: Java.B.BasicButtonUI
category: java
tags: ['java se', 'javax.swing.plaf.basic', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BasicButtonUI.metodos valor="paintFocus" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void paintFocus(Graphics g, AbstractButton b, Rectangle viewRect, Rectangle textRect, Rectangle iconRect)
~~~

## Parámetros
* **Graphics g**,  {% include w3api/param_description.html metodo=_dato parametro="Graphics g" %}
* **Rectangle viewRect**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle viewRect" %}
* **AbstractButton b**,  {% include w3api/param_description.html metodo=_dato parametro="AbstractButton b" %}
* **Rectangle iconRect**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle iconRect" %}
* **Rectangle textRect**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle textRect" %}

## Clase Padre
[BasicButtonUI](/Java/BasicButtonUI/)

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
