---
title: BasicTabbedPaneUI.paintIcon()
permalink: /Java/BasicTabbedPaneUI/paintIcon/
date: 2021-01-11
key: JavaJava.B.BasicTabbedPaneUI
category: java
tags: ['java se', 'javax.swing.plaf.basic', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BasicTabbedPaneUI.metodos valor="paintIcon" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void paintIcon(Graphics g, int tabPlacement, int tabIndex, Icon icon, Rectangle iconRect, boolean isSelected)
~~~

## Parámetros
* **Graphics g**,  {% include w3api/param_description.html metodo=_dato parametro="Graphics g" %}
* **Icon icon**,  {% include w3api/param_description.html metodo=_dato parametro="Icon icon" %}
* **Rectangle iconRect**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle iconRect" %}
* **int tabPlacement**,  {% include w3api/param_description.html metodo=_dato parametro="int tabPlacement" %}
* **boolean isSelected**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isSelected" %}
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
