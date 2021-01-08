---
title: UndoManager.undoOrRedo()
permalink: Java/UndoManager/undoOrRedo
date: 2021-01-04
key: JavaJava.U.UndoManager
category: java
tags: ['java se', 'javax.swing.undo', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.UndoManager.metodos valor="undoOrRedo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void undoOrRedo() throws CannotRedoException, CannotUndoException
~~~

## Excepciones
[CannotRedoException](/Java/CannotRedoException/), [CannotUndoException](/Java/CannotUndoException/)

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
