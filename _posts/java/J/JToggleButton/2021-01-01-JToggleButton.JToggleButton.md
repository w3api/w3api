---
title: JToggleButton.JToggleButton()
permalink: /Java/JToggleButton/JToggleButton/
date: 2021-01-11
key: Java.J.JToggleButton
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JToggleButton.constructores valor="JToggleButton" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JToggleButton()
public JToggleButton(String text)
public JToggleButton(String text, boolean selected)
public JToggleButton(String text, Icon icon)
public JToggleButton(String text, Icon icon, boolean selected)
public JToggleButton(Action a)
public JToggleButton(Icon icon)
public JToggleButton(Icon icon, boolean selected)
~~~

## Parámetros
* **String text**,  {% include w3api/param_description.html metodo=_dato parametro="String text" %}
* **Action a**,  {% include w3api/param_description.html metodo=_dato parametro="Action a" %}
* **Icon icon**,  {% include w3api/param_description.html metodo=_dato parametro="Icon icon" %}
* **boolean selected**,  {% include w3api/param_description.html metodo=_dato parametro="boolean selected" %}

## Clase Padre
[JToggleButton](/Java/JToggleButton/)

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
