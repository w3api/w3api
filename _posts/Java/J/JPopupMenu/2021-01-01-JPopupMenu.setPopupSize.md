---
title: JPopupMenu.setPopupSize()
permalink: /Java/JPopupMenu/setPopupSize/
date: 2021-01-11
key: Java.J.JPopupMenu
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JPopupMenu.metodos valor="setPopupSize" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(description="The size of the popup menu") public void setPopupSize(int width, int height)
@BeanProperty(description="The size of the popup menu") public void setPopupSize(Dimension d)
~~~

## Parámetros
* **int height**,  {% include w3api/param_description.html metodo=_dato parametro="int height" %}
* **Dimension d**,  {% include w3api/param_description.html metodo=_dato parametro="Dimension d" %}
* **int width**,  {% include w3api/param_description.html metodo=_dato parametro="int width" %}

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
