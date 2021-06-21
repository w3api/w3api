---
title: JMenuItem.processMouseEvent()
permalink: /Java/JMenuItem/processMouseEvent/
date: 2021-01-11
key: Java.J.JMenuItem
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JMenuItem.metodos valor="processMouseEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void processMouseEvent(MouseEvent e, MenuElement[] path, MenuSelectionManager manager)
~~~

## Parámetros
* **MenuElement[] path**,  {% include w3api/param_description.html metodo=_dato parametro="MenuElement[] path" %}
* **MouseEvent e**,  {% include w3api/param_description.html metodo=_dato parametro="MouseEvent e" %}
* **MenuSelectionManager manager**,  {% include w3api/param_description.html metodo=_dato parametro="MenuSelectionManager manager" %}

## Clase Padre
[JMenuItem](/Java/JMenuItem/)

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
