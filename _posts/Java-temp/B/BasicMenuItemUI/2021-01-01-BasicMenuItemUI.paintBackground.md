---
title: BasicMenuItemUI.paintBackground()
permalink: /Java/BasicMenuItemUI/paintBackground/
date: 2021-01-11
key: Java.B.BasicMenuItemUI
category: Java
tags: ['java se', 'javax.swing.plaf.basic', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BasicMenuItemUI.metodos valor="paintBackground" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void paintBackground(Graphics g, JMenuItem menuItem, Color bgColor)
~~~

## Parámetros
* **Color bgColor**,  {% include w3api/param_description.html metodo=_dato parametro="Color bgColor" %}
* **Graphics g**,  {% include w3api/param_description.html metodo=_dato parametro="Graphics g" %}
* **JMenuItem menuItem**,  {% include w3api/param_description.html metodo=_dato parametro="JMenuItem menuItem" %}

## Clase Padre
[BasicMenuItemUI](/Java/BasicMenuItemUI/)

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
