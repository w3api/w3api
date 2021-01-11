---
title: JLayeredPane.setLayer()
permalink: Java/JLayeredPane/setLayer
date: 2021-01-11
key: JavaJava.J.JLayeredPane
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JLayeredPane.metodos valor="setLayer" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setLayer(Component c, int layer)
public void setLayer(Component c, int layer, int position)
~~~

## Parámetros
* **int position**,  {% include w3api/param_description.html metodo=_dato parametro="int position" %}
* **int layer**,  {% include w3api/param_description.html metodo=_dato parametro="int layer" %}
* **Component c**,  {% include w3api/param_description.html metodo=_dato parametro="Component c" %}

## Clase Padre
[JLayeredPane](/Java/JLayeredPane/)

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
