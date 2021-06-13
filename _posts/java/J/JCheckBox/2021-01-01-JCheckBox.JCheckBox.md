---
title: JCheckBox.JCheckBox()
permalink: /Java/JCheckBox/JCheckBox/
date: 2021-01-11
key: Java.J.JCheckBox
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JCheckBox.constructores valor="JCheckBox" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JCheckBox()
public JCheckBox(String text)
public JCheckBox(String text, boolean selected)
public JCheckBox(String text, Icon icon)
public JCheckBox(String text, Icon icon, boolean selected)
public JCheckBox(Action a)
public JCheckBox(Icon icon)
public JCheckBox(Icon icon, boolean selected)
~~~

## Parámetros
* **String text**,  {% include w3api/param_description.html metodo=_dato parametro="String text" %}
* **Action a**,  {% include w3api/param_description.html metodo=_dato parametro="Action a" %}
* **Icon icon**,  {% include w3api/param_description.html metodo=_dato parametro="Icon icon" %}
* **boolean selected**,  {% include w3api/param_description.html metodo=_dato parametro="boolean selected" %}

## Clase Padre
[JCheckBox](/Java/JCheckBox/)

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
