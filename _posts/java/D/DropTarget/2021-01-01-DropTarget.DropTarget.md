---
title: DropTarget.DropTarget()
permalink: /Java/DropTarget/DropTarget/
date: 2021-01-11
key: Java.D.DropTarget
category: Java
tags: ['java se', 'java.awt.dnd', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DropTarget.constructores valor="DropTarget" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DropTarget() throws HeadlessException
public DropTarget(Component c, int ops, DropTargetListener dtl) throws HeadlessException
public DropTarget(Component c, int ops, DropTargetListener dtl, boolean act) throws HeadlessException
public DropTarget(Component c, int ops, DropTargetListener dtl, boolean act, FlavorMap fm) throws HeadlessException
public DropTarget(Component c, DropTargetListener dtl) throws HeadlessException
~~~

## Parámetros
* **int ops**,  {% include w3api/param_description.html metodo=_dato parametro="int ops" %}
* **boolean act**,  {% include w3api/param_description.html metodo=_dato parametro="boolean act" %}
* **DropTargetListener dtl**,  {% include w3api/param_description.html metodo=_dato parametro="DropTargetListener dtl" %}
* **FlavorMap fm**,  {% include w3api/param_description.html metodo=_dato parametro="FlavorMap fm" %}
* **Component c**,  {% include w3api/param_description.html metodo=_dato parametro="Component c" %}

## Excepciones
[HeadlessException](/Java/HeadlessException/)

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
