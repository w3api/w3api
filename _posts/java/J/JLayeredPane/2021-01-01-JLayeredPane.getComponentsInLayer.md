---
title: JLayeredPane.getComponentsInLayer()
permalink: /Java/JLayeredPane/getComponentsInLayer/
date: 2021-01-11
key: Java.J.JLayeredPane
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JLayeredPane.metodos valor="getComponentsInLayer" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Component[] getComponentsInLayer(int layer)
~~~

## Parámetros
* **int layer**,  {% include w3api/param_description.html metodo=_dato parametro="int layer" %}

## Clase Padre
[JLayeredPane](/Java/JLayeredPane/)

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
