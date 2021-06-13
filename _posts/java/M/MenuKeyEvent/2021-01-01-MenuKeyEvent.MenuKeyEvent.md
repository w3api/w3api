---
title: MenuKeyEvent.MenuKeyEvent()
permalink: Java/MenuKeyEvent/MenuKeyEvent
date: 2021-01-11
key: JavaJava.M.MenuKeyEvent
category: Java
tags: ['java se', 'javax.swing.event', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MenuKeyEvent.constructores valor="MenuKeyEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MenuKeyEvent(Component source, int id, long when, int modifiers, int keyCode, char keyChar, MenuElement[] p, MenuSelectionManager m)
~~~

## Parámetros
* **int modifiers**,  {% include w3api/param_description.html metodo=_dato parametro="int modifiers" %}
* **long when**,  {% include w3api/param_description.html metodo=_dato parametro="long when" %}
* **int id**,  {% include w3api/param_description.html metodo=_dato parametro="int id" %}
* **MenuElement[] p**,  {% include w3api/param_description.html metodo=_dato parametro="MenuElement[] p" %}
* **MenuSelectionManager m**,  {% include w3api/param_description.html metodo=_dato parametro="MenuSelectionManager m" %}
* **int keyCode**,  {% include w3api/param_description.html metodo=_dato parametro="int keyCode" %}
* **char keyChar**,  {% include w3api/param_description.html metodo=_dato parametro="char keyChar" %}
* **Component source**,  {% include w3api/param_description.html metodo=_dato parametro="Component source" %}

## Clase Padre
[MenuKeyEvent](/Java/MenuKeyEvent/)

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
