---
title: BasicMenuItemUI.paintText()
permalink: Java/BasicMenuItemUI/paintText
date: 2021-01-04
key: JavaJava.B.BasicMenuItemUI
category: java
tags: ['java se', 'javax.swing.plaf.basic', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BasicMenuItemUI.metodos valor="paintText" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void paintText(Graphics g, JMenuItem menuItem, Rectangle textRect, String text)
~~~

## Parámetros
* **JMenuItem menuItem**,  {% include w3api/param_description.html metodo=_data parametro="JMenuItem menuItem" %}
* **String text**,  {% include w3api/param_description.html metodo=_data parametro="String text" %}
* **Rectangle textRect**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle textRect" %}
* **Graphics g**,  {% include w3api/param_description.html metodo=_data parametro="Graphics g" %}

## Clase Padre
[BasicMenuItemUI](/Java/BasicMenuItemUI/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BasicMenuItemUI.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
