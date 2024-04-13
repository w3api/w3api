---
title: JComponent.printChildren()
permalink: /Java/JComponent/printChildren/
date: 2021-01-11
key: Java.J.JComponent
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JComponent.metodos valor="printChildren" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void printChildren(Graphics g)
~~~

## Parámetros
* **Graphics g**,  {% include w3api/param_description.html metodo=_dato parametro="Graphics g" %}

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
