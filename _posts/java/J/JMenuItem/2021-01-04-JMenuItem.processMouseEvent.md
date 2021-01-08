---
title: JMenuItem.processMouseEvent()
permalink: Java/JMenuItem/processMouseEvent
date: 2021-01-04
key: JavaJava.J.JMenuItem
category: java
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
* **MouseEvent e**,  {% include w3api/param_description.html metodo=_data parametro="MouseEvent e" %}
* **MenuSelectionManager manager**,  {% include w3api/param_description.html metodo=_data parametro="MenuSelectionManager manager" %}
* **MenuElement[] path**,  {% include w3api/param_description.html metodo=_data parametro="MenuElement[] path" %}

## Clase Padre
[JMenuItem](/Java/JMenuItem/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JMenuItem.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
