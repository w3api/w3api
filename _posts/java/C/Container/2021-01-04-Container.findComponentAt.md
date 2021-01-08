---
title: Container.findComponentAt()
permalink: Java/Container/findComponentAt
date: 2021-01-04
key: JavaJava.C.Container
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Container.metodos valor="findComponentAt" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Component findComponentAt(int x, int y)
public Component findComponentAt(Point p)
~~~

## Parámetros
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **Point p**,  {% include w3api/param_description.html metodo=_data parametro="Point p" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Container](/Java/Container/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.Container.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
