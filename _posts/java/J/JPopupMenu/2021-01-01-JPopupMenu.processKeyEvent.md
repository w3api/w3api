---
title: JPopupMenu.processKeyEvent()
permalink: Java/JPopupMenu/processKeyEvent
date: 2021-01-11
key: JavaJava.J.JPopupMenu
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JPopupMenu.metodos valor="processKeyEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void processKeyEvent(KeyEvent evt)
public void processKeyEvent(KeyEvent e, MenuElement[] path, MenuSelectionManager manager)
~~~

## Parámetros
* **MenuElement[] path**,  {% include w3api/param_description.html metodo=_dato parametro="MenuElement[] path" %}
* **KeyEvent e**,  {% include w3api/param_description.html metodo=_dato parametro="KeyEvent e" %}
* **KeyEvent evt**,  {% include w3api/param_description.html metodo=_dato parametro="KeyEvent evt" %}
* **MenuSelectionManager manager**,  {% include w3api/param_description.html metodo=_dato parametro="MenuSelectionManager manager" %}

## Clase Padre
[JPopupMenu](/Java/JPopupMenu/)

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
