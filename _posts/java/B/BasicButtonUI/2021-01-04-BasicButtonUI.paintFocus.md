---
title: BasicButtonUI.paintFocus()
permalink: Java/BasicButtonUI/paintFocus
date: 2021-01-04
key: JavaJava.B.BasicButtonUI
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
* **AbstractButton b**,  {% include w3api/param_description.html metodo=_data parametro="AbstractButton b" %}
* **Graphics g**,  {% include w3api/param_description.html metodo=_data parametro="Graphics g" %}
* **Rectangle iconRect**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle iconRect" %}
* **Rectangle viewRect**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle viewRect" %}
* **Rectangle textRect**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle textRect" %}

## Clase Padre
[BasicButtonUI](/Java/BasicButtonUI/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BasicButtonUI.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
