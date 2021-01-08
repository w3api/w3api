---
title: ContextMenu.show()
permalink: Java/ContextMenu/show
date: 2021-01-04
key: JavaJava.C.ContextMenu
category: java
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
* **Node anchor**,  {% include w3api/param_description.html metodo=_data parametro="Node anchor" %}
* **Side side**,  {% include w3api/param_description.html metodo=_data parametro="Side side" %}
* **double dy**,  {% include w3api/param_description.html metodo=_data parametro="double dy" %}
* **double dx**,  {% include w3api/param_description.html metodo=_data parametro="double dx" %}
* **double screenX**,  {% include w3api/param_description.html metodo=_data parametro="double screenX" %}
* **double screenY**,  {% include w3api/param_description.html metodo=_data parametro="double screenY" %}

## Clase Padre
[ContextMenu](/Java/ContextMenu/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ContextMenu.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
