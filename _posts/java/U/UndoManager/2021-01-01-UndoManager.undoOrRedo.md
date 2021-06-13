---
title: UndoManager.undoOrRedo()
permalink: /Java/UndoManager/undoOrRedo/
date: 2021-01-11
key: Java.U.UndoManager
category: Java
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
[CannotUndoException](/Java/CannotUndoException/), [CannotRedoException](/Java/CannotRedoException/)

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
