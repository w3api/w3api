---
title: DropTarget.dragEnter()
permalink: Java/DropTarget/dragEnter
date: 2021-01-11
key: JavaJava.D.DropTarget
category: java
tags: ['java se', 'java.awt.dnd', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DropTarget.metodos valor="dragEnter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void dragEnter(DropTargetDragEvent dtde)
~~~

## Parámetros
* **DropTargetDragEvent dtde**,  {% include w3api/param_description.html metodo=_dato parametro="DropTargetDragEvent dtde" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[DropTarget](/Java/DropTarget/)

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