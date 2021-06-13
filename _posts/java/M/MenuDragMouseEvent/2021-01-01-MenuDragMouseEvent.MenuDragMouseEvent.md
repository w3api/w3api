---
title: MenuDragMouseEvent.MenuDragMouseEvent()
permalink: Java/MenuDragMouseEvent/MenuDragMouseEvent
date: 2021-01-11
key: JavaJava.M.MenuDragMouseEvent
category: Java
tags: ['java se', 'javax.swing.event', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MenuDragMouseEvent.constructores valor="MenuDragMouseEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MenuDragMouseEvent(Component source, int id, long when, int modifiers, int x, int y, int clickCount, boolean popupTrigger, MenuElement[] p, MenuSelectionManager m)
public MenuDragMouseEvent(Component source, int id, long when, int modifiers, int x, int y, int xAbs, int yAbs, int clickCount, boolean popupTrigger, MenuElement[] p, MenuSelectionManager m)
~~~

## Parámetros
* **int modifiers**,  {% include w3api/param_description.html metodo=_dato parametro="int modifiers" %}
* **long when**,  {% include w3api/param_description.html metodo=_dato parametro="long when" %}
* **int id**,  {% include w3api/param_description.html metodo=_dato parametro="int id" %}
* **MenuElement[] p**,  {% include w3api/param_description.html metodo=_dato parametro="MenuElement[] p" %}
* **MenuSelectionManager m**,  {% include w3api/param_description.html metodo=_dato parametro="MenuSelectionManager m" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **int clickCount**,  {% include w3api/param_description.html metodo=_dato parametro="int clickCount" %}
* **boolean popupTrigger**,  {% include w3api/param_description.html metodo=_dato parametro="boolean popupTrigger" %}
* **int xAbs**,  {% include w3api/param_description.html metodo=_dato parametro="int xAbs" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **int yAbs**,  {% include w3api/param_description.html metodo=_dato parametro="int yAbs" %}
* **Component source**,  {% include w3api/param_description.html metodo=_dato parametro="Component source" %}

## Clase Padre
[MenuDragMouseEvent](/Java/MenuDragMouseEvent/)

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
