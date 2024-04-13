---
title: JComponent.requestFocusInWindow()
permalink: /Java/JComponent/requestFocusInWindow/
date: 2021-01-11
key: Java.J.JComponent
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JComponent.metodos valor="requestFocusInWindow" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean requestFocusInWindow()
protected boolean requestFocusInWindow(boolean temporary)
~~~

## Parámetros
* **boolean temporary**,  {% include w3api/param_description.html metodo=_dato parametro="boolean temporary" %}

## Clase Padre
[JComponent](/Java/JComponent/)

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
