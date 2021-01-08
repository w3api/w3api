---
title: UndoManager.redoTo()
permalink: Java/UndoManager/redoTo
date: 2021-01-04
key: JavaJava.U.UndoManager
category: java
tags: ['java se', 'javax.swing.undo', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.UndoManager.metodos valor="redoTo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void redoTo(UndoableEdit edit) throws CannotRedoException
~~~

## Parámetros
* **UndoableEdit edit**,  {% include w3api/param_description.html metodo=_data parametro="UndoableEdit edit" %}

## Excepciones
[CannotRedoException](/Java/CannotRedoException/)

## Clase Padre
[UndoManager](/Java/UndoManager/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.U.UndoManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
