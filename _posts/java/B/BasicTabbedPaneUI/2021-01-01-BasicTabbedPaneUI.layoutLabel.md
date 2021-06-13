---
title: BasicTabbedPaneUI.layoutLabel()
permalink: /Java/BasicTabbedPaneUI/layoutLabel/
date: 2021-01-11
key: Java.B.BasicTabbedPaneUI
category: Java
tags: ['java se', 'javax.swing.plaf.basic', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BasicTabbedPaneUI.metodos valor="layoutLabel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void layoutLabel(int tabPlacement, FontMetrics metrics, int tabIndex, String title, Icon icon, Rectangle tabRect, Rectangle iconRect, Rectangle textRect, boolean isSelected)
~~~

## Parámetros
* **Rectangle textRect**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle textRect" %}
* **Icon icon**,  {% include w3api/param_description.html metodo=_dato parametro="Icon icon" %}
* **String title**,  {% include w3api/param_description.html metodo=_dato parametro="String title" %}
* **Rectangle iconRect**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle iconRect" %}
* **int tabPlacement**,  {% include w3api/param_description.html metodo=_dato parametro="int tabPlacement" %}
* **Rectangle tabRect**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle tabRect" %}
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
