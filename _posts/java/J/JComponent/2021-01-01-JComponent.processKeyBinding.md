---
title: JComponent.processKeyBinding()
permalink: /Java/JComponent/processKeyBinding/
date: 2021-01-11
key: Java.J.JComponent
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JComponent.metodos valor="processKeyBinding" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected boolean processKeyBinding(KeyStroke ks, KeyEvent e, int condition, boolean pressed)
~~~

## Parámetros
* **KeyStroke ks**,  {% include w3api/param_description.html metodo=_dato parametro="KeyStroke ks" %}
* **int condition**,  {% include w3api/param_description.html metodo=_dato parametro="int condition" %}
* **KeyEvent e**,  {% include w3api/param_description.html metodo=_dato parametro="KeyEvent e" %}
* **boolean pressed**,  {% include w3api/param_description.html metodo=_dato parametro="boolean pressed" %}

## Clase Padre
[JComponent](/Java/JComponent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
