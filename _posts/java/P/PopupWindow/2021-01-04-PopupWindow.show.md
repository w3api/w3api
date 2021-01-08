---
title: PopupWindow.show()
permalink: Java/PopupWindow/show
date: 2021-01-04
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
* **double anchorX**,  {% include w3api/param_description.html metodo=_data parametro="double anchorX" %}
* **double anchorY**,  {% include w3api/param_description.html metodo=_data parametro="double anchorY" %}
* **Node ownerNode**,  {% include w3api/param_description.html metodo=_data parametro="Node ownerNode" %}
* **Window owner**,  {% include w3api/param_description.html metodo=_data parametro="Window owner" %}
* **Window ownerWindow**,  {% include w3api/param_description.html metodo=_data parametro="Window ownerWindow" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PopupWindow](/Java/PopupWindow/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PopupWindow.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
