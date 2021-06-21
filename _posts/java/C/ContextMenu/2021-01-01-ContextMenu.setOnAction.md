---
title: ContextMenu.setOnAction()
permalink: /Java/ContextMenu/setOnAction/
date: 2021-01-11
key: Java.C.ContextMenu
category: Java
tags: ['java se', 'javafx.scene.control', 'javafx.controls', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ContextMenu.metodos valor="setOnAction" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void setOnAction(EventHandler<ActionEvent> value)
~~~

## Parámetros
* **EventHandler&lt;ActionEvent&gt; value**,  {% include w3api/param_description.html metodo=_dato parametro="EventHandler<ActionEvent> value" %}

## Clase Padre
[ContextMenu](/Java/ContextMenu/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
