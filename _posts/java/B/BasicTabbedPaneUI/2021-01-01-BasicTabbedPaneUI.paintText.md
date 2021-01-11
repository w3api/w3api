---
title: BasicTabbedPaneUI.paintText()
permalink: Java/BasicTabbedPaneUI/paintText
date: 2021-01-11
key: JavaJava.B.BasicTabbedPaneUI
category: java
tags: ['java se', 'javax.swing.plaf.basic', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BasicTabbedPaneUI.metodos valor="paintText" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void paintText(Graphics g, int tabPlacement, Font font, FontMetrics metrics, int tabIndex, String title, Rectangle textRect, boolean isSelected)
~~~

## Parámetros
* **Rectangle textRect**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle textRect" %}
* **Graphics g**,  {% include w3api/param_description.html metodo=_dato parametro="Graphics g" %}
* **String title**,  {% include w3api/param_description.html metodo=_dato parametro="String title" %}
* **int tabPlacement**,  {% include w3api/param_description.html metodo=_dato parametro="int tabPlacement" %}
* **Font font**,  {% include w3api/param_description.html metodo=_dato parametro="Font font" %}
* **boolean isSelected**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isSelected" %}
* **FontMetrics metrics**,  {% include w3api/param_description.html metodo=_dato parametro="FontMetrics metrics" %}
* **int tabIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int tabIndex" %}

## Clase Padre
[BasicTabbedPaneUI](/Java/BasicTabbedPaneUI/)

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
