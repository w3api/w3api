---
title: ContextMenu.show()
permalink: /Java/ContextMenu/show/
date: 2021-01-11
key: Java.C.ContextMenu
category: Java
tags: ['java se', 'javafx.scene.control', 'javafx.controls', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ContextMenu.metodos valor="show" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void show(Node anchor, double screenX, double screenY)
public void show(Node anchor, Side side, double dx, double dy)
~~~

## Parámetros
* **double dx**,  {% include w3api/param_description.html metodo=_dato parametro="double dx" %}
* **double screenX**,  {% include w3api/param_description.html metodo=_dato parametro="double screenX" %}
* **Side side**,  {% include w3api/param_description.html metodo=_dato parametro="Side side" %}
* **Node anchor**,  {% include w3api/param_description.html metodo=_dato parametro="Node anchor" %}
* **double screenY**,  {% include w3api/param_description.html metodo=_dato parametro="double screenY" %}
* **double dy**,  {% include w3api/param_description.html metodo=_dato parametro="double dy" %}

## Clase Padre
[ContextMenu](/Java/ContextMenu/)

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
