---
title: JPopupMenu.processMouseEvent()
permalink: Java/JPopupMenu/processMouseEvent
date: 2021-01-04
key: JavaJava.J.JPopupMenu
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JPopupMenu.metodos valor="processMouseEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void processMouseEvent(MouseEvent event, MenuElement[] path, MenuSelectionManager manager)
~~~

## Parámetros
* **MenuSelectionManager manager**,  {% include w3api/param_description.html metodo=_data parametro="MenuSelectionManager manager" %}
* **MenuElement[] path**,  {% include w3api/param_description.html metodo=_data parametro="MenuElement[] path" %}
* **MouseEvent event**,  {% include w3api/param_description.html metodo=_data parametro="MouseEvent event" %}

## Clase Padre
[JPopupMenu](/Java/JPopupMenu/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JPopupMenu.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
