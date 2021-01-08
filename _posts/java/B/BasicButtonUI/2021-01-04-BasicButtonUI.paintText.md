---
title: BasicButtonUI.paintText()
permalink: Java/BasicButtonUI/paintText
date: 2021-01-04
key: JavaJava.B.BasicButtonUI
category: java
tags: ['java se', 'javax.swing.plaf.basic', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BasicButtonUI.metodos valor="paintText" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void paintText(Graphics g, AbstractButton b, Rectangle textRect, String text)
protected void paintText(Graphics g, JComponent c, Rectangle textRect, String text)
~~~

## Parámetros
* **AbstractButton b**,  {% include w3api/param_description.html metodo=_data parametro="AbstractButton b" %}
* **String text**,  {% include w3api/param_description.html metodo=_data parametro="String text" %}
* **JComponent c**,  {% include w3api/param_description.html metodo=_data parametro="JComponent c" %}
* **Graphics g**,  {% include w3api/param_description.html metodo=_data parametro="Graphics g" %}
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
