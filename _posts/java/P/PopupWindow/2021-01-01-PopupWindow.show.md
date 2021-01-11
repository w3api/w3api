---
title: PopupWindow.show()
permalink: Java/PopupWindow/show
date: 2021-01-11
key: JavaJava.P.PopupWindow
category: java
tags: ['java se', 'javafx.stage', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PopupWindow.metodos valor="show" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void show(Node ownerNode, double anchorX, double anchorY)
public void show(Window owner)
public void show(Window ownerWindow, double anchorX, double anchorY)
~~~

## Parámetros
* **Node ownerNode**,  {% include w3api/param_description.html metodo=_dato parametro="Node ownerNode" %}
* **double anchorX**,  {% include w3api/param_description.html metodo=_dato parametro="double anchorX" %}
* **Window ownerWindow**,  {% include w3api/param_description.html metodo=_dato parametro="Window ownerWindow" %}
* **double anchorY**,  {% include w3api/param_description.html metodo=_dato parametro="double anchorY" %}
* **Window owner**,  {% include w3api/param_description.html metodo=_dato parametro="Window owner" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[PopupWindow](/Java/PopupWindow/)

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
