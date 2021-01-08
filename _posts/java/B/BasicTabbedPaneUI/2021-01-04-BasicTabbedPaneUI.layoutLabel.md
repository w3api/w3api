---
title: BasicTabbedPaneUI.layoutLabel()
permalink: Java/BasicTabbedPaneUI/layoutLabel
date: 2021-01-04
key: JavaJava.B.BasicTabbedPaneUI
category: java
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
* **String title**,  {% include w3api/param_description.html metodo=_data parametro="String title" %}
* **int tabIndex**,  {% include w3api/param_description.html metodo=_data parametro="int tabIndex" %}
* **Rectangle tabRect**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle tabRect" %}
* **Rectangle iconRect**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle iconRect" %}
* **int tabPlacement**,  {% include w3api/param_description.html metodo=_data parametro="int tabPlacement" %}
* **Rectangle textRect**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle textRect" %}
* **boolean isSelected**,  {% include w3api/param_description.html metodo=_data parametro="boolean isSelected" %}
* **Icon icon**,  {% include w3api/param_description.html metodo=_data parametro="Icon icon" %}
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
