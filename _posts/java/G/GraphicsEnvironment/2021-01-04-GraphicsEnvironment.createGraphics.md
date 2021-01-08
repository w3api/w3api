---
title: GraphicsEnvironment.createGraphics()
permalink: Java/GraphicsEnvironment/createGraphics
date: 2021-01-04
key: JavaJava.G.GraphicsEnvironment
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GraphicsEnvironment.metodos valor="createGraphics" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Graphics2D createGraphics(BufferedImage img)
~~~

## Parámetros
* **BufferedImage img**,  {% include w3api/param_description.html metodo=_data parametro="BufferedImage img" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[GraphicsEnvironment](/Java/GraphicsEnvironment/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.G.GraphicsEnvironment.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
