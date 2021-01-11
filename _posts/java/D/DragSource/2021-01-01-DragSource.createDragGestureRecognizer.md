---
title: DragSource.createDragGestureRecognizer()
permalink: Java/DragSource/createDragGestureRecognizer
date: 2021-01-11
key: JavaJava.D.DragSource
category: java
tags: ['java se', 'java.awt.dnd', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DragSource.metodos valor="createDragGestureRecognizer" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<T extends DragGestureRecognizer>T createDragGestureRecognizer(Class<T> recognizerAbstractClass, Component c, int actions, DragGestureListener dgl)
~~~

## Parámetros
* **Class&lt;T&gt; recognizerAbstractClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<T> recognizerAbstractClass" %}
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
