---
title: TaskEvent.TaskEvent()
permalink: /Java/TaskEvent/TaskEvent/
date: 2021-01-11
key: Java.T.TaskEvent
category: Java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TaskEvent.constructores valor="TaskEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TaskEvent(TaskEvent.Kind kind)
public TaskEvent(TaskEvent.Kind kind, CompilationUnitTree unit)
public TaskEvent(TaskEvent.Kind kind, CompilationUnitTree unit, TypeElement clazz)
public TaskEvent(TaskEvent.Kind kind, JavaFileObject sourceFile)
~~~

## Parámetros
* **TypeElement clazz**,  {% include w3api/param_description.html metodo=_dato parametro="TypeElement clazz" %}
* **JavaFileObject sourceFile**,  {% include w3api/param_description.html metodo=_dato parametro="JavaFileObject sourceFile" %}
* **CompilationUnitTree unit**,  {% include w3api/param_description.html metodo=_dato parametro="CompilationUnitTree unit" %}
* **TaskEvent.Kind kind**,  {% include w3api/param_description.html metodo=_dato parametro="TaskEvent.Kind kind" %}

## Clase Padre
[TaskEvent](/Java/TaskEvent/)

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
