---
title: MenuElement.processMouseEvent()
permalink: /Java/MenuElement/processMouseEvent/
date: 2021-01-11
key: Java.M.MenuElement
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MenuElement.metodos valor="processMouseEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void processMouseEvent(MouseEvent event, MenuElement[] path, MenuSelectionManager manager)
~~~

## Parámetros
* **MenuElement[] path**,  {% include w3api/param_description.html metodo=_dato parametro="MenuElement[] path" %}
* **MouseEvent event**,  {% include w3api/param_description.html metodo=_dato parametro="MouseEvent event" %}
* **MenuSelectionManager manager**,  {% include w3api/param_description.html metodo=_dato parametro="MenuSelectionManager manager" %}

## Clase Padre
[MenuElement](/Java/MenuElement/)

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
