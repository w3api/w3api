---
title: DropTarget.addDropTargetListener()
permalink: Java/DropTarget/addDropTargetListener
date: 2021-01-11
key: JavaJava.D.DropTarget
category: java
tags: ['java se', 'java.awt.dnd', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DropTarget.metodos valor="addDropTargetListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void addDropTargetListener(DropTargetListener dtl) throws TooManyListenersException
~~~

## Parámetros
* **DropTargetListener dtl**,  {% include w3api/param_description.html metodo=_dato parametro="DropTargetListener dtl" %}

## Excepciones
[TooManyListenersException](/Java/TooManyListenersException/)

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
