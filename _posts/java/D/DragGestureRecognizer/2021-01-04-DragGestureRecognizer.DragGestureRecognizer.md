---
title: DragGestureRecognizer.DragGestureRecognizer()
permalink: Java/DragGestureRecognizer/DragGestureRecognizer
date: 2021-01-04
key: JavaJava.D.DragGestureRecognizer
category: java
tags: ['java se', 'java.awt.dnd', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DragGestureRecognizer.constructores valor="DragGestureRecognizer" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected DragGestureRecognizer(DragSource ds)
protected DragGestureRecognizer(DragSource ds, Component c)
protected DragGestureRecognizer(DragSource ds, Component c, int sa)
protected DragGestureRecognizer(DragSource ds, Component c, int sa, DragGestureListener dgl)
~~~

## Parámetros
* **DragSource ds**,  {% include w3api/param_description.html metodo=_data parametro="DragSource ds" %}
* **DragGestureListener dgl**,  {% include w3api/param_description.html metodo=_data parametro="DragGestureListener dgl" %}
* **Component c**,  {% include w3api/param_description.html metodo=_data parametro="Component c" %}
* **int sa**,  {% include w3api/param_description.html metodo=_data parametro="int sa" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DragGestureRecognizer](/Java/DragGestureRecognizer/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DragGestureRecognizer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
