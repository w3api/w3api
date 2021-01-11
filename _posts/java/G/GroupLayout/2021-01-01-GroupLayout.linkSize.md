---
title: GroupLayout.linkSize()
permalink: Java/GroupLayout/linkSize
date: 2021-01-11
key: JavaJava.G.GroupLayout
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GroupLayout.metodos valor="linkSize" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void linkSize(int axis, Component... components)
public void linkSize(Component... components)
~~~

## Parámetros
* **int axis**,  {% include w3api/param_description.html metodo=_dato parametro="int axis" %}
* **Component... components**,  {% include w3api/param_description.html metodo=_dato parametro="Component... components" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[GroupLayout](/Java/GroupLayout/)

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
