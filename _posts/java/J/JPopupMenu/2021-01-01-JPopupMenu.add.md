---
title: JPopupMenu.add()
permalink: /Java/JPopupMenu/add/
date: 2021-01-11
key: Java.J.JPopupMenu
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JPopupMenu.metodos valor="add" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JMenuItem add(String s)
public JMenuItem add(Action a)
public JMenuItem add(JMenuItem menuItem)
~~~

## Parámetros
* **Action a**,  {% include w3api/param_description.html metodo=_dato parametro="Action a" %}
* **JMenuItem menuItem**,  {% include w3api/param_description.html metodo=_dato parametro="JMenuItem menuItem" %}
* **String s**,  {% include w3api/param_description.html metodo=_dato parametro="String s" %}

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
