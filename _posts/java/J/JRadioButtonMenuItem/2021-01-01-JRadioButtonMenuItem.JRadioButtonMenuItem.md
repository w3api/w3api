---
title: JRadioButtonMenuItem.JRadioButtonMenuItem()
permalink: Java/JRadioButtonMenuItem/JRadioButtonMenuItem
date: 2021-01-11
key: JavaJava.J.JRadioButtonMenuItem
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JRadioButtonMenuItem.constructores valor="JRadioButtonMenuItem" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JRadioButtonMenuItem()
public JRadioButtonMenuItem(String text)
public JRadioButtonMenuItem(String text, boolean selected)
public JRadioButtonMenuItem(String text, Icon icon)
public JRadioButtonMenuItem(String text, Icon icon, boolean selected)
public JRadioButtonMenuItem(Action a)
public JRadioButtonMenuItem(Icon icon)
public JRadioButtonMenuItem(Icon icon, boolean selected)
~~~

## Parámetros
* **String text**,  {% include w3api/param_description.html metodo=_dato parametro="String text" %}
* **Action a**,  {% include w3api/param_description.html metodo=_dato parametro="Action a" %}
* **Icon icon**,  {% include w3api/param_description.html metodo=_dato parametro="Icon icon" %}
* **boolean selected**,  {% include w3api/param_description.html metodo=_dato parametro="boolean selected" %}

## Clase Padre
[JRadioButtonMenuItem](/Java/JRadioButtonMenuItem/)

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
