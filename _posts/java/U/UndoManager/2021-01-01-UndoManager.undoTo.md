---
title: UndoManager.undoTo()
permalink: Java/UndoManager/undoTo
date: 2021-01-11
key: JavaJava.U.UndoManager
category: java
tags: ['java se', 'javax.swing.undo', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.UndoManager.metodos valor="undoTo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void undoTo(UndoableEdit edit) throws CannotUndoException
~~~

## Parámetros
* **UndoableEdit edit**,  {% include w3api/param_description.html metodo=_dato parametro="UndoableEdit edit" %}

## Excepciones
[CannotUndoException](/Java/CannotUndoException/)

## Clase Padre
[UndoManager](/Java/UndoManager/)

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
