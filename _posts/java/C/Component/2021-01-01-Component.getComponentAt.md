---
title: Component.getComponentAt()
permalink: Java/Component/getComponentAt
date: 2021-01-11
key: JavaJava.C.Component
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Component.metodos valor="getComponentAt" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Component getComponentAt(int x, int y)
public Component getComponentAt(Point p)
~~~

## Parámetros
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **Point p**,  {% include w3api/param_description.html metodo=_dato parametro="Point p" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}

## Clase Padre
[Component](/Java/Component/)

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
