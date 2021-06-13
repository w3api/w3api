---
title: MouseDragGestureRecognizer.MouseDragGestureRecognizer()
permalink: Java/MouseDragGestureRecognizer/MouseDragGestureRecognizer
date: 2021-01-11
key: JavaJava.M.MouseDragGestureRecognizer
category: Java
tags: ['java se', 'java.awt.dnd', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MouseDragGestureRecognizer.constructores valor="MouseDragGestureRecognizer" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected MouseDragGestureRecognizer(DragSource ds)
protected MouseDragGestureRecognizer(DragSource ds, Component c)
protected MouseDragGestureRecognizer(DragSource ds, Component c, int act)
protected MouseDragGestureRecognizer(DragSource ds, Component c, int act, DragGestureListener dgl)
~~~

## Parámetros
* **int act**,  {% include w3api/param_description.html metodo=_dato parametro="int act" %}
* **DragSource ds**,  {% include w3api/param_description.html metodo=_dato parametro="DragSource ds" %}
* **DragGestureListener dgl**,  {% include w3api/param_description.html metodo=_dato parametro="DragGestureListener dgl" %}
* **Component c**,  {% include w3api/param_description.html metodo=_dato parametro="Component c" %}

## Clase Padre
[MouseDragGestureRecognizer](/Java/MouseDragGestureRecognizer/)

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
