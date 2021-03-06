---
title: JPopupMenu.insert()
permalink: /Java/JPopupMenu/insert/
date: 2021-01-11
key: Java.J.JPopupMenu
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JPopupMenu.metodos valor="insert" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void insert(Component component, int index)
public void insert(Action a, int index)
~~~

## Parámetros
* **Action a**,  {% include w3api/param_description.html metodo=_dato parametro="Action a" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}
* **Component component**,  {% include w3api/param_description.html metodo=_dato parametro="Component component" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JPopupMenu](/Java/JPopupMenu/)

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
