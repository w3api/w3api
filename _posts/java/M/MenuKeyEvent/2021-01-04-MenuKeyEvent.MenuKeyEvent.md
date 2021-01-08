---
title: MenuKeyEvent.MenuKeyEvent()
permalink: Java/MenuKeyEvent/MenuKeyEvent
date: 2021-01-04
key: JavaJava.M.MenuKeyEvent
category: java
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
* **char keyChar**,  {% include w3api/param_description.html metodo=_data parametro="char keyChar" %}
* **int id**,  {% include w3api/param_description.html metodo=_data parametro="int id" %}
* **MenuSelectionManager m**,  {% include w3api/param_description.html metodo=_data parametro="MenuSelectionManager m" %}
* **Component source**,  {% include w3api/param_description.html metodo=_data parametro="Component source" %}
* **int modifiers**,  {% include w3api/param_description.html metodo=_data parametro="int modifiers" %}
* **int keyCode**,  {% include w3api/param_description.html metodo=_data parametro="int keyCode" %}
* **long when**,  {% include w3api/param_description.html metodo=_data parametro="long when" %}
* **MenuElement[] p**,  {% include w3api/param_description.html metodo=_data parametro="MenuElement[] p" %}

## Clase Padre
[MenuKeyEvent](/Java/MenuKeyEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MenuKeyEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
