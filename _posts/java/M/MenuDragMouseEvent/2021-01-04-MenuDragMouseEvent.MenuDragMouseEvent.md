---
title: MenuDragMouseEvent.MenuDragMouseEvent()
permalink: Java/MenuDragMouseEvent/MenuDragMouseEvent
date: 2021-01-04
key: JavaJava.M.MenuDragMouseEvent
category: java
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
* **int xAbs**,  {% include w3api/param_description.html metodo=_data parametro="int xAbs" %}
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **int id**,  {% include w3api/param_description.html metodo=_data parametro="int id" %}
* **int yAbs**,  {% include w3api/param_description.html metodo=_data parametro="int yAbs" %}
* **MenuSelectionManager m**,  {% include w3api/param_description.html metodo=_data parametro="MenuSelectionManager m" %}
* **Component source**,  {% include w3api/param_description.html metodo=_data parametro="Component source" %}
* **int modifiers**,  {% include w3api/param_description.html metodo=_data parametro="int modifiers" %}
* **long when**,  {% include w3api/param_description.html metodo=_data parametro="long when" %}
* **int clickCount**,  {% include w3api/param_description.html metodo=_data parametro="int clickCount" %}
* **MenuElement[] p**,  {% include w3api/param_description.html metodo=_data parametro="MenuElement[] p" %}
* **boolean popupTrigger**,  {% include w3api/param_description.html metodo=_data parametro="boolean popupTrigger" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

## Clase Padre
[MenuDragMouseEvent](/Java/MenuDragMouseEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MenuDragMouseEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
