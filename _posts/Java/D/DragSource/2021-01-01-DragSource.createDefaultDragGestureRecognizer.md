---
title: DragSource.createDefaultDragGestureRecognizer()
permalink: /Java/DragSource/createDefaultDragGestureRecognizer/
date: 2021-01-11
key: Java.D.DragSource
category: Java
tags: ['java se', 'java.awt.dnd', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DragSource.metodos valor="createDefaultDragGestureRecognizer" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DragGestureRecognizer createDefaultDragGestureRecognizer(Component c, int actions, DragGestureListener dgl)
~~~

## Parámetros
* **DragGestureListener dgl**,  {% include w3api/param_description.html metodo=_dato parametro="DragGestureListener dgl" %}
* **int actions**,  {% include w3api/param_description.html metodo=_dato parametro="int actions" %}
* **Component c**,  {% include w3api/param_description.html metodo=_dato parametro="Component c" %}

## Clase Padre
[DragSource](/Java/DragSource/)

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
