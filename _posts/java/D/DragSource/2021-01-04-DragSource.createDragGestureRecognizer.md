---
title: DragSource.createDragGestureRecognizer()
permalink: Java/DragSource/createDragGestureRecognizer
date: 2021-01-04
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
* **int actions**,  {% include w3api/param_description.html metodo=_data parametro="int actions" %}
* **DragGestureListener dgl**,  {% include w3api/param_description.html metodo=_data parametro="DragGestureListener dgl" %}
* **Class&lt;T&gt; recognizerAbstractClass**,  {% include w3api/param_description.html metodo=_data parametro="Class<T> recognizerAbstractClass" %}
* **Component c**,  {% include w3api/param_description.html metodo=_data parametro="Component c" %}

## Clase Padre
[DragSource](/Java/DragSource/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DragSource.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
