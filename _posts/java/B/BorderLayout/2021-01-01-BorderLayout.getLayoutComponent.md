---
title: BorderLayout.getLayoutComponent()
permalink: Java/BorderLayout/getLayoutComponent
date: 2021-01-11
key: JavaJava.B.BorderLayout
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BorderLayout.metodos valor="getLayoutComponent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Component getLayoutComponent(Container target, Object constraints)
public Component getLayoutComponent(Object constraints)
~~~

## Parámetros
* **Container target**,  {% include w3api/param_description.html metodo=_dato parametro="Container target" %}
* **Object constraints**,  {% include w3api/param_description.html metodo=_dato parametro="Object constraints" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[BorderLayout](/Java/BorderLayout/)

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
