---
title: BasicTabbedPaneUI.paintText()
permalink: Java/BasicTabbedPaneUI/paintText
date: 2021-01-04
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
* **String title**,  {% include w3api/param_description.html metodo=_data parametro="String title" %}
* **int tabIndex**,  {% include w3api/param_description.html metodo=_data parametro="int tabIndex" %}
* **Graphics g**,  {% include w3api/param_description.html metodo=_data parametro="Graphics g" %}
* **int tabPlacement**,  {% include w3api/param_description.html metodo=_data parametro="int tabPlacement" %}
* **Font font**,  {% include w3api/param_description.html metodo=_data parametro="Font font" %}
* **Rectangle textRect**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle textRect" %}
* **boolean isSelected**,  {% include w3api/param_description.html metodo=_data parametro="boolean isSelected" %}
* **FontMetrics metrics**,  {% include w3api/param_description.html metodo=_data parametro="FontMetrics metrics" %}

## Clase Padre
[BasicTabbedPaneUI](/Java/BasicTabbedPaneUI/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BasicTabbedPaneUI.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
